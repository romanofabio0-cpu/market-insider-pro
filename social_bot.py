import tweepy
import logging
import time
import random

# =====================================================================
# CONFIGURAZIONE LOGGING (Standard CI/CD)
# =====================================================================
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] SYSTEM: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# =====================================================================
# 🔑 CREDENZIALI API DI X (TWITTER) - V2
# =====================================================================
API_KEY = "vUXuQbOUmj94iO5JkaDNfheU5"
API_SECRET = "XXfYuHYg6fGEyaY0lAQ1kGIfQ6edk7bKbWza4eX1XAOuU5x6mP"
ACCESS_TOKEN = "2026616179452973056-zBDdAEuVI7n8QXluyDA5R8Rj2MtnvG"
ACCESS_TOKEN_SECRET = "8mJhB0QPi9TrlE92VA5OofryyarMxYRVt5CW6ikohO52L"
# =====================================================================

def generate_market_tweet() -> str:
    """
    Genera un tweet quantitativo basato su metriche simulative.
    Versione Stealth Anti-Spam (Niente hashtag per scaldare l'account in sicurezza).
    """
    assets = ["BTC", "ETH", "SOL", "XRP", "BNB", "AVAX", "LINK"]
    directions = [
        "Accumulation phase detected via on-chain flow analysis.",
        "Liquidity sweep at major support node confirmed.",
        "Algorithmic breakout sequence initiated. Variance expanding.",
        "Institutional outflow spiking. Proceed with strict risk sizing.",
        "Volatility contraction suggests imminent macro expansion.",
        "Dark pool block trades detected. Smart money positioning.",
        "Order block mitigation complete. Anticipating reversal."
    ]
    
    asset = random.choice(assets)
    direction = random.choice(directions)
    
    # Testo istituzionale e pulito
    tweet = f"Market Update: {asset}\n\n{direction}\n\nData feed: Market Insider Pro Quant System."
    
    return tweet

def post_tweet(live_mode: bool = False):
    """Gestisce la pubblicazione del tweet tramite le API v2 di X."""
    tweet_text = generate_market_tweet()
    
    if not live_mode:
        logging.info("SIMULATION MODE ACTIVE. Tweet generated but not sent to X:")
        print("\n--------------------------------------------------")
        print(tweet_text)
        print("--------------------------------------------------\n")
        return

    try:
        logging.info("Establishing secure connection to X API v2...")
        
        # Autenticazione corretta per la pubblicazione in v2 (OAuth 1.0a User Context)
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        
        # Invio effettivo
        response = client.create_tweet(text=tweet_text)
        
        logging.info(f"Tweet successfully posted! ID: {response.data['id']}")
        print(f"\n✅ TWEET LIVE: https://x.com/user/status/{response.data['id']}\n")

    except tweepy.TweepyException as e:
        logging.error(f"API Execution failed: {e}")
    except Exception as ex:
        logging.error(f"Unexpected error: {ex}")

def start_automation_loop(hours: int, live_mode: bool = False):
    """Avvia il loop infinito di pubblicazione."""
    seconds = hours * 3600
    logging.info(f"Avvio Automazione: Pubblicazione ogni {hours} ore. (Live Mode: {live_mode})")
    
    while True:
        post_tweet(live_mode=live_mode)
        logging.info(f"Standby per {hours} ore... Il bot sta riposando.")
        time.sleep(seconds)

if __name__ == "__main__":
    print("=========================================================")
    print("🤖 MARKET INSIDER PRO - SOCIAL AUTOMATION ENGINE (X)     ")
    print("=========================================================")
    
    # RUN_LIVE = True accende i motori e pubblica sul profilo
    RUN_LIVE = True
    
    # Avvia il loop ogni 4 ore
    start_automation_loop(hours=4, live_mode=RUN_LIVE)