#!/usr/bin/env python3
"""
Script per creare l'eseguibile del Python Calculator
Autore: [GAB]
Data: 22/08/2025
"""

import subprocess
import sys
import os

def build_executable():
    """Crea l'eseguibile usando PyInstaller"""
    
    print("🔨 Creazione eseguibile Python Calculator...")
    print("="*50)
    
    # Parametri per PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",                    # Singolo file eseguibile
        "--windowed",                   # Nessuna finestra console
        "--name", "PythonCalculator",   # Nome dell'eseguibile
        "--icon", "NONE",               # Nessuna icona personalizzata per ora
        "--clean",                      # Pulisci build precedenti
        "gui_calculator.py"             # File principale
    ]
    
    # Aggiungi file aggiuntivi necessari
    cmd.extend([
        "--add-data", "utils.py;.",     # Includi utils.py
    ])
    
    try:
        print(f"🚀 Eseguendo: {' '.join(cmd)}")
        print("-" * 50)
        
        result = subprocess.run(cmd, check=True, capture_output=False)
        
        print("\n" + "="*50)
        print("✅ Eseguibile creato con successo!")
        print("📁 Percorso: dist/PythonCalculator.exe")
        print("📦 Dimensione:", end=" ")
        
        exe_path = "dist/PythonCalculator.exe"
        if os.path.exists(exe_path):
            size = os.path.getsize(exe_path)
            print(f"{size // (1024*1024)} MB")
            print(f"🎯 L'eseguibile è pronto per essere distribuito!")
        else:
            print("File non trovato")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Errore durante la creazione dell'eseguibile: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller non trovato. Installa con: pip install pyinstaller")
        return False
        
    return True

def clean_build_files():
    """Pulisce i file temporanei di build"""
    import shutil
    
    dirs_to_remove = ["build", "__pycache__"]
    files_to_remove = ["PythonCalculator.spec"]
    
    print("\n🧹 Pulizia file temporanei...")
    
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Rimossa cartella: {dir_name}")
    
    for file_name in files_to_remove:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"   Rimosso file: {file_name}")
    
    print("✨ Pulizia completata!")

if __name__ == "__main__":
    print("🧮 Python Calculator - Build Eseguibile")
    print("="*50)
    
    # Verifica che siamo nella directory corretta
    if not os.path.exists("gui_calculator.py"):
        print("❌ File gui_calculator.py non trovato!")
        print("   Esegui questo script dalla cartella del progetto.")
        sys.exit(1)
    
    # Crea l'eseguibile
    if build_executable():
        # Opzionalmente pulisci i file temporanei
        clean_choice = input("\n🧹 Vuoi rimuovere i file temporanei di build? (s/n): ")
        if clean_choice.lower() in ['s', 'si', 'y', 'yes']:
            clean_build_files()
            
        print("\n🎉 Processo completato!")
        print("💡 Puoi ora condividere il file dist/PythonCalculator.exe")
    else:
        print("\n❌ Build fallita!")
        sys.exit(1)