#!/usr/bin/env python3
"""
Progetto Python AssetMind- File Principale
Autore: [GAB]
Data: 17/08/2025
"""

import sys
import os
from datetime import datetime
import utils
import tkinter as tk
from tkinter import messagebox


def mostra_popup_risultato(formula, risultato, titolo="Risultato"):
    """Mostra un popup con la formula e il risultato dell'operazione"""
    # Crea una finestra root nascosta per il popup
    root = tk.Tk()
    root.withdraw()  # Nascondi la finestra principale
    
    # Messaggio da mostrare nel popup
    messaggio = f"Formula: {formula}\nRisultato: {risultato}"
    
    # Mostra il popup
    messagebox.showinfo(titolo, messaggio)
    
    # Chiudi la finestra root
    root.destroy()


def saluta_utente():
    """Funzione che saluta l'utente"""
    nome = input("Come ti chiami? ")
    print(f"Ciao {nome}! Benvenuto nel progetto Python!")
    return nome


def mostra_menu():
    """Mostra il menu principale dell'applicazione"""
    print("\n" + "="*50)
    print("MENU PRINCIPALE")
    print("="*50)
    print("1. Saluta utente")
    print("2. Mostra data e ora")
    print("3. Calcola somma")
    print("4. Calcola moltiplicazione")
    print("5. Calcoli matematici avanzati")
    print("6. Genera password")
    print("7. Test funzioni di utilità")
    print("8. Esci")
    print("="*50)


def mostra_data_ora():
    """Mostra la data e ora corrente"""
    ora_corrente = datetime.now()
    print(f"Data e ora corrente: {ora_corrente.strftime('%d/%m/%Y %H:%M:%S')}")


def calcola_somma():
    """Calcola la somma di due numeri inseriti dall'utente"""
    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))
        risultato = num1 + num2
        
        # Mostra il risultato nel popup
        formula = f"{utils.formatta_numero(num1)} + {utils.formatta_numero(num2)}"
        mostra_popup_risultato(formula, utils.formatta_numero(risultato), "Somma")
        
        # Mostra anche nella console
        print(f"La somma di {utils.formatta_numero(num1)} + {utils.formatta_numero(num2)} = {utils.formatta_numero(risultato)}")
    except ValueError:
        print("Errore: Inserisci numeri validi!")


def calcola_moltiplicazione():
    """Calcola la moltiplicazione di due numeri inseriti dall'utente"""
    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))
        risultato = num1 * num2
        
        # Mostra il risultato nel popup
        formula = f"{utils.formatta_numero(num1)} × {utils.formatta_numero(num2)}"
        mostra_popup_risultato(formula, utils.formatta_numero(risultato), "Moltiplicazione")
        
        # Mostra anche nella console
        print(f"La moltiplicazione di {utils.formatta_numero(num1)} × {utils.formatta_numero(num2)} = {utils.formatta_numero(risultato)}")
    except ValueError:
        print("Errore: Inserisci numeri validi!")


def calcoli_matematici_avanzati():
    """Menu per calcoli matematici avanzati"""
    print("\n" + "-"*40)
    print("CALCOLI MATEMATICI AVANZATI")
    print("-"*40)
    print("1. Calcola fattoriale")
    print("2. Verifica se un numero è primo")
    print("3. Trova divisori di un numero")
    print("4. Calcola MCD e MCM")
    print("5. Calcola media di una lista")
    print("6. Torna al menu principale")
    
    scelta = input("Scegli un'opzione (1-6): ")
    
    if scelta == "1":
        try:
            n = int(input("Inserisci un numero per calcolare il fattoriale: "))
            risultato = utils.calcola_fattoriale(n)
            
            # Mostra il risultato nel popup
            formula = f"{utils.formatta_numero(n)}!"
            mostra_popup_risultato(formula, utils.formatta_numero(risultato), "Fattoriale")
            
            print(f"Il fattoriale di {utils.formatta_numero(n)} è: {utils.formatta_numero(risultato)}")
        except ValueError as e:
            print(f"Errore: {e}")
    
    elif scelta == "2":
        try:
            n = int(input("Inserisci un numero da verificare: "))
            is_primo = utils.verifica_primo(n)
            
            if is_primo:
                # È un numero primo
                formula = f"È {utils.formatta_numero(n)} primo?"
                risultato = "Sì"
                mostra_popup_risultato(formula, risultato, "Verifica Numero Primo")
                print(f"{utils.formatta_numero(n)} è un numero primo!")
            else:
                # Non è primo, mostra anche la scomposizione
                fattori = utils.scomponi_in_fattori_primi(n)
                formula = f"È {utils.formatta_numero(n)} primo?"
                fattori_formattati = ' × '.join([utils.formatta_numero(f) for f in fattori])
                risultato = f"No\nScomposizione: {fattori_formattati}"
                mostra_popup_risultato(formula, risultato, "Verifica Numero Primo")
                print(f"{utils.formatta_numero(n)} non è un numero primo.")
                print(f"Scomposizione in fattori primi: {fattori_formattati}")
        except ValueError:
            print("Errore: Inserisci un numero intero valido!")
    
    elif scelta == "3":
        try:
            n = int(input("Inserisci un numero per trovare i divisori: "))
            divisori = utils.trova_divisori(n)
            
            # Mostra il risultato nel popup
            formula = f"Divisori di {utils.formatta_numero(n)}"
            divisori_formattati = [utils.formatta_numero(d) for d in divisori]
            mostra_popup_risultato(formula, str(divisori_formattati), "Divisori")
            
            print(f"I divisori di {utils.formatta_numero(n)} sono: {divisori_formattati}")
        except ValueError:
            print("Errore: Inserisci un numero intero valido!")
    
    elif scelta == "4":
        try:
            a = int(input("Inserisci il primo numero: "))
            b = int(input("Inserisci il secondo numero: "))
            mcd = utils.calcola_mcd(a, b)
            mcm = utils.calcola_mcm(a, b)
            
            # Mostra il risultato nel popup
            formula = f"MCD e MCM di {utils.formatta_numero(a)} e {utils.formatta_numero(b)}"
            risultato = f"MCD = {utils.formatta_numero(mcd)}\nMCM = {utils.formatta_numero(mcm)}"
            mostra_popup_risultato(formula, risultato, "MCD e MCM")
            
            print(f"MCD({utils.formatta_numero(a)}, {utils.formatta_numero(b)}) = {utils.formatta_numero(mcd)}")
            print(f"MCM({utils.formatta_numero(a)}, {utils.formatta_numero(b)}) = {utils.formatta_numero(mcm)}")
        except ValueError:
            print("Errore: Inserisci numeri interi validi!")
    
    elif scelta == "5":
        try:
            numeri_str = input("Inserisci numeri separati da virgola: ")
            numeri = [float(x.strip()) for x in numeri_str.split(",")]
            media = utils.calcola_media(numeri)
            
            # Mostra il risultato nel popup
            numeri_formattati = [utils.formatta_numero(n) for n in numeri]
            formula = f"Media di {numeri_formattati}"
            mostra_popup_risultato(formula, utils.formatta_numero(media), "Media")
            
            print(f"La media dei numeri {numeri_formattati} è: {utils.formatta_numero(media)}")
        except ValueError:
            print("Errore: Inserisci numeri validi separati da virgola!")


