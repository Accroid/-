@ECHO OFF

ECHO [�鿴APK����Ϣ]

ECHO -------------------------------

ECHO aapt dump badging %~nx1

D:\BaiduYunDownload\android-sdk\build-tools\17.0.0\aapt dump badging %1 > %~dp0%~n1.txt

ECHO [��ͣ3���Զ��ر�...]

ping -n 3 127.0.0.1>nul
@ECHO ON