"""
Modulo di utilità per il progetto Python
Contiene funzioni helper e strumenti utili
"""

import math
import random
from typing import List, Tuple


def calcola_media(numeri: List[float]) -> float:
    """
    Calcola la media di una lista di numeri
    
    Args:
        numeri: Lista di numeri
        
    Returns:
        Media dei numeri
    """
    if not numeri:
        return 0.0
    return sum(numeri) / len(numeri)


def calcola_fattoriale(n: int) -> int:
    """
    Calcola il fattoriale di un numero
    
    Args:
        n: Numero intero positivo
        
    Returns:
        Fattoriale del numero
    """
    if n < 0:
        raise ValueError("Il fattoriale non è definito per numeri negativi")
    if n == 0 or n == 1:
        return 1
    return n * calcola_fattoriale(n - 1)


def genera_password(lunghezza: int = 8) -> str:
    """
    Genera una password casuale
    
    Args:
        lunghezza: Lunghezza della password (default: 8)
        
    Returns:
        Password generata
    """
    caratteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))


def verifica_primo(n: int) -> bool:
    """
    Verifica se un numero è primo
    
    Args:
        n: Numero da verificare
        
    Returns:
        True se il numero è primo, False altrimenti
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def trova_divisori(n: int) -> List[int]:
    """
    Trova tutti i divisori di un numero
    
    Args:
        n: Numero di cui trovare i divisori
        
    Returns:
        Lista dei divisori
    """
    divisori = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisori.append(i)
    return divisori


def calcola_mcd(a: int, b: int) -> int:
    """
    Calcola il Massimo Comune Divisore usando l'algoritmo di Euclide
    
    Args:
        a: Primo numero
        b: Secondo numero
        
    Returns:
        MCD dei due numeri
    """
    while b:
        a, b = b, a % b
    return a


def calcola_mcm(a: int, b: int) -> int:
    """
    Calcola il Minimo Comune Multiplo
    
    Args:
        a: Primo numero
        b: Secondo numero
        
    Returns:
        MCM dei due numeri
    """
    return abs(a * b) // calcola_mcd(a, b)


def formatta_tempo(secondi: int) -> str:
    """
    Formatta i secondi in formato leggibile (ore:minuti:secondi)
    
    Args:
        secondi: Numero di secondi
        
    Returns:
        Stringa formattata
    """
    ore = secondi // 3600
    minuti = (secondi % 3600) // 60
    sec = secondi % 60
    
    if ore > 0:
        return f"{ore:02d}:{minuti:02d}:{sec:02d}"
    else:
        return f"{minuti:02d}:{sec:02d}"


def calcola_percentuale(valore: float, totale: float) -> float:
    """
    Calcola la percentuale di un valore rispetto al totale
    
    Args:
        valore: Valore di cui calcolare la percentuale
        totale: Valore totale
        
    Returns:
        Percentuale calcolata
    """
    if totale == 0:
        return 0.0
    return (valore / totale) * 100


def ordina_lista(numeri: List[float], crescente: bool = True) -> List[float]:
    """
    Ordina una lista di numeri
    
    Args:
        numeri: Lista da ordinare
        crescente: True per ordine crescente, False per decrescente
        
    Returns:
        Lista ordinata
    """
    lista_ordinata = sorted(numeri)
    if not crescente:
        lista_ordinata.reverse()
    return lista_ordinata


def trova_min_max(numeri: List[float]) -> Tuple[float, float]:
    """
    Trova il valore minimo e massimo in una lista
    
    Args:
        numeri: Lista di numeri
        
    Returns:
        Tupla (minimo, massimo)
    """
    if not numeri:
        return (0.0, 0.0)
    return (min(numeri), max(numeri))


def scomponi_in_fattori_primi(n: int) -> List[int]:
    """
    Scompone un numero in fattori primi
    
    Args:
        n: Numero da scomporre
        
    Returns:
        Lista dei fattori primi
    """
    if n < 2:
        return []
    
    fattori = []
    
    # Dividi per 2 finché possibile
    while n % 2 == 0:
        fattori.append(2)
        n = n // 2
    
    # Dividi per numeri dispari da 3 in poi
    i = 3
    while i * i <= n:
        while n % i == 0:
            fattori.append(i)
            n = n // i
        i += 2
    
    # Se n è ancora maggiore di 2, allora è un fattore primo
    if n > 2:
        fattori.append(n)
    
    return fattori


def formatta_numero(numero) -> str:
    """
    Formatta un numero con punti come separatori delle migliaia
    
    Args:
        numero: Numero da formattare (int, float, o string)
        
    Returns:
        Stringa formattata con punti per le migliaia
    """
    # Se è una stringa, prova a convertirla
    if isinstance(numero, str):
        try:
            numero = float(numero)
        except ValueError:
            return str(numero)
    
    # Se è un float con decimali, gestisci diversamente
    if isinstance(numero, float):
        if numero.is_integer():
            # È un numero intero, trattalo come tale
            return f"{int(numero):,}".replace(",", ".")
        else:
            # Ha decimali, formatta separatamente
            parte_intera = int(numero)
            parte_decimale = str(numero).split('.')[1]
            return f"{parte_intera:,}".replace(",", ".") + "," + parte_decimale
    
    # È un intero
    return f"{numero:,}".replace(",", ".")


if __name__ == "__main__":
    # Test delle funzioni
    print("Test delle funzioni di utilità:")
    print(f"Media di [1, 2, 3, 4, 5]: {calcola_media([1, 2, 3, 4, 5])}")
    print(f"Fattoriale di 5: {calcola_fattoriale(5)}")
    print(f"Password generata: {genera_password(10)}")
    print(f"17 è primo? {verifica_primo(17)}")
    print(f"Divisori di 12: {trova_divisori(12)}")
    print(f"MCD di 48 e 18: {calcola_mcd(48, 18)}")
    print(f"MCM di 12 e 18: {calcola_mcm(12, 18)}")
    print(f"3661 secondi = {formatta_tempo(3661)}")
    print(f"25% di 80: {calcola_percentuale(20, 80)}%")
    print(f"Lista ordinata [3, 1, 4, 1, 5]: {ordina_lista([3, 1, 4, 1, 5])}")
    print(f"Min e max di [3, 1, 4, 1, 5]: {trova_min_max([3, 1, 4, 1, 5])}")
