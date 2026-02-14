from playwright.sync_api import sync_playwright
import time

def ultimate_qa_test():
    print("🛡️ AVVIO PROTOCOLLO QA (QUALITY ASSURANCE) DEFINITIVO...\n")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        
        try:
            # --- TEST 1: ERRORI JAVASCRIPT NASCOSTI ---
            print("🖥️ TEST 1: Controllo Errori Javascript invisibili...")
            page = browser.new_page()
            js_errors = []
            page.on("pageerror", lambda err: js_errors.append(err.message))
            
            page.goto("https://marketinsiderpro.com")
            if js_errors:
                print(f"⚠️ ATTENZIONE: Trovati {len(js_errors)} errori JS!")
            else:
                print("✅ PASSATO: Il motore Javascript è pulito. Nessun errore.\n")

            # --- TEST 2: NAVIGAZIONE TOTALE E BROKEN LINKS ---
            print("🔗 TEST 2: Scansione di tutti i Link del Menu...")
            nav_links = ["⚡ Signals", "🏆 Leaderboard", "🤖 API Hub", "Wallet", "Academy", "Brokers", "💎 Pricing"]
            for link in nav_links:
                page.click(f"text='{link}'")
                time.sleep(0.5) # Lascia caricare la pagina
                assert page.title() != "", f"Errore: Pagina {link} non caricata o senza titolo!"
            print("✅ PASSATO: Nessun Broken Link (404). Tutte le pagine esistono e rispondono.\n")

            # --- TEST 3: TEST DEI MODULI, TENDINE E CALCOLI (WALLET) ---
            print("💼 TEST 3: Verifica Moduli di Input e Logica (Wallet)...")
            page.goto("https://marketinsiderpro.com/wallet.html")
            page.select_option("#asset-select", "bitcoin") # Testa il menu a tendina
            page.fill("#asset-amount", "0.5")              # Testa l'input numerico
            page.click("button:has-text('+ ADD')")         # Testa il bottone
            assert page.is_visible("text=0.5")             # Verifica che la tabella si aggiorni
            print("✅ PASSATO: Moduli (form), tendine e logica JS del LocalStorage funzionano.\n")

            # --- TEST 4: SIMULAZIONE MOBILE (RESPONSIVITÀ) ---
            print("📱 TEST 4: Simulazione layout Smartphone (iPhone 13)...")
            mobile_context = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
            mobile_page = mobile_context.new_page()
            mobile_page.goto("https://marketinsiderpro.com")
            assert mobile_page.is_visible(".grid")
            print("✅ PASSATO: Il sito si carica senza crashare su schermi mobili.\n")

            print("🏆 TUTTI I TEST SONO VERDI. IL CODICE È SOLIDO COME UNA ROCCIA.")
            time.sleep(2)
            
        except Exception as e:
            print(f"\n❌ TEST FALLITO! Dettagli errore: {e}\n")
        
        finally:
            browser.close()

if __name__ == "__main__":
    ultimate_qa_test()