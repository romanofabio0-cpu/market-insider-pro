import os

# --- DEFINIZIONE ARCHITETTURA MODULARE (FIXED) ---

def create_file(path, content):
    # FIX: Crea la cartella solo se il file non è nella root (come main.py)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
        
    # FIX: Scrittura in UTF-8 forzata per evitare errori di encoding su Windows
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Creato: {path}")

# ==========================================
# 1. CORE/CONFIG.PY
# ==========================================
code_config = r"""import os
import logging
import sys

# Configurazione Percorsi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "public")

# Configurazione Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)

def get_logger(name):
    return logging.getLogger(name)

# Fix Encoding Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
"""

# ==========================================
# 2. CORE/STYLES.PY
# ==========================================
# Usiamo r''' per evitare conflitti con le virgolette doppie del CSS
code_styles = r'''
"""
Modulo contenente lo stile CSS dell'applicazione.
"""

CSS_CORE = """
<style>
    :root { --bg: #050505; --card: #111; --border: #222; --accent: #2962FF; --text: #e0e0e0; --green: #00e676; --red: #ff1744; --yellow: #FFD700; }
    body { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; }
    a { text-decoration: none; color: inherit; transition: 0.2s; }
    
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
    
    header { background: rgba(10,10,10,0.95); border-bottom: 1px solid var(--border); padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(10px); }
    .logo { font-size: 1.8rem; font-weight: 800; letter-spacing: -1px; color: #fff; }
    .logo span { color: var(--accent); }
    .nav { display: flex; gap: 25px; align-items: center; }
    .nav a { font-weight: 600; font-size: 0.9rem; color: #888; text-transform: uppercase; padding: 5px 10px; border-radius: 4px; }
    .nav a:hover, .nav a.active { color: #fff; background: rgba(255,255,255,0.05); }
    .vip-btn { background: linear-gradient(45deg, #FFD700, #FFA500); color: #000 !important; font-weight: bold; padding: 8px 20px !important; border-radius: 20px; box-shadow: 0 0 15px rgba(255, 215, 0, 0.3); animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.4); } 70% { box-shadow: 0 0 0 10px rgba(255, 215, 0, 0); } 100% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); } }

    .container { max-width: 1600px; margin: 0 auto; padding: 40px 20px; }
    h2.section-title { font-size: 1.5rem; border-left: 5px solid var(--accent); padding-left: 20px; margin: 50px 0 30px 0; color: #fff; display: flex; align-items: center; gap: 10px; }
    
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }
    .card-link { display: block; }
    .card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 20px; position: relative; transition: all 0.2s; }
    .card:hover { transform: translateY(-3px); border-color: var(--accent); z-index: 10; box-shadow: 0 5px 20px rgba(0,0,0,0.5); }
    .card-head { display: flex; justify-content: space-between; margin-bottom: 10px; }
    .symbol { font-weight: 800; color: #fff; font-size: 1.1rem; }
    .name { font-size: 0.8rem; color: #666; }
    .price { font-size: 1.4rem; font-weight: 700; color: #fff; }
    .change { font-weight: bold; font-size: 0.9rem; }
    .signal-box { margin-top: 15px; padding-top: 10px; border-top: 1px solid #222; font-size: 0.75rem; color: #888; display: flex; justify-content: space-between; }
    .green { color: var(--green); } .red { color: var(--red); } .grey { color: #888; }

    .split-layout { display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-top: 40px; }
    .table-wrapper { background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; height: fit-content; }
    table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    th { background: #151515; padding: 15px; text-align: left; color: #666; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; border-bottom: 1px solid var(--border); }
    td { padding: 12px 15px; border-bottom: 1px solid #222; color: #ccc; }
    tr:hover td { background: #1a1a1a; }
    .tag { padding: 3px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }
    .tag-buy { background: rgba(0, 230, 118, 0.1); color: var(--green); border: 1px solid rgba(0, 230, 118, 0.2); }
    .tag-sell { background: rgba(255, 23, 68, 0.1); color: var(--red); border: 1px solid rgba(255, 23, 68, 0.2); }
    .blur-row td { filter: blur(4px); user-select: none; opacity: 0.5; }
    .unlock-overlay { position: absolute; left: 50%; transform: translateX(-50%); background: #FFD700; color: #000; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.8rem; cursor: pointer; box-shadow: 0 0 10px rgba(0,0,0,0.5); }

    .academy-grid { display: grid; grid-template-columns: 300px 1fr; gap: 30px; }
    .sidebar { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; height: fit-content; }
    .module-title { color: var(--accent); font-weight: bold; margin-top: 25px; margin-bottom: 10px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid #222; padding-bottom: 5px; }
    .lesson-link { display: block; padding: 12px; border-radius: 6px; color: #888; margin-bottom: 5px; cursor: pointer; transition: 0.2s; font-size: 0.95rem; }
    .lesson-link:hover, .lesson-link.active { background: #222; color: #fff; padding-left: 18px; border-left: 3px solid var(--accent); }
    .lesson-content { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 50px; min-height: 600px; }
    .lesson-content h1 { color: #fff; font-size: 2rem; margin-top: 0; }
    .lesson-content h3 { color: var(--accent); margin-top: 30px; }
    .lesson-content p, .lesson-content li { font-size: 1.1rem; color: #ccc; margin-bottom: 15px; line-height: 1.8; }
    
    .chat-interface { max-width: 900px; margin: 0 auto; background: var(--card); border: 1px solid var(--border); border-radius: 12px; height: 75vh; display: flex; flex-direction: column; overflow: hidden; }
    .chat-history { flex: 1; padding: 30px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
    .msg { max-width: 75%; padding: 15px 20px; border-radius: 12px; font-size: 1rem; line-height: 1.5; }
    .msg-user { align-self: flex-end; background: var(--accent); color: white; border-bottom-right-radius: 2px; }
    .msg-ai { align-self: flex-start; background: #1f1f1f; color: #ddd; border-bottom-left-radius: 2px; border: 1px solid #333; }
    .chat-input-area { padding: 25px; background: #0f0f0f; border-top: 1px solid var(--border); display: flex; gap: 15px; }
    .chat-input { flex: 1; background: #1a1a1a; border: 1px solid #333; color: white; padding: 15px; border-radius: 8px; outline: none; font-size: 1rem; }
    .chat-btn { background: var(--accent); color: white; border: none; padding: 0 30px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.2s; }
    .chat-btn:hover { background: #1a4bd6; }

    footer { text-align: center; padding: 60px 20px; color: #666; font-size: 0.8rem; border-top: 1px solid var(--border); margin-top: 80px; background: #080808; }
    .legal-links a { color: #888; margin: 0 15px; }
</style>
"""
'''

