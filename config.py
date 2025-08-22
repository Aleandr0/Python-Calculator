"""
File di configurazione per il progetto Python
Contiene impostazioni, costanti e configurazioni
"""

import os
from pathlib import Path

# Configurazioni del progetto
PROJECT_NAME = "Progetto Python"
VERSION = "1.0.0"
AUTHOR = "[Il tuo nome]"
DESCRIPTION = "Un progetto Python completo con funzionalità di esempio"

# Directory del progetto
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Crea le directory se non esistono
for directory in [DATA_DIR, LOGS_DIR, OUTPUT_DIR]:
    directory.mkdir(exist_ok=True)

# Configurazioni dell'applicazione
APP_CONFIG = {
    "debug": True,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "default_language": "it"
}

# Configurazioni matematiche
MATH_CONFIG = {
    "precision": 6,
    "max_factorial": 1000,
    "max_password_length": 50,
    "min_password_length": 4
}

# Configurazioni di output
OUTPUT_CONFIG = {
    "date_format": "%d/%m/%Y %H:%M:%S",
    "number_format": "{:.2f}",
    "separator": "=" * 50
}

# Messaggi dell'applicazione
MESSAGES = {
    "welcome": "Benvenuto nel Progetto Python!",
    "goodbye": "Grazie per aver usato l'applicazione! Arrivederci!",
    "error_invalid_input": "Errore: Inserisci un input valido!",
    "error_number_required": "Errore: Inserisci un numero valido!",
    "success": "Operazione completata con successo!",
    "menu_title": "MENU PRINCIPALE",
    "option_invalid": "Opzione non valida. Riprova."
}

# Colori per l'output (se supportati)
COLORS = {
    "reset": "\033[0m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m"
}

# Configurazioni per i test
TEST_CONFIG = {
    "test_timeout": 10,
    "verbose": True,
    "failfast": False
}

# Funzioni di utilità per la configurazione
def get_config_value(config_dict, key, default=None):
    """
    Ottiene un valore dalla configurazione con fallback al default
    
    Args:
        config_dict: Dizionario di configurazione
        key: Chiave da cercare
        default: Valore di default se la chiave non esiste
        
    Returns:
        Valore della configurazione o default
    """
    return config_dict.get(key, default)

def is_debug_mode():
    """Verifica se il progetto è in modalità debug"""
    return APP_CONFIG.get("debug", False)

def get_log_level():
    """Ottiene il livello di log configurato"""
    return APP_CONFIG.get("log_level", "INFO")

def get_message(key, default=""):
    """Ottiene un messaggio dalla configurazione"""
    return MESSAGES.get(key, default)

def format_number(number):
    """Formatta un numero secondo la configurazione"""
    return OUTPUT_CONFIG["number_format"].format(number)

def get_separator():
    """Ottiene il separatore configurato"""
    return OUTPUT_CONFIG["separator"]

# Configurazioni specifiche per ambiente
if os.getenv("PYTHON_ENV") == "production":
    APP_CONFIG["debug"] = False
    APP_CONFIG["log_level"] = "WARNING"
elif os.getenv("PYTHON_ENV") == "development":
    APP_CONFIG["debug"] = True
    APP_CONFIG["log_level"] = "DEBUG"
