
@echo on
set DST=..\GameData\KramaxAutoPilot\Plugins
set DST2=..\GameData\KramaxAutoPilot
if not exist %DST% mkdir %DST%

copy bin\release\KramaxAutoPilot.dll %DST%
copy Kramax.version %DST2%
copy D:\Users\jbb\github\MiniAVC.dll %DST2%

set VERSIONFILE=Kramax.version
rem The following requires the JQ program, available here: https://stedolan.github.io/jq/download/
c:\local\jq-win64  ".VERSION.MAJOR" %VERSIONFILE% >tmpfile
set /P major=<tmpfile

c:\local\jq-win64  ".VERSION.MINOR"  %VERSIONFILE% >tmpfile
set /P minor=<tmpfile

c:\local\jq-win64  ".VERSION.PATCH"  %VERSIONFILE% >tmpfile
set /P patch=<tmpfile

c:\local\jq-win64  ".VERSION.BUILD"  %VERSIONFILE% >tmpfile
set /P build=<tmpfile
del tmpfile
set VERSION=%major%.%minor%.%patch%
if "%build%" NEQ "0"  set VERSION=%VERSION%.%build%
echo %VERSION%

set RELEASEDIR=d:\Users\jbb\release
set ZIP="c:\Program Files\7-zip\7z.exe"

cd ..

set FILE="%RELEASEDIR%\KramaxAutoPilot-%VERSION%.zip"
IF EXIST %FILE% del /F %FILE%
%ZIP% a -tzip %FILE% GameData\KramaxAutoPilot
pause