# ==========================================
# 3. CORE/CONTENT.PY
# ==========================================
code_content = r"""
def get_header(active_page: str) -> str:
    return f'''
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Dashboard</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="chat.html" class="{'active' if active_page=='chat' else ''}">AI Analyst</a>
            <a href="#" class="vip-btn">GET VIP PASS 👑</a>
        </nav>
    </header>
    '''

def get_footer() -> str:
    return '''
    <footer>
        <div class="legal-links"><a href="#">Privacy Policy</a><a href="#">Terms of Service</a><a href="#">Risk Disclaimer</a></div>
        <p style="margin-top:20px;">&copy; 2026 Market Insider Pro. All trading involves risk. Past performance is not indicative of future results.</p>
    </footer>
    '''

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: FOUNDATIONS",
        "lessons": [
            {"id": "lez1_1", "title": "1.1 The Trading Mindset", "html": "<h1>The Trading Mindset</h1><p>Success in trading is 20% strategy and 80% psychology.</p>"},
            {"id": "lez1_2", "title": "1.2 Understanding Candles", "html": "<h1>Japanese Candlesticks</h1><p>Candlesticks tell the story of the battle between buyers and sellers.</p>"}
        ]
    },
    "mod2": {
        "title": "MODULE 2: TECHNICAL ANALYSIS",
        "lessons": [
            {"id": "lez2_1", "title": "2.1 Support & Resistance", "html": "<h1>Support & Resistance</h1><p>Invisible floors and ceilings of the market.</p>"},
            {"id": "lez2_2", "title": "2.2 RSI & MACD", "html": "<h1>Indicators</h1><p>RSI measures momentum.</p>"}
        ]
    },
    "mod3": {
        "title": "MODULE 3: PRO STRATEGIES",
        "lessons": [
            {"id": "lez3_1", "title": "3.1 Smart Money Concepts", "html": "<h1>Follow the Whales</h1><p>Institutional money leaves footprints.</p>"}
        ]
    }
}
"""

