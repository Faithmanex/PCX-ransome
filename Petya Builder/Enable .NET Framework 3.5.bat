@echo off
title .NET Framework 3.5 Enabler
echo -----------------------------------------------
echo .NET Framework 3.5 Enabler
echo -----------------------------------------------
echo.
net session >NUL 2>&1
if %errorlevel% neq 0 (
echo -----------------------------------------------
echo Administrator privileges required!
echo -----------------------------------------------
pause > NUL
exit
)
echo -----------------------------------------------
echo Insert the Windows DVD and press any key
echo -----------------------------------------------
pause > NUL
FOR %%I IN (D E F G H I J K L M N O P Q R S T U V W X Y Z) DO IF EXIST %%I:\sources\setup.exe (SET CDROM=%%I:& GOTO DONECD)
echo.
echo -----------------------------------------------
echo Windows DVD not found. Operation aborted.
echo -----------------------------------------------
pause > NUL
exit

:DONECD
echo.
echo -----------------------------------------------
echo Found %CDROM% as install CD
echo -----------------------------------------------
echo.
echo -----------------------------------------------
echo Enabling .NET Framework 3.5...
echo -----------------------------------------------
Dism /online /enable-feature /featurename:NetFx3 /All /Source:%CDROM%\sources\sxs /LimitAccess
echo.
echo -----------------------------------------------
echo Done
echo -----------------------------------------------
pause > NUL
exit