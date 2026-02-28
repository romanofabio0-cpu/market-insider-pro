import os
import requests
import random
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] TELEGRAM: %(message)s')

# =====================================================================
# 🔑 CREDENZIALI TELEGRAM - BLINDATE CLOUD MODE
# =====================================================================
# Il token viene letto automaticamente dai GitHub Secrets
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

# INSERISCI QUI IL NOME DEL TUO CANALE (es. "@MarketInsiderPro")
TELEGRAM_CHANNEL_ID = "@IlTuoCanaleMarketInsider" 
# =====================================================================

def generate_telegram_signal():
    assets = ["BTC", "ETH", "SOL", "S&P500", "NVDA"]
    actions = ["Accumulo Istituzionale Rilevato 🟢", "Rischio Volatilità Alto 🔴", "Breakout Tecnico Imminente 🚀"]
    
    msg = f"⚡ **MARKET INSIDER FLASH** ⚡\n\n"
    msg += f"Asset: #{random.choice(assets)}\n"
    msg += f"Status: {random.choice(actions)}\n\n"
    msg += "🔒 Analisi completa e target price sbloccati per i membri VIP.\n"
    msg += "👉 marketinsiderpro.com"
    return msg

def send_to_telegram(message):
    if not TELEGRAM_BOT_TOKEN:
        logging.warning("Simulazione: Token Telegram mancante. Messaggio generato ma non inviato:")
        print(f"\n{message}\n")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        logging.info("Connessione ai server di Telegram...")
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info("✅ Messaggio inviato con successo sul canale Telegram!")
        else:
            logging.error(f"Errore Telegram: {response.text}")
    except Exception as e:
        logging.error(f"Errore di connessione: {e}")

if __name__ == "__main__":
    print("=========================================================")
    print("🚀 MARKET INSIDER PRO - TELEGRAM BROADCASTER             ")
    print("=========================================================")
    messaggio = generate_telegram_signal()
    send_to_telegram(messaggio)
    print("Operazione completata. Motori spenti.")