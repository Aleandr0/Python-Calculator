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

**🚀 Launcher Semplice (Raccomandato):**
```bash
python start.py
```

**🚀 Launcher Avanzato:**
```bash
python launcher.py
```

**🎨 Interfaccia Grafica:**
```bash
python gui_calculator.py
```

**💻 Interfaccia Console:**
```bash
python main.py
```

## 📁 Struttura del progetto

```
Python_AM/
├── start.py             # 🚀 Launcher semplice (raccomandato)
├── launcher.py          # 🚀 Launcher avanzato con subprocess
├── gui_calculator.py    # 🎨 Interfaccia grafica moderna
├── main.py              # 💻 Interfaccia console principale
├── utils.py             # 🛠️ Funzioni di utilità
├── ui.py                # 📱 Componenti UI aggiuntivi
├── config.py            # ⚙️ Configurazione applicazione
├── requirements.txt     # 📦 Dipendenze del progetto
├── README.md           # 📖 Documentazione
├── .gitignore          # 🚫 File da ignorare in Git
├── data/               # 📊 Cartella dati
├── logs/               # 📝 Cartella log
├── output/             # 📤 Cartella output
└── tests/              # 🧪 Cartella test
```

## 🎯 Funzionalità

L'applicazione include le seguenti funzionalità:

### 🎨 **Interfaccia Grafica Moderna**
- **Layout accattivante** con colori moderni
- **Popup eleganti** per mostrare risultati
- **Pulsanti categorizzati** per facile navigazione
- **Stili personalizzati** e icone intuitive

### 🧮 **Operazioni Matematiche**
1. **➕ Addizione e ✖️ Moltiplicazione** con formattazione italiana
2. **! Fattoriale** per calcoli avanzati
3. **🔍 Verifica numeri primi** con scomposizione in fattori
4. **📋 Divisori** di qualsiasi numero
5. **📐 MCD e MCM** (Massimo Comune Divisore e Minimo Comune Multiplo)
6. **📊 Media** di liste di numeri

### 🛠️ **Utilità Avanzate**
- **🔐 Generatore password** sicure
- **📅 Data e ora** corrente formattata
- **🧪 Test funzioni** per verificare tutte le operazioni
- **📊 Formattazione numeri** italiana (1.234.567,89)

### 💻 **Doppia Interfaccia**
- **🎨 GUI moderna** con tkinter
- **💻 Console classica** per utenti avanzati
- **🚀 Launcher** per scegliere l'interfaccia

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
