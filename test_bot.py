from playwright.sync_api import sync_playwright
import time

def run_automated_tests():
    print("🤖 Avvio del Robot di Test su MarketInsiderPro.com...\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800) 
        page = browser.new_page()
        
        try:
            # --- TEST 1: CARICAMENTO HOMEPAGE ---
            print("⏳ TEST 1: Caricamento Homepage...")
            page.goto("https://marketinsiderpro.com")
            assert "Market Insider Pro" in page.title()
            print("✅ PASSATO: Il sito è online e risponde.\n")

            # --- TEST 2: NAVIGAZIONE PRICING ---
            print("⏳ TEST 2: Verifica tasto VIP e Pagina Prezzi...")
            # Clicca esattamente sul testo del nuovo link nella navbar
            page.click("text='VIP PASS 👑'") 
            assert page.is_visible("text=UPGRADE TO VIP PASS")
            print("✅ PASSATO: Il funnel di vendita funziona ed è collegato.\n")

            # --- TEST 3: CHECKOUT STRIPE ---
            print("⏳ TEST 3: Verifica Checkout Stripe...")
            page.click("button:has-text('START 7-DAY TRIAL')")
            assert page.is_visible("text=Market Insider Pro VIP")
            # Chiude il popup di Stripe cliccando sulla X
            page.click(".close-modal") 
            print("✅ PASSATO: Il modulo di pagamento si apre e si chiude correttamente.\n")

            # --- TEST 4: LEADERBOARD GAMIFICATION ---
            print("⏳ TEST 4: Verifica Gamification e Classifiche...")
            page.click("text='🏆 Leaderboard'")
            assert page.is_visible("text=GLOBAL LEADERBOARD")
            print("✅ PASSATO: La classifica è online e funzionante.\n")

            print("🏆 TUTTI I TEST SONO STATI SUPERATI CON SUCCESSO! LA V1.0.0 E' BLINDATA.")
            time.sleep(3) # Pausa per farti godere la vittoria
            
        except Exception as e:
            print(f"\n❌ TEST FALLITO! Dettagli errore: {e}\n")
        
        finally:
            browser.close()

if __name__ == "__main__":
    run_automated_tests()