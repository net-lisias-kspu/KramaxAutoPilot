@echo on
set DST=..\GameData\KramaxAutoPilot\Plugins
set DST2=..\GameData\KramaxAutoPilot
if not exist %DST% mkdir %DST%

copy bin\release\KramaxAutoPilot.dll %DST%
copy Kramax.version %DST2%
copy D:\Users\jbb\github\MiniAVC.dll %DST2%

type Kramax.version
set /p VERSION= "Enter version: "

set RELEASEDIR=d:\Users\jbb\release
set ZIP="c:\Program Files\7-zip\7z.exe"

cd ..

set FILE="%RELEASEDIR%\KramaxAutoPilot-%VERSION%.zip"
IF EXIST %FILE% del /F %FILE%
%ZIP% a -tzip %FILE% GameData\KramaxAutoPilot
