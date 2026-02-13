import os
from core.config import OUTPUT_FOLDER, get_logger
from modules.data_engine import scarica_crypto_live, genera_dataset_completo, genera_calendario_macro
from modules.news_engine import scarica_news
# AGGIUNTO build_wallet all'import
from modules.builder import build_index, build_chart_pages, build_academy, build_chat, build_wallet

logger = get_logger("Main")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    logger.info("🚀 AVVIO MARKET INSIDER PRO (MEGA-UPDATE FASE 3)...")
    
    # 1. Dati di Mercato
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    
    # 2. News & Macro
    news = scarica_news() 
    calendar = genera_calendario_macro()
    
    # 3. Costruzione Sito
    build_index(assets, news, calendar)
    build_chart_pages(assets)
    build_academy()
    build_chat()
    build_wallet() # 🔥 COSTRUISCE LA PAGINA PORTFOLIO
    
    logger.info(f"✅ SITO COMPLETO AGGIORNATO IN: {OUTPUT_FOLDER}")
    print("Premi ENTER per chiudere...")

if __name__ == "__main__":
    main()