@echo off
echo 🔨 Creazione eseguibile Python Calculator...
echo ==================================================

REM Verifica che PyInstaller sia installato
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo ❌ PyInstaller non installato. Installazione in corso...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo ❌ Errore nell'installazione di PyInstaller
        pause
        exit /b 1
    )
)

REM Crea l'eseguibile
echo 🚀 Creazione eseguibile...
pyinstaller --onefile --windowed --name PythonCalculator --clean gui_calculator.py

if errorlevel 1 (
    echo ❌ Errore nella creazione dell'eseguibile
    pause
    exit /b 1
)

echo.
echo ✅ Eseguibile creato con successo!
echo 📁 Percorso: dist\PythonCalculator.exe
echo.

REM Mostra dimensione file
for %%A in (dist\PythonCalculator.exe) do (
    echo 📦 Dimensione: %%~zA bytes
)

echo.
echo 🎯 L'eseguibile è pronto per essere distribuito!
echo 💡 Puoi copiarlo su altri computer senza Python installato
echo.

set /p cleanup="🧹 Vuoi rimuovere i file temporanei di build? (s/n): "
if /i "%cleanup%"=="s" (
    rmdir /s /q build 2>nul
    del PythonCalculator.spec 2>nul
    echo ✨ File temporanei rimossi!
)

echo.
echo 🎉 Processo completato!
pause