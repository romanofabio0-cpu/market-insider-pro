import requests
import os
import logging

# Configurazione Log
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] BACKEND-CHECK: %(message)s')

# --- CONFIGURAZIONE TARGET ---
CHECK_LIST = {
    "LINKS": [
        "https://marketinsiderpro.com",
        "https://accounts.binance.com/register?ref=1218170181", # Tuo Referral [cite: 2026-02-18]
        "https://stripe.com" # Portale pagamenti [cite: 2026-02-17]
    ],
    "FILES": [
        "modules/builder.py",   # La tua base [cite: 2026-02-23]
        "social_bot.py",
        "test_frontend.py"
    ]
}

def check_links():
    logging.info("--- AVVIO: Link Integrity Check ---")
    for link in CHECK_LIST["LINKS"]:
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                logging.info(f"✅ FUNZIONANTE ({response.status_code}): {link}")
            else:
                logging.warning(f"⚠️ PROBLEMA ({response.status_code}): {link}")
        except Exception as e:
            logging.error(f"❌ ERRORE CRITICO su {link}: {e}")

def check_files():
    logging.info("--- AVVIO: File Integrity Check ---")
    for file in CHECK_LIST["FILES"]:
        if os.path.exists(file):
            size = os.path.getsize(file)
            logging.info(f"✅ PRESENTE: {file} ({size} bytes)")
        else:
            logging.error(f"❌ MANCANTE: {file} - Il sistema potrebbe essere instabile!")

if __name__ == "__main__":
    print("=========================================================")
    print("🤖 MARKET INSIDER PRO - BACKEND VALIDATION SUITE         ")
    print("=========================================================")
    check_files()
    check_links()