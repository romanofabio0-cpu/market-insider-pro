import os
from core.config import OUTPUT_FOLDER, get_logger
# Aggiunto 'genera_smart_money' per estrarre i dati dei miliardari e bloccarli dietro il VIP PASS
from modules.data_engine import scarica_crypto_live, genera_dataset_completo, genera_calendario_macro, scarica_fear_greed, genera_smart_money
from modules.news_engine import scarica_news
from modules.builder import build_index, build_academy, build_chat, build_wallet, build_signals_page, build_brokers_page, build_api_hub, build_referral_page, build_pricing_page, build_leaderboard_page, build_legal_page, build_success_page, build_vip_lounge, build_stories_page, build_tools_page, build_seo_files

logger = get_logger("Main")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    # Cambio della versione per segnare la transizione ad asset a rendita passiva
    logger.info("🚀 AVVIO MARKET INSIDER PRO (PRODUCTION V1.5.0 - MONETIZATION EDITION)...")
    
    # --- 1. MOTORE DATI (Estrazione Valore) ---
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    fng_data = scarica_fear_greed() 
    
    news = scarica_news() 
    calendar = genera_calendario_macro()
    
    # Estrazione dei flussi istituzionali (L'esca per gli abbonamenti VIP)
    smart_money = genera_smart_money() 
    
    # --- 2. MOTORE DI RENDER (Costruzione Pagine e Funnels) ---
    # Passiamo 'smart_money' all'index per renderizzare la tabella VIP
    build_index(assets, news, calendar, fng_data, smart_money) 
    
    build_signals_page(assets)
    build_api_hub()            
    build_brokers_page()       
    build_referral_page()     
    build_pricing_page()      
    build_leaderboard_page()  
    build_legal_page()        
    build_academy()
    build_chat()
    build_wallet() 
    build_success_page() 
    build_vip_lounge() 
    build_stories_page()
    build_tools_page()
    
    # --- 3. INFRASTRUTTURA SEO ---
    build_seo_files()
    
    logger.info(f"✅ SITO COMPLETO AGGIORNATO E BLINDATO IN: {OUTPUT_FOLDER}")

if __name__ == "__main__":
    main()