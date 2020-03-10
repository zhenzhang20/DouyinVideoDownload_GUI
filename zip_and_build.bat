REM 1 	使用py打包： 	pyinstaller -F -w Downloader.py
REM 2 	修改 datas=[], -- > datas=[('Resource', '.')],
REM 3 	pyinstaller -F Downloader.spec

set CURDIR=%~dp0
cd /d %CURDIR%
cd src 
rd dist /S /Q
rd build /S /Q
rd download /S /Q
del Resource\config.json
del Resource\url.txt
del Resource\def_tailerpicture.jpg
del Resource\def_tailervideo.mp4

set "Date=%date:~0,4%%date:~5,2%%date:~8,2%"

cd /d %CURDIR%

7z a -tzip VideoDownload_GUI-douyin-%Date%.7z src


pause

cd /d %CURDIR%/src
pyinstaller -F Downloader.spec

copy dist\Downloader.exe  C:\Users\zz\Desktop\verr\d\