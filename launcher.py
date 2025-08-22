#!/usr/bin/env python3
"""
Launcher - Scegli come avviare Python Calculator
Autore: [GAB]
Data: 22/08/2025
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys


def launch_console():
    """Avvia la versione console"""
    try:
        subprocess.run([sys.executable, "main.py"], check=True)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore nell'avvio della versione console:\n{e}")


def launch_gui():
    """Avvia la versione GUI"""
    try:
        subprocess.run([sys.executable, "gui_calculator.py"], check=True)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore nell'avvio della versione GUI:\n{e}")


def create_launcher():
    """Crea la finestra di selezione"""
    root = tk.Tk()
    root.title("🚀 Python Calculator - Launcher")
    root.geometry("500x350")
    root.configure(bg="#2c3e50")
    root.resizable(False, False)
    
    # Centra la finestra
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Frame principale
    main_frame = tk.Frame(root, bg="#2c3e50", padx=40, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Titolo
    title_label = tk.Label(
        main_frame,
        text="🚀 Python Calculator",
        font=('Segoe UI', 22, 'bold'),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=(0, 10))
    
    # Sottotitolo
    subtitle_label = tk.Label(
        main_frame,
        text="Scegli come vuoi avviare l'applicazione",
        font=('Segoe UI', 14),
        fg="#3498db",
        bg="#2c3e50"
    )
    subtitle_label.pack(pady=(0, 30))
    
    # Pulsante GUI (più prominente)
    gui_button = tk.Button(
        main_frame,
        text="🎨 Interfaccia Grafica (GUI)\nModerna e Accattivante",
        font=('Segoe UI', 14, 'bold'),
        fg="#ecf0f1",
        bg="#27ae60",
        activebackground="#2ecc71",
        activeforeground="#ecf0f1",
        bd=0,
        pady=15,
        command=lambda: [launch_gui(), root.destroy()]
    )
    gui_button.pack(fill=tk.X, pady=10)
    
    # Pulsante Console
    console_button = tk.Button(
        main_frame,
        text="💻 Interfaccia Console\nClassica a Riga di Comando",
        font=('Segoe UI', 12),
        fg="#ecf0f1",
        bg="#34495e",
        activebackground="#5d6d7e",
        activeforeground="#ecf0f1",
        bd=0,
        pady=12,
        command=lambda: [launch_console(), root.destroy()]
    )
    console_button.pack(fill=tk.X, pady=10)
    
    # Info
    info_label = tk.Label(
        main_frame,
        text="💡 La GUI include tutte le funzioni della versione console\ncon un'interfaccia più intuitiva e popup eleganti",
        font=('Segoe UI', 10, 'italic'),
        fg="#95a5a6",
        bg="#2c3e50",
        justify=tk.CENTER
    )
    info_label.pack(pady=(20, 0))
    
    # Pulsante esci
    exit_button = tk.Button(
        main_frame,
        text="❌ Esci",
        font=('Segoe UI', 10),
        fg="#ecf0f1",
        bg="#e74c3c",
        activebackground="#c0392b",
        activeforeground="#ecf0f1",
        bd=0,
        pady=5,
        command=root.destroy
    )
    exit_button.pack(pady=(15, 0))
    
    root.mainloop()


if __name__ == "__main__":
    create_launcher()