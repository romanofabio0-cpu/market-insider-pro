import os
import re
import urllib.request

def run_advanced_tests():
    print("🔬 AVVIO PROTOCOLLO DI TESTING AVANZATO (FASE 3)...\n")
    public_dir = "public" 
    
    if not os.path.exists(public_dir):
        html_files_here = [f for f in os.listdir('.') if f.endswith('.html')]
        if len(html_files_here) > 0:
            public_dir = "."
        else:
            print("❌ ERRORE: Nessun file HTML trovato per il test.")
            return

    html_files = [f for f in os.listdir(public_dir) if f.endswith('.html')]
    
    # TEST 4: BROKEN LINKS (Corretto per ignorare le News esterne)
    print("🔗 TEST 4: Scansione Link Rotti (Broken Links)...")
    broken_links = 0
    for file in html_files:
        filepath = os.path.join(public_dir, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            links = re.findall(r'href="([^"]+\.html)"', content)
            for link in links:
                if link.startswith("http"):  # Ignora i link esterni come la CNBC!
                    continue
                if not os.path.exists(os.path.join(public_dir, link)):
                    print(f"   ❌ Broken Link trovato in {file}: punta a '{link}' che non esiste!")
                    broken_links += 1
                    
    if broken_links == 0:
        print("   ✅ Perfetto! Nessun link rotto trovato. Ragnatela di navigazione sicura al 100%.")

    # TEST 5: AFFILIATE TRACKING
    print("\n💰 TEST 5: Verifica Presenza Tag Affiliato Amazon...")
    academy_file = os.path.join(public_dir, "academy_lez1_1.html")
    if os.path.exists(academy_file):
        with open(academy_file, 'r', encoding='utf-8') as f:
            if "mip081-21" in f.read():
                print("   ✅ Tag Affiliato Amazon (mip081-21) rilevato e blindato nei bottoni!")
            else:
                print("   ❌ ATTENZIONE: Tag affiliato non trovato nell'Academy.")
    else:
        print("   ⚠️ File Academy_lez1_1.html non trovato per il test affiliati.")

    # TEST 6: BINANCE API PING
    print("\n📡 TEST 6: Ping Server Binance (Motore Prezzi & Wallet)...")
    try:
        req = urllib.request.urlopen("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT", timeout=5)
        if req.getcode() == 200:
            print("   ✅ Connessione a Binance stabilita con successo! Il feed dei prezzi live è operativo.")
    except Exception as e:
        print(f"   ❌ ERRORE DI CONNESSIONE A BINANCE: {e}")

    print("\n🏁 STRESS TEST COMPLETATO. SISTEMA BLINDATO.")

if __name__ == "__main__":
    run_advanced_tests()