def genera_password():
    """Genera una password casuale"""
    try:
        lunghezza = int(input("Inserisci la lunghezza della password (default 8): ") or "8")
        password = utils.genera_password(lunghezza)
        print(f"Password generata: {password}")
    except ValueError:
        print("Errore: Inserisci un numero valido!")


def test_funzioni_utilità():
    """Testa tutte le funzioni di utilità"""
    print("\nTest delle funzioni di utilità:")
    print("-" * 40)
    
    # Test calcoli matematici
    print(f"Media di [1, 2, 3, 4, 5]: {utils.formatta_numero(utils.calcola_media([1, 2, 3, 4, 5]))}")
    print(f"Fattoriale di 5: {utils.formatta_numero(utils.calcola_fattoriale(5))}")
    print(f"17 è primo? {utils.verifica_primo(17)}")
    divisori_12 = [utils.formatta_numero(d) for d in utils.trova_divisori(12)]
    print(f"Divisori di 12: {divisori_12}")
    print(f"MCD di 48 e 18: {utils.formatta_numero(utils.calcola_mcd(48, 18))}")
    print(f"MCM di 12 e 18: {utils.formatta_numero(utils.calcola_mcm(12, 18))}")
    
    # Test utility
    print(f"Password generata: {utils.genera_password(10)}")
    print(f"3.661 secondi in hh:mm:ss = {utils.formatta_tempo(3661)}")
    print(f"20 su 80 = {utils.formatta_numero(utils.calcola_percentuale(20, 80))}%")
    lista_test = [3, 1, 4, 1, 5]
    lista_ordinata = [utils.formatta_numero(n) for n in utils.ordina_lista(lista_test)]
    print(f"Lista ordinata [3, 1, 4, 1, 5]: {lista_ordinata}")
    min_val, max_val = utils.trova_min_max(lista_test)
    print(f"Min e max di [3, 1, 4, 1, 5]: ({utils.formatta_numero(min_val)}, {utils.formatta_numero(max_val)})")
    fattori_12 = ' × '.join([utils.formatta_numero(f) for f in utils.scomponi_in_fattori_primi(12)])
    fattori_30 = ' × '.join([utils.formatta_numero(f) for f in utils.scomponi_in_fattori_primi(30)])
    print(f"Scomposizione di 12: {fattori_12}")
    print(f"Scomposizione di 30: {fattori_30}")


def main():
    """Funzione principale dell'applicazione"""
    print("Benvenuto nel Progetto Python!")
    print("Questo è un progetto di esempio creato da zero.")
    
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-8): ")
        
        if scelta == "1":
            saluta_utente()
        elif scelta == "2":
            mostra_data_ora()
        elif scelta == "3":
            calcola_somma()
        elif scelta == "4":
            calcola_moltiplicazione()
        elif scelta == "5":
            calcoli_matematici_avanzati()
        elif scelta == "6":
            genera_password()
        elif scelta == "7":
            test_funzioni_utilità()
        elif scelta == "8":
            print("Grazie per aver usato l'applicazione! Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
