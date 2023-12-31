@echo off

REM Build the package
echo Building the package...

REM Create the virtual environment
SET VENV_DIR=.venv

IF EXIST "%VENV_DIR%" (
    echo Virtual environment already exists.
) ELSE (
    echo Creating a new virtual environment...
    python -m venv %VENV_DIR%
    echo Virtual environment created.
)


echo Activating the virtual environment...
CALL "%VENV_DIR%\Scripts\activate"
echo Activated Virtual environment

echo Installing the build module...
CALL "%VENV_DIR%\Scripts\python.exe" -m pip install build

python -m build
if %errorlevel% neq 0 exit /b %errorlevel%

setlocal enabledelayedexpansion

:: Path to your pyproject.toml file
set "FILE_PATH=pyproject.toml"

:: Variable to store the version
set "VERSION="

:: Read each line from the file
for /f "tokens=*" %%a in ('type "%FILE_PATH%"') do (
    set "line=%%a"
    
    :: Debug: Show the current line
    echo Reading line: !line!

    :: Check if the line contains 'version ='
    echo !line! | findstr /C:"version =" >nul
    if !errorlevel! == 0 (
        :: Extract the version number
        for /f "tokens=3 delims= " %%b in ("!line!") do (
            echo Found version line: %%b
            set "VERSION=%%b"
            set "VERSION=!VERSION:"=!" 
        )
        goto :found
    )
)

:found
if not defined VERSION (
    echo Version not found.
) else (
    echo Extracted Version: !VERSION!
)


REM Install to testing virtual environment
pip install dist\xmi-!VERSION!-py3-none-any.whl --force-reinstall
pip install pytest

REM Running tests
echo Running tests...
pytest after_install_tests\

endlocal




