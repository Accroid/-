@ECHO OFF

ECHO [��װAPK]

ECHO -------------------------------

ECHO [�ȴ������ֻ�...]

adb wait-for-device

ECHO [��װ] %~nx1

adb install -r %1

ECHO [��ͣ5���Զ��ر�...]

ping -n 5 127.0.0.1>nul

@ECHO ON