#!/usr/bin/env bash

source ../CONFIG.inc

function copyifneeded {
	local src=$1
	local targetdir=$2
	local filename="${fullfile##*/}"

	if [ ! -f $src ] ; then
		return 1
	fi

	if [ ! -f $targetdir/$filename ] ; then
		cp $src $targetdir
		return 0
	fi

	local mtf0=`stat -c %Y $src`
	local mtf1=`stat -c %Y $targetdir/$filename`
	local dt=$(( mtf1 - mtf0 ))
	if [[ $dt -gt 0 ]] ; then
		cp $source $targetdir
	fi
}


DEPLOYDIR=./GameData/KramaxAutoPilot/Plugins
rm $DEPLOYDIR/*.dll
rm $DEPLOYDIR/*.pdb

copyifneeded ./KramaxAutoPilot/bin/Release/KramaxAutoPilot.dll $DEPLOYDIR
copyifneeded ./KramaxAutoPilot/bin/Debug/KramaxAutoPilot.dll $DEPLOYDIR
copyifneeded ./KramaxAutoPilot/bin/Debug/KramaxAutoPilot.pdb $DEPLOYDIR

copyifneeded $DEPLOYDIR/KramaxAutoPilot.dll $KSP_DEV/GameData/KramaxAutoPilot/Plugins
copyifneeded $DEPLOYDIR/KramaxAutoPilot.pdb $KSP_DEV/GameData/KramaxAutoPilot/Plugins
