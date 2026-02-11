import os
from core.config import OUTPUT_FOLDER, get_logger
from modules.data_engine import scarica_crypto_live, genera_dataset_completo, genera_smart_money, genera_calendario_macro
from modules.builder import build_index, build_chart_pages, build_academy, build_chat

logger = get_logger("Main")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    logger.info("🚀 AVVIO MARKET INSIDER PRO (MODULAR BUILD)...")
    
    # 1. Recupero Dati
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    smart_data = genera_smart_money()
    calendar = genera_calendario_macro()
    
    # 2. Costruzione Sito
    build_index(assets, smart_data, calendar)
    build_chart_pages(assets)
    build_academy()
    build_chat()
    
    logger.info(f"✅ SITO GENERATO CON SUCCESSO IN: {OUTPUT_FOLDER}")
    print("Premi ENTER per chiudere...")

if __name__ == "__main__":
    main()


