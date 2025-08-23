#!/usr/bin/env python3
"""
Start - Launcher semplificato per Python Calculator
Autore: [GAB]
Data: 22/08/2025
"""

import tkinter as tk
from tkinter import messagebox


def main():
    """Finestra principale di selezione"""
    # Crea finestra principale
    root = tk.Tk()
    root.title("🚀 Python Calculator")
    root.geometry("400x300")
    root.configure(bg="#2c3e50")
    root.resizable(False, False)
    
    # Centra la finestra
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (200)
    y = (root.winfo_screenheight() // 2) - (150)
    root.geometry(f"+{x}+{y}")
    
    # Frame principale
    frame = tk.Frame(root, bg="#2c3e50", padx=30, pady=30)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Titolo
    title = tk.Label(
        frame,
        text="🧮 Python Calculator",
        font=('Arial', 18, 'bold'),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title.pack(pady=(0, 20))
    
    # Sottotitolo
    subtitle = tk.Label(
        frame,
        text="Scegli l'interfaccia:",
        font=('Arial', 12),
        fg="#3498db",
        bg="#2c3e50"
    )
    subtitle.pack(pady=(0, 20))
    
    def start_gui():
        """Avvia GUI e chiudi launcher"""
        try:
            root.destroy()
            # Nascondi anche la console del launcher se siamo su Windows
            if tk._default_root:
                tk._default_root.withdraw()
            from gui_calculator import ModernCalculator
            app = ModernCalculator()
            app.run()
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nell'avvio GUI:\n{str(e)}")
    
    def start_console():
        """Avvia console e chiudi launcher"""
        try:
            root.destroy()
            import main
            main.main()
        except Exception as e:
            messagebox.showerror("Errore", f"Errore nell'avvio console:\n{str(e)}")
    
    # Pulsante GUI
    btn_gui = tk.Button(
        frame,
        text="🎨 Interfaccia Grafica",
        font=('Arial', 12, 'bold'),
        fg="white",
        bg="#27ae60",
        activebackground="#2ecc71",
        bd=0,
        pady=10,
        command=start_gui
    )
    btn_gui.pack(fill=tk.X, pady=5)
    
    # Pulsante Console
    btn_console = tk.Button(
        frame,
        text="💻 Interfaccia Console",
        font=('Arial', 12),
        fg="white",
        bg="#34495e",
        activebackground="#5d6d7e",
        bd=0,
        pady=10,
        command=start_console
    )
    btn_console.pack(fill=tk.X, pady=5)
    
    # Pulsante Esci
    btn_exit = tk.Button(
        frame,
        text="❌ Esci",
        font=('Arial', 10),
        fg="white",
        bg="#e74c3c",
        activebackground="#c0392b",
        bd=0,
        pady=5,
        command=root.destroy
    )
    btn_exit.pack(pady=(15, 0))
    
    root.mainloop()


if __name__ == "__main__":
    main()