# ==========================================
# 4. MODULES/ANALYSIS.PY
# ==========================================
code_analysis = r"""from typing import Tuple

def analizza_segnale_tecnico(change_24h: float) -> Tuple[str, str]:
    '''
    Simula un algoritmo di analisi tecnica basato sulla volatilità.
    '''
    rsi_simulato = 50 + (change_24h * 2.5)
    
    if rsi_simulato > 75: return "STRONG BUY 🚀", "green"
    if rsi_simulato > 60: return "BUY 🟢", "green"
    if rsi_simulato < 25: return "STRONG SELL 🩸", "red"
    if rsi_simulato < 40: return "SELL 🔴", "red"
    return "NEUTRAL ⚪", "grey"
"""

# ==========================================
# 5. MODULES/DATA_ENGINE.PY
# ==========================================
code_data = r"""import urllib.request
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from core.config import get_logger
from modules.analysis import analizza_segnale_tecnico

logger = get_logger("DataEngine")

def scarica_crypto_live() -> Dict[str, Any]:
    logger.info("📡 Connessione API CoinGecko...")
    ids = "bitcoin,ethereum,binancecoin,solana,ripple,cardano,staked-ether,avalanche-2,dogecoin,polkadot,tron,chainlink,matic-network,shiba-inu,litecoin,bitcoin-cash,uniswap,stellar,monero,ethereum-classic"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MarketInsiderBot/1.0'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        logger.warning(f"⚠️ Errore API: {e}")
        return {}

def genera_dataset_completo(db_live: Dict) -> List[Dict]:
    assets = []
    # Crypto
    crypto_map = {
        "bitcoin": "BTC", "ethereum": "ETH", "binancecoin": "BNB", "solana": "SOL", "ripple": "XRP",
        "cardano": "ADA", "dogecoin": "DOGE", "polkadot": "DOT", "tron": "TRX", "chainlink": "LINK",
        "matic-network": "MATIC", "shiba-inu": "SHIB", "litecoin": "LTC", "uniswap": "UNI", "stellar": "XLM"
    }
    for cid, symbol in crypto_map.items():
        data = db_live.get(cid, {})
        price = data.get('usd', 0)
        change = data.get('usd_24h_change', 0)
        sig_txt, sig_col = analizza_segnale_tecnico(change)
        assets.append({
            "id": symbol.lower(), "type": "CRYPTO", "name": cid.title(), "symbol": symbol,
            "price": price, "change": change, "tv": f"BINANCE:{symbol}USD", "signal": sig_txt, "sig_col": sig_col
        })

    # Stocks
    stocks = [
        ("NVDA", "NVIDIA", 148.50), ("TSLA", "Tesla", 325.10), ("AAPL", "Apple", 224.00), ("MSFT", "Microsoft", 418.00),
        ("AMZN", "Amazon", 198.00), ("GOOGL", "Google", 175.00), ("META", "Meta", 592.00), ("NFLX", "Netflix", 750.00),
        ("AMD", "AMD", 160.00), ("INTC", "Intel", 22.50), ("COIN", "Coinbase", 250.00), ("MSTR", "MicroStrategy", 380.00),
        ("PLTR", "Palantir", 45.00), ("HOOD", "Robinhood", 25.00), ("PYPL", "PayPal", 78.00), ("SQ", "Block", 80.00),
        ("UBER", "Uber", 75.00), ("ABNB", "Airbnb", 130.00), ("DIS", "Disney", 95.00), ("NKE", "Nike", 85.00),
        ("JPM", "JPMorgan", 210.00), ("BAC", "Bank of America", 38.00), ("GS", "Goldman Sachs", 510.00), ("V", "Visa", 280.00),
        ("MA", "Mastercard", 490.00), ("KO", "Coca-Cola", 68.00), ("PEP", "PepsiCo", 170.00), ("MCD", "McDonald's", 290.00),
        ("WMT", "Walmart", 70.00), ("TGT", "Target", 150.00)
    ]
    for s, n, p in stocks:
        var = round(random.uniform(-4.5, 4.5), 2)
        sig_txt, sig_col = analizza_segnale_tecnico(var)
        assets.append({"id": s.lower(), "type": "STOCK", "name": n, "symbol": s, "price": p, "change": var, "tv": f"NASDAQ:{s}", "signal": sig_txt, "sig_col": sig_col})
        
    return assets

def genera_smart_money() -> List[Dict]:
    names = ["Nancy Pelosi", "BlackRock", "Warren Buffet", "Elon Musk", "Mark Zuckerberg", "Jeff Bezos", "Cathie Wood", "Michael Burry", "Whale 0x7a...", "Whale 0x9b...", "Citadel LLC", "Bridgewater", "State Street", "Vanguard", "Senator Cruz", "Rep. Crenshaw"]
    actions = ["BUY 🟢", "SELL 🔴", "ACCUMULATE 🔵", "DUMP 🔻"]
    data = []
    for i in range(25):
        asset = random.choice(["NVDA", "TSLA", "BTC", "ETH", "AAPL", "MSFT", "PLTR", "COIN"])
        val = f"${random.randint(1, 50)}.{random.randint(1, 9)}M"
        data.append({"chi": names[i % len(names)], "asset": asset, "azione": random.choice(actions), "valore": val, "data": f"{random.randint(1, 12)}h ago"})
    return data

def genera_calendario_macro() -> List[Dict]:
    oggi = datetime.now()
    eventi = [
        {"evento": "CPI Inflation Data", "impatto": "ALTO 🔴", "previsto": "2.4%", "precedente": "2.5%"},
        {"evento": "FED Rate Decision", "impatto": "CRITICO 🔥", "previsto": "4.50%", "precedente": "4.75%"},
        {"evento": "Jobless Claims", "impatto": "MEDIO 🟡", "previsto": "220K", "precedente": "218K"},
        {"evento": "GDP Growth Rate", "impatto": "ALTO 🔴", "previsto": "2.1%", "precedente": "2.0%"},
        {"evento": "NFP Payrolls", "impatto": "CRITICO 🔥", "previsto": "150K", "precedente": "142K"}
    ]
    calendario = []
    for i, ev in enumerate(eventi):
        data_ev = (oggi + timedelta(days=i*3)).strftime("%d/%m")
        ev["data"] = data_ev
        calendario.append(ev)
    return calendario
"""

