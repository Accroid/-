@ECHO OFF

ECHO.[�����ֻ�����]

ECHO.-------------------------------

ECHO.[Exce ] �ֻ�����

adb shell screencap -p /sdcard/screen.png

ECHO.[Tips ] ��������ͼƬ������

adb pull /sdcard/screen.png "%~dp0\screen.png"

ren screen.png "%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.png"

adb shell rm /sdcard/screen.png

ECHO [��ͣ2���Զ��ر�...]

ping -n 2 127.0.0.1>nul

@ECHO ON