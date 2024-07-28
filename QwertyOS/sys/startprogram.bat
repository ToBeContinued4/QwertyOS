@echo off

if not exist ../apps/%1 (
    echo Programa "%1" no existe
    echo.
    pause
    exit
) else (
    cd ../apps/%1
    startup
    exit
)