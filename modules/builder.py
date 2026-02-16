import os
from core.content import get_header, get_footer, MODALS_HTML

# ==========================================
# IL TUO NUOVO DATABASE ASSET (Crypto + Azioni Tradizionali)
# ==========================================
ASSETS = {
    "BTC": {"name": "Bitcoin", "symbol": "BINANCE:BTCUSDT", "type": "crypto", "has_chart": True},
    "ETH": {"name": "Ethereum", "symbol": "BINANCE:ETHUSDT", "type": "crypto", "has_chart": True},
    "SOL": {"name": "Solana", "symbol": "BINANCE:SOLUSDT", "type": "crypto", "has_chart": True},
    # FIX RNDR: Binance ha cambiato il ticker in RENDER
    "RNDR": {"name": "Render", "symbol": "BINANCE:RENDERUSDT", "type": "crypto", "has_chart": True}, 
    "PEPE": {"name": "Pepe", "symbol": "BINANCE:1000PEPEUSDT", "type": "crypto", "has_chart": True},
    "DOGE": {"name": "Dogecoin", "symbol": "BINANCE:DOGEUSDT", "type": "crypto", "has_chart": True},
    "XRP": {"name": "Ripple", "symbol": "BINANCE:XRPUSDT", "type": "crypto", "has_chart": True},
    "ADA": {"name": "Cardano", "symbol": "BINANCE:ADAUSDT", "type": "crypto", "has_chart": True},
    
    # NUOVE AZIONI (STOCKS dal NASDAQ)
    "NVDA": {"name": "Nvidia", "symbol": "NASDAQ:NVDA", "type": "stock", "has_chart": True},
    "AAPL": {"name": "Apple", "symbol": "NASDAQ:AAPL", "type": "stock", "has_chart": True},
    "TSLA": {"name": "Tesla", "symbol": "NASDAQ:TSLA", "type": "stock", "has_chart": True},
    
    # ESEMPIO ASSET ESCLUSIVO SENZA GRAFICO TRADINGVIEW
    "MIP_INDEX": {"name": "MIP Whale Index", "symbol": "NONE", "type": "index", "has_chart": False}
}

def build_pages():
    os.makedirs("public", exist_ok=True)
    
    # 1. COSTRUZIONE HOME (TERMINAL)
    home_html = get_header("home") + f'''
    <main class="container">
        <h1 style="margin-top: 10px;">GLOBAL MARKETS PULSE ⚡</h1>
        <p style="color: #888; margin-bottom: 30px;">Live institutional data. Click <span style="color:var(--gold);">★</span> to pin assets to your Custom Watchlist.</p>
        <div class="grid">
    '''
    
    for ticker, data in ASSETS.items():
        # Genera le "Carte" della Home Page
        home_html += f'''
        <div class="card" onclick="window.location.href='chart_{ticker.lower()}.html'" style="cursor:pointer; background: #111; padding: 20px; border-radius: 12px; border: 1px solid #333; transition: 0.3s;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h2 style="margin:0; font-size: 1.5rem;">{ticker}</h2>
                <span style="color:#666; font-size:0.8rem;">{data['name']} ★</span>
            </div>
            <h1 style="margin: 15px 0; font-size: 2.2rem; color: white;">$---</h1>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px;">
                <span style="color:#888; font-size:0.7rem; letter-spacing: 1px;">AI SIGNAL:</span>
                <span style="background:#222; padding:4px 10px; border-radius:4px; font-size:0.7rem; font-weight:bold; color:#aaa;">NEUTRAL ⚪</span>
            </div>
        </div>
        '''
        
        # 2. COSTRUZIONE PAGINE GRAFICI
        chart_content = ""
        if data["has_chart"]:
            # Se ha il grafico, stampa TradingView corretto
            chart_content = f'''
            <div class="tradingview-widget-container" style="height: 650px; width: 100%; margin-top:20px; border-radius: 12px; overflow: hidden;">
              <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px); width:100%;"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
              {{
              "autosize": true,
              "symbol": "{data['symbol']}",
              "interval": "D",
              "timezone": "Etc/UTC",
              "theme": "dark",
              "style": "1",
              "locale": "en",
              "enable_publishing": false,
              "backgroundColor": "#0b0e14",
              "gridColor": "#1f293d",
              "hide_top_toolbar": false,
              "hide_legend": false,
              "save_image": false,
              "container_id": "tradingview_{ticker}"
            }}
              </script>
            </div>
            '''
        else:
            # Se NON ha il grafico, mostra questo bellissimo messaggio invece dell'UFO
            chart_content = f'''
            <div style="text-align:center; padding: 120px 20px; background:#111; border-radius:12px; margin-top:30px; border:1px solid #333;">
                <h1 style="font-size:4rem; margin:0;">🔒</h1>
                <h2 style="color:#FFD700; margin-top:20px; font-size: 2rem;">Exclusive Internal Asset</h2>
                <p style="color:#aaa; font-size: 1.1rem; max-width: 600px; margin: 15px auto;">
                    Standard charts are not available for <b>{data['name']}</b>. <br>
                    Our AI is currently calculating internal liquidity metrics and dark pool volume for this specific asset.
                </p>
                <button class="vip-btn" onclick="window.history.back()" style="margin-top:30px; padding: 15px 40px;">← GO BACK</button>
            </div>
            '''

        # Assembla la pagina del singolo grafico
        chart_page = get_header("home") + f'''
        <main class="container">
            <a href="index.html" style="color:#888; text-decoration:none; display:inline-block; margin: 15px 0; font-size: 0.9rem; letter-spacing: 1px;">← BACK TO TERMINAL</a>
            <h1 style="margin:0; font-size: 2.5rem;">{data['name']} <span style="color:var(--accent);">PRO CHART</span></h1>
            {chart_content}
        </main>
        ''' + MODALS_HTML + get_footer()
        
        # Salva la pagina
        with open(f"public/chart_{ticker.lower()}.html", "w", encoding="utf-8") as f:
            f.write(chart_page)

    # Chiudi e salva la Home Page
    home_html += "</div></main>" + MODALS_HTML + get_footer()
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(home_html)
        
    print("✅ Pagine Costruite con Successo (Azioni e Crypto integrate)!")