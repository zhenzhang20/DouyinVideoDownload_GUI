REM 1 	使用py打包： 	pyinstaller -F -w Downloader.py
REM 2 	修改 datas=[], -- > datas=[('Resource', '.')],
REM 3 	pyinstaller -F Downloader.spec

set CURDIR=%~dp0
cd /d %CURDIR%
rd dist /S /Q
rd build /S /Q
rd download /S /Q
del Resource\config.json
del Resource\url.txt
del Resource\def_tailerpicture.jpg
del Resource\def_tailervideo.mp4
pyinstaller -F Downloader.spec
