#!/usr/bin/env python3
"""
GUI Calculator - Interfaccia Grafica Moderna
Autore: [GAB]
Data: 22/08/2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import utils


class ModernCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🧮 Python Calculator - Versione GUI")
        self.root.geometry("800x700")
        self.root.configure(bg="#2c3e50")
        
        # Impedisce il ridimensionamento
        self.root.resizable(False, False)
        
        # Stili e colori moderni
        self.colors = {
            'bg_primary': '#2c3e50',      # Blu scuro
            'bg_secondary': '#34495e',     # Blu più chiaro
            'accent': '#3498db',           # Blu brillante
            'success': '#27ae60',          # Verde
            'warning': '#f39c12',          # Arancione
            'danger': '#e74c3c',           # Rosso
            'text_light': '#ecf0f1',       # Bianco sporco
            'text_dark': '#2c3e50'         # Scuro per testo su sfondo chiaro
        }
        
        self.setup_styles()
        self.create_widgets()
        self.center_window()
    
    def setup_styles(self):
        """Configura gli stili personalizzati"""
        style = ttk.Style()
        
        # Stile per i pulsanti principali
        style.configure(
            "Modern.TButton",
            foreground=self.colors['text_light'],
            background=self.colors['accent'],
            font=('Segoe UI', 11, 'bold'),
            padding=(10, 8)
        )
        
        # Stile per pulsanti di successo
        style.configure(
            "Success.TButton",
            foreground=self.colors['text_light'],
            background=self.colors['success'],
            font=('Segoe UI', 11, 'bold'),
            padding=(10, 8)
        )
        
        # Stile per pulsanti di attenzione
        style.configure(
            "Warning.TButton",
            foreground=self.colors['text_light'],
            background=self.colors['warning'],
            font=('Segoe UI', 11, 'bold'),
            padding=(10, 8)
        )
    
    def center_window(self):
        """Centra la finestra sullo schermo"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def create_widgets(self):
        """Crea tutti i widget dell'interfaccia"""
        # Frame principale
        main_frame = tk.Frame(self.root, bg=self.colors['bg_primary'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titolo
        title_label = tk.Label(
            main_frame,
            text="🧮 Python Calculator",
            font=('Segoe UI', 24, 'bold'),
            fg=self.colors['text_light'],
            bg=self.colors['bg_primary']
        )
        title_label.pack(pady=(0, 20))
        
        # Sottotitolo
        subtitle_label = tk.Label(
            main_frame,
            text="Calcolatore Avanzato con Funzioni Matematiche",
            font=('Segoe UI', 12),
            fg=self.colors['accent'],
            bg=self.colors['bg_primary']
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Frame per le operazioni di base
        basic_frame = tk.LabelFrame(
            main_frame,
            text="📊 Operazioni di Base",
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['text_light'],
            bg=self.colors['bg_secondary'],
            bd=2,
            relief=tk.GROOVE
        )
        basic_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Pulsanti operazioni di base (2 colonne)
        basic_buttons_frame = tk.Frame(basic_frame, bg=self.colors['bg_secondary'])
        basic_buttons_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Prima riga
        ttk.Button(
            basic_buttons_frame,
            text="➕ Addizione",
            style="Modern.TButton",
            command=self.addizione
        ).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        ttk.Button(
            basic_buttons_frame,
            text="✖️ Moltiplicazione",
            style="Modern.TButton",
            command=self.moltiplicazione
        ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Seconda riga
        ttk.Button(
            basic_buttons_frame,
            text="📅 Data e Ora",
            style="Success.TButton",
            command=self.mostra_data_ora
        ).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        ttk.Button(
            basic_buttons_frame,
            text="🔐 Password",
            style="Warning.TButton",
            command=self.genera_password
        ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Configura il grid per espandere uniformemente
        basic_buttons_frame.grid_columnconfigure(0, weight=1)
        basic_buttons_frame.grid_columnconfigure(1, weight=1)
        
        # Frame per le operazioni avanzate
        advanced_frame = tk.LabelFrame(
            main_frame,
            text="🔬 Operazioni Matematiche Avanzate",
            font=('Segoe UI', 14, 'bold'),
            fg=self.colors['text_light'],
            bg=self.colors['bg_secondary'],
            bd=2,
            relief=tk.GROOVE
        )
        advanced_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Pulsanti operazioni avanzate (3 colonne)
        advanced_buttons_frame = tk.Frame(advanced_frame, bg=self.colors['bg_secondary'])
        advanced_buttons_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Prima riga
        ttk.Button(
            advanced_buttons_frame,
            text="! Fattoriale",
            style="Modern.TButton",
            command=self.fattoriale
        ).grid(row=0, column=0, padx=3, pady=5, sticky="ew")
        
        ttk.Button(
            advanced_buttons_frame,
            text="🔍 Numero Primo",
            style="Modern.TButton",
            command=self.verifica_primo
        ).grid(row=0, column=1, padx=3, pady=5, sticky="ew")
        
        ttk.Button(
            advanced_buttons_frame,
            text="📋 Divisori",
            style="Modern.TButton",
            command=self.trova_divisori
        ).grid(row=0, column=2, padx=3, pady=5, sticky="ew")
        
        # Seconda riga
        ttk.Button(
            advanced_buttons_frame,
            text="📐 MCD & MCM",
            style="Success.TButton",
            command=self.mcd_mcm
        ).grid(row=1, column=0, padx=3, pady=5, sticky="ew")
        
        ttk.Button(
            advanced_buttons_frame,
            text="📊 Media",
            style="Success.TButton",
            command=self.calcola_media
        ).grid(row=1, column=1, padx=3, pady=5, sticky="ew")
        
        ttk.Button(
            advanced_buttons_frame,
            text="🧪 Test Funzioni",
            style="Warning.TButton",
            command=self.test_funzioni
        ).grid(row=1, column=2, padx=3, pady=5, sticky="ew")
        
        # Configura il grid per espandere uniformemente
        for i in range(3):
            advanced_buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Frame informazioni
        info_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        info_frame.pack(fill=tk.X, pady=(20, 0))
        
        info_label = tk.Label(
            info_frame,
            text="💡 Tutti i risultati saranno mostrati in popup con formattazione italiana (punti per migliaia)",
            font=('Segoe UI', 10, 'italic'),
            fg=self.colors['accent'],
            bg=self.colors['bg_primary']
        )
        info_label.pack()
        
        # Pulsante di uscita
        exit_frame = tk.Frame(main_frame, bg=self.colors['bg_primary'])
        exit_frame.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Button(
            exit_frame,
            text="❌ Esci",
            style="Warning.TButton",
            command=self.esci
        ).pack()
    
    def mostra_risultato(self, formula, risultato, titolo="Risultato"):
        """Mostra il risultato in un popup elegante"""
        messaggio = f"Formula: {formula}\n\nRisultato: {risultato}"
        messagebox.showinfo(titolo, messaggio)
    
    def get_number_input(self, prompt, title="Input Numero"):
        """Ottiene un numero dall'utente con dialog"""
        while True:
            try:
                value = simpledialog.askfloat(title, prompt)
                if value is None:  # Utente ha premuto Cancel
                    return None
                return value
            except:
                messagebox.showerror("Errore", "Inserisci un numero valido!")
    
    def get_integer_input(self, prompt, title="Input Numero Intero"):
        """Ottiene un numero intero dall'utente con dialog"""
        while True:
            try:
                value = simpledialog.askinteger(title, prompt)
                if value is None:  # Utente ha premuto Cancel
                    return None
                return value
            except:
                messagebox.showerror("Errore", "Inserisci un numero intero valido!")
    
    def get_string_input(self, prompt, title="Input"):
        """Ottiene una stringa dall'utente con dialog"""
        return simpledialog.askstring(title, prompt)
    
    # Funzioni matematiche
    def addizione(self):
        """Esegue l'addizione di due numeri"""
        num1 = self.get_number_input("Inserisci il primo numero:")
        if num1 is None:
            return
        
        num2 = self.get_number_input("Inserisci il secondo numero:")
        if num2 is None:
            return
        
        risultato = num1 + num2
        formula = f"{utils.formatta_numero(num1)} + {utils.formatta_numero(num2)}"
        self.mostra_risultato(formula, utils.formatta_numero(risultato), "➕ Addizione")
    
    def moltiplicazione(self):
        """Esegue la moltiplicazione di due numeri"""
        num1 = self.get_number_input("Inserisci il primo numero:")
        if num1 is None:
            return
        
        num2 = self.get_number_input("Inserisci il secondo numero:")
        if num2 is None:
            return
        
        risultato = num1 * num2
        formula = f"{utils.formatta_numero(num1)} × {utils.formatta_numero(num2)}"
        self.mostra_risultato(formula, utils.formatta_numero(risultato), "✖️ Moltiplicazione")
    
    def fattoriale(self):
        """Calcola il fattoriale di un numero"""
        n = self.get_integer_input("Inserisci un numero per calcolare il fattoriale:")
        if n is None:
            return
        
        try:
            risultato = utils.calcola_fattoriale(n)
            formula = f"{utils.formatta_numero(n)}!"
            self.mostra_risultato(formula, utils.formatta_numero(risultato), "! Fattoriale")
        except ValueError as e:
            messagebox.showerror("Errore", str(e))
    
    def verifica_primo(self):
        """Verifica se un numero è primo"""
        n = self.get_integer_input("Inserisci un numero da verificare:")
        if n is None:
            return
        
        is_primo = utils.verifica_primo(n)
        formula = f"È {utils.formatta_numero(n)} primo?"
        
        if is_primo:
            risultato = "Sì"
        else:
            fattori = utils.scomponi_in_fattori_primi(n)
            fattori_formattati = ' × '.join([utils.formatta_numero(f) for f in fattori])
            risultato = f"No\nScomposizione: {fattori_formattati}"
        
        self.mostra_risultato(formula, risultato, "🔍 Verifica Numero Primo")
    
    def trova_divisori(self):
        """Trova tutti i divisori di un numero"""
        n = self.get_integer_input("Inserisci un numero per trovare i divisori:")
        if n is None:
            return
        
        divisori = utils.trova_divisori(n)
        divisori_formattati = [utils.formatta_numero(d) for d in divisori]
        formula = f"Divisori di {utils.formatta_numero(n)}"
        self.mostra_risultato(formula, str(divisori_formattati), "📋 Divisori")
    
    def mcd_mcm(self):
        """Calcola MCD e MCM di due numeri"""
        a = self.get_integer_input("Inserisci il primo numero:")
        if a is None:
            return
        
        b = self.get_integer_input("Inserisci il secondo numero:")
        if b is None:
            return
        
        mcd = utils.calcola_mcd(a, b)
        mcm = utils.calcola_mcm(a, b)
        
        formula = f"MCD e MCM di {utils.formatta_numero(a)} e {utils.formatta_numero(b)}"
        risultato = f"MCD = {utils.formatta_numero(mcd)}\nMCM = {utils.formatta_numero(mcm)}"
        self.mostra_risultato(formula, risultato, "📐 MCD & MCM")
    
    def calcola_media(self):
        """Calcola la media di una lista di numeri"""
        numeri_str = self.get_string_input("Inserisci numeri separati da virgola:", "📊 Calcolo Media")
        if not numeri_str:
            return
        
        try:
            numeri = [float(x.strip()) for x in numeri_str.split(",")]
            media = utils.calcola_media(numeri)
            
            numeri_formattati = [utils.formatta_numero(n) for n in numeri]
            formula = f"Media di {numeri_formattati}"
            self.mostra_risultato(formula, utils.formatta_numero(media), "📊 Media")
        except ValueError:
            messagebox.showerror("Errore", "Inserisci numeri validi separati da virgola!")
    
    def genera_password(self):
        """Genera una password casuale"""
        lunghezza = self.get_integer_input("Inserisci la lunghezza della password (default 8):")
        if lunghezza is None:
            lunghezza = 8
        
        password = utils.genera_password(lunghezza)
        formula = f"Password di {lunghezza} caratteri"
        self.mostra_risultato(formula, password, "🔐 Password Generata")
    
    def mostra_data_ora(self):
        """Mostra la data e ora corrente"""
        ora_corrente = datetime.now()
        formula = "Data e ora corrente"
        risultato = ora_corrente.strftime('%d/%m/%Y %H:%M:%S')
        self.mostra_risultato(formula, risultato, "📅 Data e Ora")
    
    def test_funzioni(self):
        """Esegue un test di tutte le funzioni di utilità"""
        test_results = []
        
        # Test calcoli matematici
        test_results.append(f"Media di [1, 2, 3, 4, 5]: {utils.formatta_numero(utils.calcola_media([1, 2, 3, 4, 5]))}")
        test_results.append(f"Fattoriale di 5: {utils.formatta_numero(utils.calcola_fattoriale(5))}")
        test_results.append(f"17 è primo? {utils.verifica_primo(17)}")
        
        divisori_12 = [utils.formatta_numero(d) for d in utils.trova_divisori(12)]
        test_results.append(f"Divisori di 12: {divisori_12}")
        
        test_results.append(f"MCD di 48 e 18: {utils.formatta_numero(utils.calcola_mcd(48, 18))}")
        test_results.append(f"MCM di 12 e 18: {utils.formatta_numero(utils.calcola_mcm(12, 18))}")
        
        # Test utility
        test_results.append(f"Password generata: {utils.genera_password(10)}")
        test_results.append(f"3.661 secondi = {utils.formatta_tempo(3661)}")
        test_results.append(f"25% di 80: {utils.formatta_numero(utils.calcola_percentuale(20, 80))}%")
        
        fattori_12 = ' × '.join([utils.formatta_numero(f) for f in utils.scomponi_in_fattori_primi(12)])
        fattori_30 = ' × '.join([utils.formatta_numero(f) for f in utils.scomponi_in_fattori_primi(30)])
        test_results.append(f"Scomposizione di 12: {fattori_12}")
        test_results.append(f"Scomposizione di 30: {fattori_30}")
        
        risultato = "\n".join(test_results)
        messagebox.showinfo("🧪 Test Funzioni di Utilità", risultato)
    
    def esci(self):
        """Chiude l'applicazione"""
        if messagebox.askokcancel("Uscita", "Vuoi davvero uscire dall'applicazione?"):
            self.root.destroy()
    
    def run(self):
        """Avvia l'interfaccia grafica"""
        self.root.mainloop()


if __name__ == "__main__":
    app = ModernCalculator()
    app.run()