# ==========================================
# 6. MODULES/BUILDER.PY
# ==========================================
# ATTENZIONE: Qui usiamo r''' per evitare che i backslash o le virgolette interne rompano tutto.
code_builder = r"""import os
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import get_header, get_footer, ACADEMY_CONTENT

logger = get_logger("Builder")

def scrivi_file(nome_file: str, contenuto: str) -> None:
    path = os.path.join(OUTPUT_FOLDER, nome_file)
    try:
        with open(path, "wb") as f:
            f.write(contenuto.encode('utf-8'))
        logger.info(f"💾 Generato: {nome_file}")
    except IOError as e:
        logger.error(f"❌ Errore scrittura {nome_file}: {e}")

def build_index(assets: List[Dict], smart_money: List[Dict], calendar: List[Dict]):
    # Grid
    grid_html = ""
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        # Usiamo triple quote single f''' per gestire le virgolette doppie dell'HTML
        grid_html += f'''
        <a href="chart_{a['id']}.html" class="card-link">
            <div class="card">
                <div class="card-head"><span class="symbol">{a['symbol']}</span><span class="name">{a['type']}</span></div>
                <div class="price">${a['price']:,}</div>
                <div class="change {color}">{sign}{a['change']}%</div>
                <div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{a['sig_col']}">{a['signal']}</strong></div>
            </div>
        </a>
        '''
    
    # Tables
    sm_rows = ""
    for i, row in enumerate(smart_money):
        is_vip = i > 6
        blur = "blur-row" if is_vip else ""
        act_cls = "tag-buy" if "BUY" in row['azione'] or "ACC" in row['azione'] else "tag-sell"
        sm_rows += f'<tr class="{blur}"><td><strong style="color:#fff">{row["chi"]}</strong></td><td>{row["asset"]}</td><td><span class="tag {act_cls}">{row["azione"]}</span></td><td>{row["valore"]}</td><td>{row["data"]}</td></tr>'
        if i == 7: sm_rows += '<tr><td colspan="5" style="position:relative; padding:0;"><div class="unlock-overlay">🔒 UPGRADE TO VIP TO SEE FULL HISTORY</div></td></tr>'

    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr><td><strong style="color:#fff">{ev["evento"]}</strong></td><td>{ev["impatto"]}</td><td>{ev["previsto"]}</td><td>{ev["precedente"]}</td><td>{ev["data"]}</td></tr>'

    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        <h2 class="section-title">GLOBAL MARKETS PULSE ({len(assets)} Live Assets) ⚡</h2>
        <div class="grid">{grid_html}</div>
        <div class="split-layout">
            <div><h2 class="section-title">🕵️‍♂️ INSIDER & WHALE TRACKER</h2><div class="table-wrapper"><table><thead><tr><th>ENTITY</th><th>ASSET</th><th>ACTION</th><th>SIZE</th><th>TIME</th></tr></thead><tbody>{sm_rows}</tbody></table></div></div>
            <div><h2 class="section-title">📅 MACRO CALENDAR</h2><div class="table-wrapper"><table><thead><tr><th>EVENT</th><th>IMPACT</th><th>FCAST</th><th>PREV</th><th>DATE</th></tr></thead><tbody>{cal_rows}</tbody></table></div></div>
        </div>
    </div>
    {get_footer()}
    </body></html>'''
    scrivi_file("index.html", html)

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        # Qui usiamo single quotes esterne e doppie interne per l'HTML
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Analysis</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888;">&larr; DASHBOARD</a>
            <h1 style="color:#fff; margin-bottom:20px;">{a['name']} ({a['symbol']}) <span style="color:var(--accent)">PRO CHART</span></h1>
            <div style="height:75vh; border:1px solid #333; border-radius:12px; overflow:hidden;">{widget}</div>
        </div>
        {get_footer()}
        </body></html>'''
        scrivi_file(f"chart_{a['id']}.html", html)

def build_academy():
    sidebar = ""
    for _, mod in ACADEMY_CONTENT.items():
        sidebar += f"<div class='module-title'>{mod['title']}</div>"
        for lez in mod['lessons']:
            # FIX CRUCIALE: Usiamo f'''...''' triplo per permettere le virgolette miste nell'HTML generato
            sidebar += f'''<div onclick="window.location.href='academy_{lez['id']}.html'" class="lesson-link">📄 {lez['title']}</div>'''
            
    for _, mod in ACADEMY_CONTENT.items():
        for lez in mod['lessons']:
            html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{lez['title']}</title>{CSS_CORE}</head><body>
            {get_header('academy')}
            <div class="container">
                <div class="academy-grid">
                    <div class="sidebar">{sidebar}</div>
                    <div class="lesson-content">
                        {lez['html']}
                        <hr style="border:0; border-top:1px solid #333; margin:50px 0;">
                        <button class="vip-btn">MARK COMPLETE</button>
                    </div>
                </div>
            </div>
            {get_footer()}
            </body></html>'''
            scrivi_file(f"academy_{lez['id']}.html", html)

def build_chat():
    js = '''<script>
    function send() {
        let i = document.getElementById('in'); let v = i.value; if(!v) return;
        let h = document.getElementById('hist');
        h.innerHTML += `<div class="msg msg-user">${v}</div>`; i.value = ''; h.scrollTop = h.scrollHeight;
        setTimeout(() => {
            let r = ["Analyzing volume profile... Bullish divergence detected.", "Market sentiment is currently FEAR.", "Institutional accumulation detected on ETH.", "Support levels holding strong."];
            h.innerHTML += `<div class="msg msg-ai">🤖 ${r[Math.floor(Math.random()*r.length)]}</div>`; h.scrollTop = h.scrollHeight;
        }, 1200);
    }
    document.getElementById('in').addEventListener("keypress", e => { if(e.key === "Enter") send(); });
    </script>'''
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>AI Analyst</title>{CSS_CORE}</head><body>
    {get_header('chat')}
    <div class="container">
        <h2 class="section-title">AI MARKET ANALYST 🤖</h2>
        <div class="chat-interface">
            <div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Hello! I am your Market Analyst.</div></div>
            <div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Ask analysis..."><button class="chat-btn" onclick="send()">ANALYZE</button></div>
        </div>
    </div>
    {js} {get_footer()}
    </body></html>'''
    scrivi_file("chat.html", html)
"""

# ==========================================
# 7. MAIN.PY
# ==========================================
code_main = r"""import os
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
"""

# --- ESECUZIONE CREAZIONE FILE ---
create_file("core/config.py", code_config)
create_file("core/styles.py", code_styles)
create_file("core/content.py", code_content)
create_file("modules/analysis.py", code_analysis)
create_file("modules/data_engine.py", code_data)
create_file("modules/builder.py", code_builder)
create_file("main.py", code_main)

print("\n🎉 ARCHITETTURA FIXATA E COMPLETATA!")
print("👉 Esegui ora: python main.py")