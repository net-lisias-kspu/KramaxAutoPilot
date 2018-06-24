#!/usr/bin/env bash

VERSION=$(cat ./KramaxAutoPilot/Version.cs | grep -Po 'public const string Number = "(.+)";' | sed 's/public const string Number = "//' | sed 's/";//')
echo $VERSION
FILE=KramaxAutoPilot-$VERSION.zip
rm $FILE
zip -r $FILE ./GameData/* -x ".*"
zip -d $FILE __MACOSX .DS_Store
mv $FILE ./Archive
