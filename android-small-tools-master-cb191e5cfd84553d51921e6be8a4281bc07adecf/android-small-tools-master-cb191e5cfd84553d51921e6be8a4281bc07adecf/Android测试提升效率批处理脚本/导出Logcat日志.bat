@ECHO OFF

ECHO.[����logcat��־]

ECHO.-------------------------------

adb logcat -d>"%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.log"

ECHO.[��ͣ5���Զ��ر�...]

ping -n 5 127.0.0.1>nul

@ECHO ON