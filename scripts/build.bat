@echo off
REM Cross-Platform Build Script for Human Typer Mimicker - Windows Version

echo ======================================
echo Human Typer - Windows Builder
echo ======================================

REM Get platform info
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Platform: Windows %PROCESSOR_ARCHITECTURE%
echo Python: %PYTHON_VERSION%
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Clean build directories
echo Cleaning build directories...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
if exist src\__pycache__ rmdir /s /q src\__pycache__

REM Build GUI application
echo Building GUI application...
python -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name "HumanTyperGUI-Windows" ^
    --add-data "src;src" ^
    --distpath dist ^
    --workpath build ^
    src\human_typer_gui.py

REM Build CLI application
echo Building CLI application...
python -m PyInstaller ^
    --onefile ^
    --console ^
    --name "HumanTyper-Windows" ^
    --distpath dist ^
    --workpath build ^
    src\human_typer.py

REM Create distribution package
set DIST_NAME=HumanTyper-Windows-%PROCESSOR_ARCHITECTURE%
set DIST_DIR=dist\%DIST_NAME%

echo Creating distribution package...
mkdir "%DIST_DIR%" 2>nul

REM Copy executables
copy "dist\HumanTyperGUI-Windows.exe" "%DIST_DIR%\" >nul
copy "dist\HumanTyper-Windows.exe" "%DIST_DIR%\" >nul

REM Copy documentation
copy "README.md" "%DIST_DIR%\" >nul 2>&1
copy "LICENSE" "%DIST_DIR%\" >nul 2>&1
copy "CHANGELOG.md" "%DIST_DIR%\" >nul 2>&1
copy "scripts\examples.py" "%DIST_DIR%\examples.py" >nul 2>&1

echo.
echo ======================================
echo Build completed successfully!
echo ======================================
echo Distribution: %DIST_DIR%
echo Executables:
dir "%DIST_DIR%"
echo.
echo To run:
echo   GUI: %DIST_DIR%\HumanTyperGUI-Windows.exe
echo   CLI: %DIST_DIR%\HumanTyper-Windows.exe

pause
