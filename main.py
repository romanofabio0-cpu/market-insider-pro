import os
from core.config import OUTPUT_FOLDER, get_logger
from modules.data_engine import scarica_crypto_live, genera_dataset_completo, genera_calendario_macro, scarica_fear_greed
from modules.news_engine import scarica_news
# Importiamo la nuova funzione build_referral_page
from modules.builder import build_index, build_chart_pages, build_academy, build_chat, build_wallet, build_signals_page, build_brokers_page, build_api_hub, build_referral_page

logger = get_logger("Main")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    logger.info("🚀 AVVIO MARKET INSIDER PRO (FASE 6: RITENZIONE E CRESCITA)...")
    
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    fng_data = scarica_fear_greed() 
    
    news = scarica_news() 
    calendar = genera_calendario_macro()
    
    build_index(assets, news, calendar, fng_data) 
    build_signals_page(assets)
    build_api_hub()            
    build_brokers_page()       
    build_referral_page()     # 🔥 COSTRUISCE LA PAGINA INVITA E GUADAGNA
    build_chart_pages(assets)
    build_academy()
    build_chat()
    build_wallet() 
    
    logger.info(f"✅ SITO COMPLETO AGGIORNATO IN: {OUTPUT_FOLDER}")
    print("Premi ENTER per chiudere...")

if __name__ == "__main__":
    main()