# Progetto Python

Un progetto Python creato da zero con una struttura professionale e funzionalità di esempio.

## 📋 Descrizione

Questo progetto dimostra come creare un'applicazione Python completa con:
- Menu interattivo
- Gestione degli input utente
- Calcoli matematici
- Gestione delle date
- Struttura modulare del codice

## 🚀 Come iniziare

### Prerequisiti

- Python 3.7 o superiore
- pip (gestore pacchetti Python)

### Installazione

1. Clona o scarica questo progetto nella tua cartella
2. Apri un terminale nella cartella del progetto
3. Installa le dipendenze (se necessario):
   ```bash
   pip install -r requirements.txt
   ```

### Esecuzione

Per eseguire l'applicazione:

```bash
python main.py
```

## 📁 Struttura del progetto

```
Python_AM/
├── main.py              # File principale dell'applicazione
├── requirements.txt     # Dipendenze del progetto
├── README.md           # Documentazione (questo file)
├── .gitignore          # File da ignorare in Git
└── tests/              # Cartella per i test (da creare)
```

## 🎯 Funzionalità

L'applicazione include le seguenti funzionalità:

1. **Saluto utente**: Chiede il nome e saluta l'utente
2. **Data e ora**: Mostra la data e ora corrente
3. **Calcolo somma**: Calcola la somma di due numeri
4. **Menu interattivo**: Interfaccia utente semplice e intuitiva

## 🛠️ Sviluppo

### Aggiungere nuove funzionalità

1. Aggiungi la tua funzione in `main.py`
2. Aggiorna il menu nella funzione `mostra_menu()`
3. Aggiungi la logica nella funzione `main()`

### Esempio di aggiunta funzionalità:

```python
def mia_nuova_funzione():
    """Descrizione della nuova funzionalità"""
    print("La mia nuova funzionalità!")

# Nel menu:
print("5. Mia nuova funzionalità")

# Nella funzione main:
elif scelta == "5":
    mia_nuova_funzione()
```

## 📝 Note

- Il progetto usa solo librerie standard di Python
- È progettato per essere facilmente estendibile
- Include gestione degli errori di base
- Documentazione completa in italiano

## 🤝 Contribuire

Per contribuire al progetto:

1. Fai un fork del repository
2. Crea un branch per la tua feature
3. Committa le tue modifiche
4. Fai un pull request

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT.

## 👨‍💻 Autore

[Il tuo nome] - 2024

---

**Buon coding! 🐍**
