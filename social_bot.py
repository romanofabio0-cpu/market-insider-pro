import os
import tweepy
import logging
import random
import time

# =====================================================================
# CONFIGURAZIONE LOGGING (Standard CI/CD)
# =====================================================================
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] SYSTEM: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# =====================================================================
# 🔑 CREDENZIALI API DI X (TWITTER) - BLINDATE CLOUD MODE
# =====================================================================
# Le chiavi ora vengono "pescate" automaticamente dalle variabili di sistema
# (GitHub Secrets) per evitare che vengano rubate se il codice diventa pubblico.
API_KEY = os.environ.get("TWITTER_API_KEY", "")
API_SECRET = os.environ.get("TWITTER_API_SECRET", "")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN", "")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_SECRET", "")
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

if __name__ == "__main__":
    print("=========================================================")
    print("🤖 MARKET INSIDER PRO - SOCIAL AUTOMATION ENGINE (X)     ")
    print("=========================================================")
    
    # RUN_LIVE = True accende i motori e pubblica sul profilo
    RUN_LIVE = True
    
    # Esecuzione CLOUD: Singolo invio controllato da GitHub Actions
    logging.info("Avvio pubblicazione (Cloud Mode)...")
    post_tweet(live_mode=RUN_LIVE)
    logging.info("Operazione completata con successo. Motori spenti.")