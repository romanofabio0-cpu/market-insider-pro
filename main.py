import pandas as pd
import os
import datetime
import random
import yfinance as yf

# --- CONFIGURAZIONE PROPRIETARIA ---
NOME_SITO = "Market Insider Pro"
AUTORE = "Market Insider Inc."
CHAT_EMBED_URL = "https://minnit.chat/MarketInsiderGlobal?embed&nickname="
LINK_DEMO = "https://www.etoro.com/demo"

OUTPUT_FOLDER = "sito_generato"
if not os.path.exists(OUTPUT_FOLDER): os.makedirs(OUTPUT_FOLDER)

# --- DATABASE INTEGRATO (Niente più file CSV esterni) ---
# Qui puoi aggiungere o togliere asset direttamente.
DATI_ASSET = [
    {"nome": "Bitcoin", "symbol": "BTC-USD", "cat": "Crypto"},
    {"nome": "Ethereum", "symbol": "ETH-USD", "cat": "Crypto"},
    {"nome": "Solana", "symbol": "SOL-USD", "cat": "Crypto"},
    {"nome": "Ripple (XRP)", "symbol": "XRP-USD", "cat": "Crypto"},
    {"nome": "NVIDIA", "symbol": "NVDA", "cat": "Stock"},
    {"nome": "Tesla", "symbol": "TSLA", "cat": "Stock"},
    {"nome": "Apple", "symbol": "AAPL", "cat": "Stock"},
    {"nome": "Amazon", "symbol": "AMZN", "cat": "Stock"},
    {"nome": "Meta", "symbol": "META", "cat": "Stock"},
    {"nome": "Microsoft", "symbol": "MSFT", "cat": "Stock"},
    {"nome": "Gold", "symbol": "GC=F", "cat": "Commodity"},
    {"nome": "Silver", "symbol": "SI=F", "cat": "Commodity"},
    {"nome": "Oil (WTI)", "symbol": "CL=F", "cat": "Commodity"},
    {"nome": "Euro/USD", "symbol": "EURUSD=X", "cat": "Forex"}
]

# --- DATI TRACKER & ACADEMY ---
INSIDER_MOVES = [
    {"nome": "Nancy P.", "asset": "NVIDIA", "azione": "BUY 🟢", "valore": "$1.2M", "data": "2gg fa"},
    {"nome": "Mark Z.", "asset": "META", "azione": "SELL 🔴", "valore": "$15M", "data": "Ieri"},
    {"nome": "Warren B.", "asset": "APPLE", "azione": "SELL 🔴", "valore": "$50M", "data": "Oggi"}
]

LEZIONI = [
    {"slug": "lezione_1", "titolo": "Lezione 1: Candele", "desc": "Impara a leggere i grafici.", "html": "<h3>Candele Giapponesi</h3><p>Il verde sale, il rosso scende...</p>"},
    {"slug": "lezione_2", "titolo": "Lezione 2: RSI", "desc": "Trova i punti di inversione.", "html": "<h3>L'indicatore RSI</h3><p>Sopra 70 vendi, sotto 30 compra...</p>"}
]

print("🚀 AVVIO SISTEMA (Database Integrato)...")
df = pd.DataFrame(DATI_ASSET)

