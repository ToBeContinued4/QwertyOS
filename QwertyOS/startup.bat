@echo off
cls
goto verify1

:verify1
if exist sys (
    goto verify2
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify2
if exist apps (
    goto verify3
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify3
if exist sys/base.py (
    goto verify4
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify4
if exist sys/commandmissing.vbs (
    goto verify5
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify5
if exist sys/wrongcommand.vbs (
    goto verify6
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify6
if exist sys/commandlist.txt (
    goto verify7
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:verify7
if exist sys/titleascii.txt (
    goto end
) else (
    echo Critical Error
    timeout /t 4 /nobreak >nul
    exit
)

:end
cd sys
start /max base.py
exit