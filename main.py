import os
from core.config import OUTPUT_FOLDER, get_logger
from modules.data_engine import scarica_crypto_live, genera_dataset_completo, genera_calendario_macro, scarica_fear_greed
from modules.news_engine import scarica_news
from modules.builder import build_index, build_chart_pages, build_academy, build_chat, build_wallet, build_signals_page, build_brokers_page

logger = get_logger("Main")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    logger.info("🚀 AVVIO MARKET INSIDER PRO (FASE 4: PRO TERMINAL)...")
    
    # 1. Dati di Mercato e Sentiment
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    
    # 🔥 ECCO IL PEZZO CHE MANCAVA: Scarichiamo il Fear & Greed
    fng_data = scarica_fear_greed() 
    
    # 2. News & Macro
    news = scarica_news() 
    calendar = genera_calendario_macro()
    
    # 3. Costruzione Sito
    build_index(assets, news, calendar, fng_data) # 👈 Ora passiamo fng_data alla Home!
    build_signals_page(assets)
    build_brokers_page()       
    build_chart_pages(assets)
    build_academy()
    build_chat()
    
    # Gestione sicura del wallet se esiste
    try:
        build_wallet() 
    except NameError:
        logger.warning("Wallet function not found, skipping...")
    
    logger.info(f"✅ SITO COMPLETO AGGIORNATO IN: {OUTPUT_FOLDER}")
    print("Premi ENTER per chiudere...")

if __name__ == "__main__":
    main()