# --- CSS DEFINITIVO ---
css_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;500;700;800&display=swap');
    body { font-family: 'Manrope', sans-serif; background: #09090b; color: #eee; margin:0; padding:0; line-height:1.6; }
    a { text-decoration: none; color: inherit; transition:0.2s; }
    .container { max-width: 1100px; margin: 0 auto; padding: 20px; }
    
    header { background: #111; padding: 20px; text-align: center; border-bottom: 1px solid #222; position:sticky; top:0; z-index:100; backdrop-filter:blur(10px); }
    .nav { display: flex; justify-content: center; gap: 20px; margin-top: 10px; font-weight: bold; }
    .nav a:hover { color: #007aff; }

    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }
    .card { background: #161616; padding: 20px; border-radius: 12px; border: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }
    .card:hover { border-color: #007aff; cursor: pointer; transform: translateY(-2px); background: #1a1a1a; }
    
    .badge { padding: 5px 10px; border-radius: 4px; font-size: 0.7em; font-weight: bold; text-transform: uppercase; }
    .bull { background: rgba(52, 199, 89, 0.2); color: #34c759; border:1px solid #34c759; }
    .bear { background: rgba(255, 59, 48, 0.2); color: #ff3b30; border:1px solid #ff3b30; }
    .whale { background: linear-gradient(90deg, #bd00ff, #4b0082); color: white; animation: pulse 2s infinite; }
    
    table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #111; border-radius: 8px; overflow: hidden; }
    td, th { padding: 12px; text-align: left; border-bottom: 1px solid #222; }
    .chat-box { height: 75vh; border: 1px solid #333; border-radius: 12px; overflow: hidden; background:black; }
    
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(189,0,255,0.7); } 100% { box-shadow: 0 0 0 10px rgba(189,0,255,0); } }
</style>
"""

html_header = f"""
<header>
    <h1>{NOME_SITO}</h1>
    <div class="nav">
        <a href="index.html">DASHBOARD</a>
        <a href="chat.html" style="color:#34c759">SECRET CHAT 💬</a>
        <a href="academy.html">ACADEMY 🎓</a>
    </div>
</header>
"""

# --- MOTORE DI ANALISI ---
def analizza_asset(symbol):
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1mo")
        if len(hist) < 2: return '<span class="badge">LOADING...</span>', "---"
        
        current = hist['Close'].iloc[-1]
        prev = hist['Close'].iloc[-2]
        vol = hist['Volume'].iloc[-1]
        avg_vol = hist['Volume'].mean()
        
        # Logica Bull/Bear
        badge = '<span class="badge bull">BULLISH 🟢</span>' if current > prev else '<span class="badge bear">BEARISH 🔴</span>'
        
        # Logica Whale
        if vol > avg_vol * 1.5: badge += ' <span class="badge whale">WHALE 🐳</span>'
        
        return badge, f"${current:,.2f}"
    except:
        return '<span class="badge">WAITING...</span>', "---"

# --- GENERAZIONE PAGINE ---
lista_html = ""
for index, row in df.iterrows():
    nome = row['nome']
    sym = row['symbol']
    badge, prezzo = analizza_asset(sym)
    
    # Pagina Singola Asset
    file_asset = f"{sym.replace('=','').replace('^','')}.html"
    tv_sym = sym.replace("-USD", "USD").replace("=F", "").replace("=X", "")
    if "BTC" in sym: tv_sym = "BINANCE:BTCUSDT"
    
    html_dettaglio = f"""<!DOCTYPE html><html><head><title>{nome}</title>{css_style}</head><body>{html_header}
    <div class="container">
        <h2>{nome} <span style="color:#666">{sym}</span></h2>
        <div style="font-size:2em; font-weight:bold; margin-bottom:20px;">{prezzo} {badge}</div>
        <div class="tradingview-widget-container" style="height:500px">
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>{{ "autosize": true, "symbol": "{tv_sym}", "theme": "dark", "interval": "D" }}</script>
        </div>
        <br><a href="index.html">← Dashboard</a>
    </div></body></html>"""
    with open(os.path.join(OUTPUT_FOLDER, file_asset), "w", encoding="utf-8") as f: f.write(html_dettaglio)
    
    # Card Home Page
    lista_html += f'<a href="{file_asset}" class="card"><div><strong>{nome}</strong><br><small style="color:#666">{sym}</small></div><div>{badge}</div></a>'

# PAGINA INDEX
rows_insider = ""
for m in INSIDER_MOVES:
    rows_insider += f"<tr><td>{m['nome']}</td><td>{m['asset']}</td><td>{m['azione']}</td><td>{m['valore']}</td></tr>"

html_index = f"""<!DOCTYPE html><html><head><title>{NOME_SITO}</title>{css_style}</head><body>{html_header}
<div class="container">
    <div class="tradingview-widget-container"><script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>{{ "symbols": [ {{ "proName": "BINANCE:BTCUSDT", "title": "Bitcoin" }}, {{ "proName": "NASDAQ:NVDA", "title": "NVIDIA" }} ], "colorTheme": "dark", "displayMode": "adaptive" }}</script></div>
    
    <h3>🔥 Market Scanner (AI Live)</h3>
    <div class="grid">{lista_html}</div>
    
    <div style="margin-top:40px;">
        <h3>🏛️ Insider Tracker</h3>
        <table><tr><th>Chi</th><th>Asset</th><th>Azione</th><th>Valore</th></tr>{rows_insider}</table>
    </div>
</div></body></html>"""
with open(os.path.join(OUTPUT_FOLDER, "index.html"), "w", encoding="utf-8") as f: f.write(html_index)

# PAGINA ACADEMY & CHAT
html_academy = f"""<!DOCTYPE html><html><head><title>Academy</title>{css_style}</head><body>{html_header}<div class="container"><h1>Academy</h1><p>Coming Soon...</p></div></body></html>"""
with open(os.path.join(OUTPUT_FOLDER, "academy.html"), "w", encoding="utf-8") as f: f.write(html_academy)

html_chat = f"""<!DOCTYPE html><html><head><title>Chat</title>{css_style}</head><body>{html_header}<div class="container"><div class="chat-box"><iframe src="{CHAT_EMBED_URL}" style="width:100%; height:100%; border:none;"></iframe></div></div></body></html>"""
with open(os.path.join(OUTPUT_FOLDER, "chat.html"), "w", encoding="utf-8") as f: f.write(html_chat)

print("✅ SITO GENERATO! Pronto per GitHub.")