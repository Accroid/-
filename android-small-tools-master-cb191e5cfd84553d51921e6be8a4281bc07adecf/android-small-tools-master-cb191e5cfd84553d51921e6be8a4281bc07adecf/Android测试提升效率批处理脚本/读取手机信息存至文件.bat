@ECHO OFF 
ECHO [��ȡ�ֻ���Ϣ]

ECHO -------------------------------

adb shell cat /system/build.prop>%~dp0\phone.info

FOR /F "tokens=1,2 delims==" %%a in (phone.info) do (

 IF %%a == ro.build.version.release SET androidOS=%%b

 IF %%a == ro.product.model SET model=%%b

 IF %%a == ro.product.brand SET brand=%%b

)

del /a/f/q %~dp0\phone.info

ECHO.

ECHO.�ֻ�Ʒ��: %brand%

ECHO.�ֻ��ͺ�: %model%

ECHO.ϵͳ�汾: Android %androidOS%



ECHO.-------------------------------

ECHO.�ֻ�Ʒ��: %brand%>"%~dp0\Phone_%model%.txt"

ECHO.�ֻ��ͺ�: %model%>>"%~dp0\Phone_%model%.txt"

ECHO.ϵͳ�汾: Android %androidOS%>>"%~dp0\Phone_%model%.txt"

ECHO [��ͣ5���Զ��ر�...]

ping -n 5 127.0.0.1>nul

@ECHO ON