import os
import logging
import sys

# Configurazione Percorsi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "public")

# Configurazione Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)

def get_logger(name):
    return logging.getLogger(name)

# Fix Encoding Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
