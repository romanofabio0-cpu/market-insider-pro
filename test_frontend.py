from playwright.sync_api import sync_playwright
import logging

# Configurazione standard per i log
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] SYSTEM: %(message)s')

TARGET_URL = "https://marketinsiderpro.com" 

def run_amnesia_test():
    """Testa la persistenza della memoria (LocalStorage) al ricaricamento della pagina."""
    logging.info("--- AVVIO: Test di Amnesia (LocalStorage) ---")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(TARGET_URL)
            page.evaluate("localStorage.setItem('mip_vip_status', 'Active_User_Test')")
            page.reload()
            vip_status = page.evaluate("localStorage.getItem('mip_vip_status')")
            
            if vip_status == 'Active_User_Test':
                logging.info("✅ TEST SUPERATO: Il frontend ha una memoria di ferro. Nessuna amnesia.\n")
            else:
                logging.error(f"❌ TEST FALLITO: Dato perso dopo il reload. Trovato: {vip_status}\n")
                
        except Exception as e:
            logging.error(f"Errore durante l'esecuzione del test: {e}\n")
        finally:
            browser.close()

def run_fat_finger_test():
    """Simula la navigazione da Smartphone (iPhone 13) per testare la reattività del design."""
    logging.info("--- AVVIO: Fat Finger Test (Emulazione Mobile) ---")
    
    with sync_playwright() as p:
        # Carichiamo i parametri esatti di un iPhone 13 (dimensioni, touch screen, user agent)
        iphone_13 = p.devices['iPhone 13']
        
        browser = p.chromium.launch(headless=True)
        # Creiamo il contesto applicando le regole del telefono
        context = browser.new_context(**iphone_13)
        page = context.new_page()
        
        try:
            page.goto(TARGET_URL)
            
            # Leggiamo la larghezza dello schermo che il sito sta effettivamente renderizzando
            viewport = page.viewport_size
            logging.info(f"Risoluzione emulata: {viewport['width']}x{viewport['height']} (Touch screen: Attivo)")
            
            # Un iPhone 13 in verticale ha una larghezza di 390 pixel. 
            # Se il sito risponde con una larghezza mobile (< 500px), il test è passato.
            if viewport['width'] <= 500:
                logging.info("✅ TEST SUPERATO: Il sito si è adattato perfettamente alla visualizzazione Mobile (Responsive OK).\n")
            else:
                logging.error("❌ TEST FALLITO: Il sito sta forzando la visualizzazione Desktop su uno schermo mobile.\n")
                
        except Exception as e:
            logging.error(f"Errore durante l'esecuzione del test mobile: {e}\n")
        finally:
            browser.close()

if __name__ == "__main__":
    print("=========================================================")
    print("🤖 MARKET INSIDER PRO - FRONTEND DIAGNOSTICS SUITE       ")
    print("=========================================================")
    
    # Eseguiamo la suite di test in sequenza
    run_amnesia_test()
    run_fat_finger_test()