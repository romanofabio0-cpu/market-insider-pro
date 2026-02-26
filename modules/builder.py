import os
import json
import datetime
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import MODALS_HTML

logger = get_logger("Builder")

# =========================================================
# CABINA DI REGIA AFFILIAZIONI
# =========================================================
AMAZON_LINK_BOOK = "https://www.amazon.it/s?k=trading+in+the+zone+libro&tag=mip081-21"
AMAZON_LINK_MONITOR = "https://www.amazon.it/s?k=monitor+lg+34+pollici+ultrawide&tag=mip081-21"
AMAZON_LINK_LEDGER = "https://www.amazon.it/s?k=ledger+nano+x+wallet&tag=mip081-21"

BINANCE_AFFILIATE_LINK = "https://accounts.binance.com/register?ref=1218170181"
BYBIT_AFFILIATE_LINK = "https://www.bybit.eu/invite?ref=PXANQ70"
AFF_TRADINGVIEW = "https://it.tradingview.com/?aff_id=163720"
AFF_KOINLY = "https://koinly.io/?via=2B79173F&utm_source=affiliate"

AFF_CRYPTOQUANT = "https://cryptoquant.com/sign-up?my-friend=b5rr9oZOXoAAmBbbfECQAQ0c"
AFF_NORDVPN = "https://go.nordvpn.net/aff_c?offer_id=15&aff_id=141781&url_id=858"
AFF_MEXC_BOTS = "https://www.mexc.com/register?inviteCode=3rYPU"
AFF_MEXC = "https://promote.mexc.com/r/ha7nQSXy"
AFF_FTMO = "https://trader.ftmo.com/?affiliates=RopBUMkXRdxTzXtcUKQU"
AFF_TREZOR = "https://trezor.io/?offer_id=TUO_CODICE"
AFF_NEXO = "https://nexo.com/ref/TUO_CODICE"
AFF_GLASSNODE = "https://glassnode.com/?via=TUO_CODICE"
AFF_UDEMY_COURSE = "https://click.linksynergy.com/fs-bin/click?id=TUO_CODICE&offerid=UDEMY_TRADING_COURSE"
# =========================================================

# --- STILE DASHBOARD GLOBALE E RESPONSIVE ---
MIP_DASHBOARD_CSS = """
:root {
    --bg-sidebar: #050505;
    --bg-header: #050505;
    --bg-main: #000000;
    --border-color: #1a1a1a;
    --gold: #d4af37;
    --text-main: #f8fafc;
    --text-muted: #888;
}
body {
    margin: 0; font-family: 'Inter', system-ui, sans-serif; 
    background-color: var(--bg-main); color: var(--text-main);
    display: flex; height: 100vh; overflow: hidden;
}
.sidebar {
    width: 250px; background-color: var(--bg-sidebar); 
    border-right: 1px solid var(--border-color); display: flex; flex-direction: column; z-index: 10;
    overflow-y: auto; flex-shrink: 0;
}
.sidebar-logo {
    padding: 20px; display: flex; align-items: center; gap: 12px; 
    border-bottom: 1px solid var(--border-color);
}
.sidebar-logo img { 
    width: 38px; height: 38px; border-radius: 50%; object-fit: contain; flex-shrink: 0;
    background: #111; border: 1px solid var(--gold);
}
.sidebar-logo span {
    font-size: 1.05rem; font-weight: 800; letter-spacing: -0.5px; color: #fff;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.nav-group-title {
    padding: 20px 20px 5px 20px; font-size: 0.7rem; color: #555; 
    font-weight: bold; letter-spacing: 1px; text-transform: uppercase;
}
.nav-item {
    padding: 12px 20px; color: var(--text-muted); text-decoration: none; 
    font-weight: 500; font-size: 0.9rem; border-left: 3px solid transparent; transition: all 0.2s ease;
}
.nav-item:hover, .nav-item.active { 
    background-color: #111; color: #fff; border-left: 3px solid var(--gold); 
}
.main-wrapper { 
    flex: 1; overflow-y: auto; display: flex; flex-direction: column; background-color: var(--bg-main);
}
.top-header {
    height: 65px; background-color: var(--bg-header); border-bottom: 1px solid var(--border-color);
    display: flex; align-items: center; justify-content: space-between; padding: 0 30px;
    position: sticky; top: 0; z-index: 50; flex-shrink: 0;
}
.lang-switcher {
    background: #111; color: #fff; border: 1px solid #333; padding: 8px 12px; 
    border-radius: 4px; font-weight: 600; font-size: 0.85rem; cursor: pointer; outline: none;
    appearance: none; -webkit-appearance: none;
}
.lang-switcher:hover { border-color: var(--gold); }
.dashboard-content { padding: 30px; width: 100%; box-sizing: border-box; }

/* REGOLE STRUTTURALI (Griglie, Layout, Tabelle) */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
.split-layout { display: flex; gap: 20px; align-items: stretch; margin-bottom: 30px; }
.split-layout > .panel { flex: 1; min-width: 0; }
.table-responsive { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; border-radius: 4px; }

/* RESPONSIVE MOBILE PERFETTO */
@media (max-width: 768px) {
    body { flex-direction: column; overflow: auto; }
    .sidebar { width: 100%; height: auto; flex-direction: row; flex-wrap: nowrap; overflow-x: auto; border-right: none; border-bottom: 1px solid var(--border-color); -webkit-overflow-scrolling: touch; }
    .sidebar::-webkit-scrollbar { display: none; }
    .sidebar-logo { padding: 10px 15px; border-bottom: none; border-right: 1px solid var(--border-color); }
    .sidebar-logo span { display: none; }
    .nav-group-title { display: none; }
    .nav-item { padding: 15px 20px; border-left: none; border-bottom: 2px solid transparent; white-space: nowrap; }
    .nav-item:hover, .nav-item.active { border-left: none; border-bottom: 2px solid var(--gold); background: transparent; }
    
    .top-header { padding: 0 15px; height: 60px; }
    .dashboard-content { padding: 15px; overflow-x: hidden; }
    
    .split-layout { flex-direction: column; }
    .academy-grid { grid-template-columns: 1fr !important; }
    .wallet-form { flex-direction: column !important; }
    .wallet-form input, .wallet-form button { width: 100% !important; margin-left: 0; margin-top: 10px; }
    .market-clocks { justify-content: center; }
    .fng-value { font-size: 2rem !important; }
}
"""

def get_dashboard_layout(title: str, content: str, active_page: str = "dashboard") -> str:
    """Motore di layout unificato. Avvolge ogni pagina garantendo perfezione mobile."""
    
    sidebar_html = f"""
    <div class="sidebar">
        <div class="sidebar-logo">
            <img src="logo_mip.jpg" alt="MIP Logo" onerror="this.src='https://ui-avatars.com/api/?name=MIP&background=d4af37&color=000&rounded=true&bold=true'">
            <span>Market Insider Pro</span>
        </div>
        
        <div class="nav-group-title">Core Terminal</div>
        <a href="index.html" class="nav-item {'active' if active_page == 'dashboard' else ''}">Dashboard</a>
        <a href="academy_lez1_1.html" class="nav-item {'active' if active_page == 'academy' else ''}">The Quant Journey</a>
        <a href="tools.html" class="nav-item {'active' if active_page == 'tools' else ''}">Institutional Stack</a>
        <a href="signals.html" class="nav-item {'active' if active_page == 'signals' else ''}">Signals Engine</a>
        <a href="wallet.html" class="nav-item {'active' if active_page == 'wallet' else ''}">Portfolio Tracker</a>
        <a href="chat.html" class="nav-item {'active' if active_page == 'chat' else ''}">AI Analyst</a>
        
        <div class="nav-group-title">External Venues</div>
        <a href="{BINANCE_AFFILIATE_LINK}" target="_blank" class="nav-item">Exchange (Binance)</a>
        <a href="{BYBIT_AFFILIATE_LINK}" target="_blank" class="nav-item">Exchange (Bybit)</a>
        <a href="{AFF_TRADINGVIEW}" target="_blank" class="nav-item">TradingView Charts</a>
        
        <div class="nav-group-title">Account & Clearance</div>
        <a href="pricing.html" class="nav-item {'active' if active_page == 'pricing' else ''}" style="color: var(--gold); font-weight: 800;">&#9830; VIP PASS</a>
        <a href="vip_lounge.html" class="nav-item {'active' if active_page == 'vip' else ''}">VIP Lounge</a>
    </div>
    """
    
    header_html = """
    <div class="top-header">
        <div class="header-mobile-space">
            <span style="font-weight:bold; color:var(--text-main); font-size:1.1rem; display:none;" class="mobile-title">Market Insider Pro</span>
        </div>
        <select class="lang-switcher" onchange="console.log('Language changed to: ' + this.value)">
            <option value="en">English</option>
            <option value="it">Italiano</option>
            <option value="es">Español</option>
            <option value="fr">Français</option>
        </select>
    </div>
    """
    
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>{title} | Market Insider Pro</title>
        {CSS_CORE}
        <style>{MIP_DASHBOARD_CSS}</style>
    </head>
    <body>
        {sidebar_html}
        <div class="main-wrapper">
            {header_html}
            <div class="dashboard-content">
                {content}
            </div>
        </div>
        {MODALS_HTML}
    </body>
    </html>"""

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE I: QUANTITATIVE PSYCHOLOGY", 
        "lessons": [
            {
                "id": "lez1_1", 
                "title": "1.1 Institutional Mindset", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; font-weight:900; margin-bottom:15px;">The 1% Statistical Edge</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.7;">Retail market participants systematically lose capital due to emotional execution. At Market Insider Pro, we eliminate discretionary bias. We execute purely on quantitative probabilities.</p>
                
                <div style="margin-top:40px; padding:30px; background:#111; border-left:4px solid #FFD700; border-radius:4px;">
                    <h3 style="color:#FFD700; margin-top:0;">Mandatory Literature</h3>
                    <p style="color:#ccc; line-height:1.6;">To align with institutional standards, "Trading in the Zone" by Mark Douglas is required reading for risk management conditioning.</p>
                    <a href="{AMAZON_LINK_BOOK}" target="_blank" class="vip-btn" style="background: #FFD700; color:black; text-decoration:none; display:inline-block; margin-top:15px; font-weight:bold; letter-spacing:1px; padding: 10px 20px; border-radius:4px;">ACQUIRE RESOURCE</a>
                </div>
                '''
            }
        ]
    },
    "mod2": {
        "title": "MODULE II: TECHNICAL FRAMEWORKS", 
        "lessons": [
            {
                "id": "lez2_1", 
                "title": "2.1 Liquidity Architecture", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; font-weight:900; margin-bottom:15px;">Price Action & Volume Distribution</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.7;">Discard lagging indicators. Institutional algorithms track only raw volume nodes and liquidity sweeps.</p>
                
                <div style="margin-top:40px; padding:30px; background:#111; border-left:4px solid #555; border-radius:4px;">
                    <h3 style="color:#fff; margin-top:0;">Hardware Specifications</h3>
                    <p style="color:#ccc; line-height:1.6;">Multi-timeframe analysis requires significant screen real estate. An ultrawide display is standard protocol.</p>
                    <a href="{AMAZON_LINK_MONITOR}" target="_blank" class="btn-trade" style="background:transparent; border:1px solid #fff; color:#fff; display:inline-block; margin-top:15px; padding: 10px 20px; text-decoration:none;">HARDWARE UPGRADE</a>
                </div>
                
                <div style="margin-top:20px; padding:30px; background:#111; border-left:4px solid #FCD535; border-radius:4px;">
                    <h3 style="color:#FCD535; margin-top:0;">Execution Venue</h3>
                    <p style="color:#ccc; line-height:1.6;">Zero-slippage execution is mandatory. Connect to top-tier liquidity pools.</p>
                    <a href="{BINANCE_AFFILIATE_LINK}" target="_blank" class="vip-btn" style="background:#FCD535; color:black; text-decoration:none; display:inline-block; margin-top:15px; font-weight:bold; padding: 10px 20px; border-radius:4px;">ACCESS BINANCE POOL</a>
                </div>
                '''
            }
        ]
    },
    "mod3": {
        "title": "MODULE III: ON-CHAIN ANALYSIS", 
        "lessons": [
            {
                "id": "lez3_1", 
                "title": "3.1 Order Block Dynamics", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; font-weight:900; margin-bottom:15px;">Identifying Accumulation Nodes</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.7;">Order Blocks (OBs) represent massive capital deployment by central entities. We trace these footprints to model predictive entries.</p>
                
                <div style="margin-top:40px; padding:30px; background:#111; border-left:4px solid #00C853; border-radius:4px;">
                    <h3 style="color:#00C853; margin-top:0;">Asset Custody Protocol</h3>
                    <p style="color:#ccc; line-height:1.6;">Long-term capital must remain disconnected from network attack vectors. Cold storage is strictly enforced.</p>
                    <a href="{AMAZON_LINK_LEDGER}" target="_blank" class="vip-btn" style="background:#00C853; color:black; text-decoration:none; display:inline-block; margin-top:15px; font-weight:bold; padding: 10px 20px; border-radius:4px;">SECURE HARDWARE</a>
                </div>
                '''
            }
        ]
    },
    "mod4": {
        "title": "MODULE IV: ALGORITHMIC EXECUTION", 
        "lessons": [
            {
                "id": "lez4_1", 
                "title": "4.1 API Environment Setup", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; font-weight:900; margin-bottom:15px;">System Integration</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.7;">Connect exchange APIs to deploy systematic logic without manual intervention.</p>
                
                <div style="margin-top:40px; padding:30px; background:#111; border-left:4px solid #FF9900; border-radius:4px;">
                    <h3 style="color:#FF9900; margin-top:0;">Latency Optimization</h3>
                    <p style="color:#ccc; line-height:1.6;">High-frequency logic demands ultra-low latency. Dedicated futures accounts are recommended.</p>
                    <a href="{BYBIT_AFFILIATE_LINK}" target="_blank" class="vip-btn" style="background:#17181E; border:1px solid #FF9900; color:#FF9900; text-decoration:none; display:inline-block; margin-top:15px; font-weight:bold; padding: 10px 20px;">INITIALIZE PRO ACCOUNT</a>
                </div>
                '''
            }
        ]
    },
    "mod5": {
        "title": "MODULE V: ADVANCED DERIVATIVES", 
        "lessons": [
            {
                "id": "lez5_1", 
                "title": "5.1 Options & Hedging", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; font-weight:900; margin-bottom:15px;">Delta Neutral Strategies</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.7;">Institutions do not expose themselves to directional risk blindly. Utilizing derivatives to hedge spot portfolios is the key to surviving bear markets.</p>
                
                <div style="margin-top:40px; padding:30px; background:#111; border-left:4px solid #2962FF; border-radius:4px;">
                    <h3 style="color:#2962FF; margin-top:0;">Derivatives Platform</h3>
                    <p style="color:#ccc; line-height:1.6;">For complex hedging, deep liquidity and zero maker fees are essential to maintain margin.</p>
                    <a href="{AFF_MEXC}" target="_blank" class="vip-btn" style="background:#2962FF; color:white; text-decoration:none; display:inline-block; margin-top:15px; font-weight:bold; padding: 10px 20px; border-radius:4px;">ACCESS MEXC DERIVATIVES</a>
                </div>
                '''
            }
        ]
    }
}

ASSETS_DB = {
    "BTC": {"name": "Bitcoin", "symbol": "BINANCE:BTCUSDT", "type": "crypto", "has_chart": True},
    "ETH": {"name": "Ethereum", "symbol": "BINANCE:ETHUSDT", "type": "crypto", "has_chart": True},
    "SOL": {"name": "Solana", "symbol": "BINANCE:SOLUSDT", "type": "crypto", "has_chart": True},
    "BNB": {"name": "Binance Coin", "symbol": "BINANCE:BNBUSDT", "type": "crypto", "has_chart": True},
    "XRP": {"name": "Ripple", "symbol": "BINANCE:XRPUSDT", "type": "crypto", "has_chart": True},
    "ADA": {"name": "Cardano", "symbol": "BINANCE:ADAUSDT", "type": "crypto", "has_chart": True},
    "AVAX": {"name": "Avalanche", "symbol": "BINANCE:AVAXUSDT", "type": "crypto", "has_chart": True},
    "DOT": {"name": "Polkadot", "symbol": "BINANCE:DOTUSDT", "type": "crypto", "has_chart": True},
    "LINK": {"name": "Chainlink", "symbol": "BINANCE:LINKUSDT", "type": "crypto", "has_chart": True},
    "MATIC": {"name": "Polygon", "symbol": "BINANCE:MATICUSDT", "type": "crypto", "has_chart": True},
    "TRX": {"name": "Tron", "symbol": "BINANCE:TRXUSDT", "type": "crypto", "has_chart": True},
    "DOGE": {"name": "Dogecoin", "symbol": "BINANCE:DOGEUSDT", "type": "crypto", "has_chart": True},
    "SHIB": {"name": "Shiba Inu", "symbol": "BINANCE:SHIBUSDT", "type": "crypto", "has_chart": True},
    "PEPE": {"name": "Pepe", "symbol": "BINANCE:1000PEPEUSDT", "type": "crypto", "has_chart": True},
    "RNDR": {"name": "Render", "symbol": "BINANCE:RENDERUSDT", "type": "crypto", "has_chart": True}, 
    "LTC": {"name": "Litecoin", "symbol": "BINANCE:LTCUSDT", "type": "crypto", "has_chart": True},
    "NEAR": {"name": "NEAR Protocol", "symbol": "BINANCE:NEARUSDT", "type": "crypto", "has_chart": True},
    "UNI": {"name": "Uniswap", "symbol": "BINANCE:UNIUSDT", "type": "crypto", "has_chart": True},
    "INJ": {"name": "Injective", "symbol": "BINANCE:INJUSDT", "type": "crypto", "has_chart": True},
    "OP": {"name": "Optimism", "symbol": "BINANCE:OPUSDT", "type": "crypto", "has_chart": True},
    "SUI": {"name": "Sui Network", "symbol": "BINANCE:SUIUSDT", "type": "crypto", "has_chart": True},
    "APT": {"name": "Aptos", "symbol": "BINANCE:APTUSDT", "type": "crypto", "has_chart": True},
    "ARB": {"name": "Arbitrum", "symbol": "BINANCE:ARBUSDT", "type": "crypto", "has_chart": True},
    "FET": {"name": "Fetch.ai", "symbol": "BINANCE:FETUSDT", "type": "crypto", "has_chart": True},
    "FIL": {"name": "Filecoin", "symbol": "BINANCE:FILUSDT", "type": "crypto", "has_chart": True}
}

def scrivi_file(nome_file: str, contenuto: str) -> None:
    path = os.path.join(OUTPUT_FOLDER, nome_file)
    try:
        with open(path, "wb") as f: 
            f.write(contenuto.encode('utf-8'))
        logger.info(f"Generato: {nome_file}")
    except IOError as e: 
        logger.error(f"Errore scrittura: {e}")

def format_price(price):
    if price < 0.01: return f"${price:.6f}"
    elif price < 1: return f"${price:.4f}"
    else: return f"${price:,.2f}"

def build_index(assets: List[Dict], news: List[Dict], calendar: List[Dict], fng: Dict):
    grid_html = ""
    dyn_data = {a['symbol']: a for a in assets} 
    
    for ticker, db_info in ASSETS_DB.items():
        d_asset = dyn_data.get(ticker, {"price": 0, "change": 0, "signal": "NEUTRAL", "sig_col": "#aaa"})
        color = "green" if d_asset['change'] >= 0 else "red"
        elem_id = ticker.lower()
        
        grid_html += f'''
        <div class="card-wrapper" data-id="{elem_id}" data-type="{db_info['type']}">
            <a href="chart_{elem_id}.html" class="card-link" style="display:block; height:100%; text-decoration:none;">
                <div class="card" style="border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a; padding:15px; transition:border-color 0.2s;">
                    <div class="card-head" style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="symbol" style="font-weight:700; color:#fff; font-size:1.1rem;">{ticker}</span>
                        <span class="name" style="color:#666; font-size:0.75rem; text-transform:uppercase;">{db_info['name']}</span>
                    </div>
                    <div class="price" id="price-{elem_id}" style="font-family:monospace; font-size:1.6rem; margin-top:8px; color:#fff;">
                        {format_price(d_asset["price"])}
                    </div>
                    <div class="change {color}" id="change-{elem_id}" style="font-family:monospace; font-size:0.9rem; margin-top:4px;">
                        {("+" if d_asset["change"] >= 0 else "")}{d_asset["change"]}%
                    </div>
                    <div class="signal-box" style="border-top:1px solid #1a1a1a; padding-top:10px; margin-top:15px; display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:0.65rem; color:#555; text-transform:uppercase;">Trend Matrix</span>
                        <strong style="color:{d_asset['sig_col']}; font-size:0.75rem; background:#111; padding:2px 6px; border-radius:2px;">
                            {d_asset['signal']}
                        </strong>
                    </div>
                </div>
            </a>
        </div>
        '''
        
        chart_content = f'''
        <a href="index.html" style="color:#888; text-decoration:none; display:inline-block; margin: 15px 0; font-size: 0.8rem; letter-spacing: 1px; border:1px solid #222; padding:5px 10px; border-radius:2px;">
            BACK TO TERMINAL
        </a>
        <h1 style="margin:0 0 20px 0; font-size: 2rem; font-weight:700;">
            {db_info['name']} <span style="color:#666;">DATA</span>
        </h1>
        <div class="tradingview-widget-container" style="height:100%;width:100%; margin-top:20px; border:1px solid #222; border-radius:4px; overflow:hidden;">
            <div id="tv_{elem_id}" style="height:650px;width:100%"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({{
                "autosize": true,
                "symbol": "{db_info['symbol']}",
                "interval": "D",
                "timezone": "Etc/UTC",
                "theme": "dark",
                "style": "1",
                "locale": "en",
                "toolbar_bg": "#050505",
                "enable_publishing": false,
                "allow_symbol_change": true,
                "studies": ["RSI@tv-basicstudies", "Volume@tv-basicstudies"],
                "container_id": "tv_{elem_id}"
            }});
            </script>
        </div>
        '''
        chart_page_html = get_dashboard_layout(f"{ticker} Data", chart_content, active_page="dashboard")
        scrivi_file(f"chart_{elem_id}.html", chart_page_html)

    fng_color = "#FF3D00" if fng['value'] < 40 else ("#00C853" if fng['value'] > 60 else "#FFD700")
    fng_html = f'''
    <div class="fng-meter" style="border-radius:4px; border:1px solid #222; padding:20px; background:#0a0a0a;">
        <h3 style="margin:0; color:#888; text-transform:uppercase; font-size:0.8rem; font-weight:700;">
            MACRO SENTIMENT INDEX
        </h3>
        <div class="fng-value" style="color:{fng_color}; font-family:monospace; font-size:2.5rem; font-weight:900; margin:10px 0;">
            {fng["value"]}
        </div>
        <div style="font-weight:bold; letter-spacing:1px; color:#ccc;">
            {fng["text"]}
        </div>
        <div class="fng-bar" style="border-radius:2px; background:#111; height:8px; margin-top:15px; position:relative;">
            <div class="fng-indicator" style="position:absolute; top:0; left: {fng["value"]}%; width:4px; height:100%; background:{fng_color}; border-radius:0;"></div>
        </div>
    </div>
    '''
    
    filter_html = '''
    <div class="market-filters" style="margin-bottom: 30px; display: flex; gap: 15px; align-items:center;">
        <input type="text" id="asset-search" placeholder="Query ticker (e.g. BTC)..." onkeyup="filterAssets()" style="padding: 12px 20px; background: #0a0a0a; border: 1px solid #222; color: #fff; width: 100%; max-width: 350px; border-radius: 4px; outline:none; font-family:monospace; font-size:0.9rem;">
    </div>
    <script>
    function filterAssets() {
        let search = document.getElementById("asset-search").value.toLowerCase();
        let cards = document.querySelectorAll(".card-wrapper");
        cards.forEach(c => {
            let id = c.getAttribute("data-id");
            if (id.includes(search) || c.innerText.toLowerCase().includes(search)) { 
                c.style.display = "block"; 
            } else { 
                c.style.display = "none"; 
            }
        });
    }
    </script>
    '''
    
    news_rows = "".join([f'''
        <tr style="border-bottom: 1px solid #111;">
            <td style="padding:15px 10px;">
                <a href="{n["link"]}" target="_blank" style="font-weight:600; color:#ddd; display:block; margin-bottom:5px; text-decoration:none;">
                    {n["title"]}
                </a>
                <span style="font-size:0.7rem; color:#666; text-transform:uppercase;">SOURCE: {n["source"]}</span>
            </td>
            <td style="text-align:right;">
                <a href="{n["link"]}" target="_blank" class="btn-trade" style="background:transparent; color:#888; border:1px solid #333; padding:5px 10px; font-size:0.7rem; border-radius:2px; text-decoration:none;">
                    ACCESS
                </a>
            </td>
        </tr>
    ''' for n in news])
    
    ticker_css = '''
    <style>
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-50%, 0, 0); } } 
    .ticker-wrap { width: 100%; overflow: hidden; background-color: #050505; border-bottom: 1px solid #1a1a1a; padding: 8px 0; margin-bottom: 20px;} 
    .ticker { display: inline-block; white-space: nowrap; padding-right: 100%; box-sizing: content-box; animation: ticker 40s linear infinite; font-family: monospace; font-size: 0.8rem; color: #888; text-transform:uppercase; } 
    .ticker-item { display: inline-block; padding: 0 2rem; border-right:1px solid #222; } 
    .market-clocks { display: flex; justify-content: space-between; flex-wrap:wrap; gap:10px; background: #0a0a0a; padding: 15px; border-radius: 4px; border: 1px solid #1a1a1a; margin-bottom: 20px; font-family: monospace; color: #666; } 
    .clock { text-align: center; flex:1; min-width:120px; border-right: 1px solid #111; } 
    .clock:last-child { border:none; } 
    .clock span { display: block; font-size: 1.2rem; color: #ccc; font-weight: normal; margin-top: 5px; letter-spacing:1px; }
    </style>
    '''
    
    ticker_html = '''
    <div class="ticker-wrap">
        <div class="ticker">
            <div class="ticker-item"><span style="color:#00C853;">[LIQUIDITY]</span> 1,240 BTC outflow from Binance confirmed</div>
            <div class="ticker-item"><span style="color:#FF3D00;">[DERIVATIVES]</span> $4.2M wiped on ETH perpetuals</div>
            <div class="ticker-item"><span style="color:var(--gold);">[MACRO]</span> US CPI aligns with consensus</div>
            <div class="ticker-item"><span style="color:#2962FF;">[ON-CHAIN]</span> Major accumulation spotted on SOL</div>
            <div class="ticker-item"><span style="color:#00C853;">[LIQUIDITY]</span> 1,240 BTC outflow from Binance confirmed</div>
            <div class="ticker-item"><span style="color:#FF3D00;">[DERIVATIVES]</span> $4.2M wiped on ETH perpetuals</div>
        </div>
    </div>
    '''
    
    clocks_html = '''
    <div class="market-clocks">
        <div class="clock">NY (NYSE) <span id="clock-ny">--:--</span></div>
        <div class="clock">LON (LSE) <span id="clock-lon">--:--</span></div>
        <div class="clock">TOK (TSE) <span id="clock-tok">--:--</span></div>
        <div class="clock">NETWORK STATUS <span style="color:#00C853;">ONLINE</span></div>
    </div>
    <script>
    function updateClocks() { 
        let d = new Date(); 
        document.getElementById("clock-ny").innerText = d.toLocaleTimeString("en-US", {timeZone: "America/New_York", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); 
        document.getElementById("clock-lon").innerText = d.toLocaleTimeString("en-US", {timeZone: "Europe/London", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); 
        document.getElementById("clock-tok").innerText = d.toLocaleTimeString("en-US", {timeZone: "Asia/Tokyo", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); 
    } 
    setInterval(updateClocks, 1000); 
    updateClocks();
    </script>
    '''

    index_content = f'''
    {ticker_css}
    {ticker_html}
    <div style="max-width: 1400px; margin: 0 auto;">
        {clocks_html}
        
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 class="section-title" style="margin:0; font-size:1.5rem; letter-spacing:-0.5px;">GLOBAL MACRO DATA</h2>
            <div style="font-size:0.7rem; color:#00C853; font-family:monospace; border:1px solid #00C853; padding:4px 8px; border-radius:2px;">
                API CONNECTED
            </div>
        </div>
        
        {filter_html}
        
        <div class="grid" id="markets-grid">
            {grid_html}
        </div>
        
        <div class="split-layout">
            <div class="panel" style="border-radius:4px; background:#0a0a0a; padding:20px; border:1px solid #1a1a1a;">
                {fng_html}
            </div>
            <div class="panel" style="border-radius:4px; background:#0a0a0a; padding:20px; border:1px solid #1a1a1a;">
                <h2 class="section-title" style="font-size:1.2rem; border-bottom:1px solid #222; padding-bottom:10px;">MARKET INTELLIGENCE</h2>
                <div class="table-responsive">
                    <table style="width:100%; border-collapse:collapse;">
                        <tbody>{news_rows}</tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    '''
    
    html = get_dashboard_layout("Terminal", index_content, active_page="dashboard")
    scrivi_file("index.html", html)

def build_signals_page(assets: List[Dict]):
    hot_assets = [a for a in assets if abs(a['change']) >= 1.0][:10]
    
    rows = ""
    for a in hot_assets:
        p = a["price"]
        c = a["change"]
        vol_mult = abs(c) / 100
        
        if c > 0:
            sig = "LONG BIAS"
            css = "signal-buy"
            sl = p * (1 - (vol_mult * 1.5))
            tp1 = p * (1 + (vol_mult * 2.0))
        else:
            sig = "SHORT BIAS"
            css = "signal-sell"
            sl = p * (1 + (vol_mult * 1.5))
            tp1 = p * (1 - (vol_mult * 2.0))
            
        rows += f'''
        <tr style="border-bottom: 1px solid #111;">
            <td style="padding:15px;">
                <strong style="font-size:1.1rem; color:#fff;">{a["symbol"]}</strong><br>
                <span style="font-size:0.7rem;color:#666;">{a["name"]}</span>
            </td>
            <td style="padding:15px; font-weight:bold; font-size:0.9rem;" class="{css}">
                {sig}
            </td>
            <td style="padding:15px; font-family:monospace;">
                <div style="font-size:0.65rem; color:#666;">ENTRY</div>
                <strong style="color:#ccc;">{format_price(p)}</strong>
            </td>
            <td style="padding:15px; font-family:monospace;">
                <div style="font-size:0.65rem; color:#666;">TARGET</div>
                <strong style="color:var(--gold);">{format_price(tp1)}</strong>
            </td>
            <td style="padding:15px; font-family:monospace;">
                <div style="font-size:0.65rem; color:#666;">INVALIDATION</div>
                <strong style="color:#FF3D00;">{format_price(sl)}</strong>
            </td>
            <td style="padding:15px; text-align:right;">
                <a href="chart_{a["id"]}.html" class="btn-trade" style="padding: 6px 12px; font-size:0.75rem; background:transparent; border:1px solid #333; color:#aaa; border-radius:2px; text-decoration:none;">
                    DATA
                </a>
            </td>
        </tr>
        '''

    content = f'''
    <div style="max-width: 1400px; margin: 0 auto;">
        <div class="panel" style="margin-bottom:30px; border-left:4px solid var(--gold); background: #0a0a0a; border-radius:4px; border-top:1px solid #1a1a1a; border-right:1px solid #1a1a1a; border-bottom:1px solid #1a1a1a; padding: 25px;">
            <h3 style="margin-top:0; color:#fff; font-size:1.2rem;">QUANTITATIVE RISK MODEL</h3>
            <p style="color:#888; font-size:0.85rem;">Calculate exact position exposure based on strict institutional tolerance algorithms.</p>
            
            <div class="wallet-form" style="padding:0; background:none; border:none; display:flex; gap:15px; align-items:flex-end;">
                <div style="flex:1; min-width:150px;">
                    <label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Capital ($)</label>
                    <input type="number" id="rm-balance" value="10000" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #222; color:#fff; font-family:monospace; border-radius:2px; outline:none; padding:10px;">
                </div>
                <div style="flex:1; min-width:150px;">
                    <label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Risk Exposure (%)</label>
                    <input type="number" id="rm-risk" value="1" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #222; color:#fff; font-family:monospace; border-radius:2px; outline:none; padding:10px;">
                </div>
                <div style="flex:1; min-width:150px;">
                    <label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Invalidation Dist. (%)</label>
                    <input type="number" id="rm-sl" value="2.5" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #222; color:#fff; font-family:monospace; border-radius:2px; outline:none; padding:10px;">
                </div>
                <div>
                    <button class="btn-trade" onclick="calcRisk()" style="padding:10px 24px; height:40px; border-radius:2px;">CALCULATE</button>
                </div>
            </div>
            
            <div id="rm-result" style="display:none; margin-top:20px; padding:15px; background:#000; border-radius:4px; border:1px solid #111;">
                <span style="color:#666; text-transform:uppercase; font-size:0.75rem;">Optimal Allocation Size:</span> 
                <strong id="rm-size" style="color:var(--gold); font-size:1.3rem; margin-left:10px; font-family:monospace;">$0</strong>
            </div>
        </div>
        
        <script>
        function calcRisk() {{
            let bal = parseFloat(document.getElementById("rm-balance").value);
            let risk = parseFloat(document.getElementById("rm-risk").value);
            let sl = parseFloat(document.getElementById("rm-sl").value);
            if(bal>0 && risk>0 && sl>0) {{
                let riskAmt = bal * (risk/100);
                let posSize = riskAmt / (sl/100);
                document.getElementById("rm-result").style.display = "flex";
                document.getElementById("rm-result").style.alignItems = "center";
                document.getElementById("rm-size").innerText = "$" + posSize.toLocaleString("en-US", {{maximumFractionDigits:2}});
            }}
        }}
        </script>
        
        <div style="border: 1px solid #222; padding: 15px; border-radius: 4px; margin-bottom: 40px; text-align: center; background:#0a0a0a;">
            <strong style="color: #FF3D00; font-size:0.8rem; letter-spacing:1px;">SYSTEM ADVISORY:</strong> 
            <span style="color: #888; font-size: 0.8rem;">Algorithmic targets are generated based on mathematical variance (ATR). Do not execute discretionary trades blindly.</span>
        </div>
        
        <h2 class="section-title" style="font-size:1.5rem; letter-spacing:-0.5px;">QUANTITATIVE SIGNALS ENGINE</h2>
        
        <div class="panel table-responsive" style="padding:0; border-radius:4px; border:1px solid #1a1a1a;">
            <table style="width:100%; border-collapse:collapse;">
                <thead>
                    <tr style="background:#050505; font-size:0.75rem; color:#666; text-transform:uppercase; border-bottom:1px solid #222; text-align:left;">
                        <th style="padding:15px;">ASSET</th>
                        <th>ALGO SIGNAL</th>
                        <th>ENTRY</th>
                        <th>TARGET ZONES</th>
                        <th>INVALIDATION</th>
                        <th style="text-align:right; padding-right:15px;">DATA</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
    </div>
    '''
    
    html = get_dashboard_layout("Signals Engine", content, active_page="signals")
    scrivi_file("signals.html", html)

def build_api_hub():
    content = '''
    <div style="max-width:800px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:40px;">
            <h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900; letter-spacing:-0.5px;">EXECUTION HUB</h1>
            <p style="color:#888; font-size:1rem;">Bridge exchange infrastructures to deploy automated strategy logic.</p>
        </div>
        
        <div class="panel" style="padding:40px; border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a;">
            <div id="api-form-container" class="wallet-form" style="background:none; border:none; padding:0; flex-direction:column; gap:20px; display:flex;">
                <div>
                    <label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold; letter-spacing:1px;">Protocol</label>
                    <select style="width:100%; margin-top:5px; padding:15px; background:#000; border:1px solid #222; color:#ccc; outline:none; border-radius:2px; font-family:monospace;">
                        <option>Binance FIX/REST API</option>
                        <option>Bybit Linear API</option>
                        <option>MEXC v3 API</option>
                    </select>
                </div>
                <div>
                    <label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold; letter-spacing:1px;">Public Key</label>
                    <input type="text" style="width:100%; box-sizing:border-box; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #222; color:#ccc; outline:none; border-radius:2px;" placeholder="Enter Public Key">
                </div>
                <div>
                    <label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold; letter-spacing:1px;">Private Key</label>
                    <input type="password" style="width:100%; box-sizing:border-box; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #222; color:#ccc; outline:none; border-radius:2px;" placeholder="Enter Private Key">
                </div>
                <button class="btn-trade" style="padding:15px; font-size:1rem; margin-top:10px; letter-spacing:1px; border-radius:2px; cursor:pointer;" onclick="connectAPI()">INITIALIZE CONNECTION</button>
            </div>
            
            <div class="hacker-terminal" id="term" style="display:none; cursor:text; height:250px; background:#000; border:1px solid #111; border-radius:2px; padding:20px; font-family:monospace; color:#888; font-size:0.9rem;" onclick="document.getElementById('term-input').focus()">
                <div id="term-content">> SYSTEM READY.<br>> Awaiting execution... (Type 'connect')<br></div>
                <div style="display:flex;">> <input type="text" id="term-input" onkeypress="checkTerminalCommand(event)" style="background:transparent; border:none; color:#ccc; font-family:monospace; outline:none; width:100%; margin-left:5px; font-size:0.9rem;" autocomplete="off" spellcheck="false"></div>
            </div>
        </div>
    </div>
    <script>
    function connectAPI() { 
        document.getElementById('api-form-container').style.display = 'none'; 
        document.getElementById('term').style.display = 'block'; 
        document.getElementById('term-input').focus(); 
    } 
    function checkTerminalCommand(e) { 
        if(e.key === 'Enter') { 
            let val = e.target.value.trim().toLowerCase(); 
            let term = document.getElementById('term-content'); 
            
            if(val === 'connect') { 
                e.target.value = ''; 
                e.target.disabled = true; 
                term.innerHTML += "><span style='color:#ccc;'> connect</span><br>> Establishing secure bridge...<br>"; 
                setTimeout(() => { term.innerHTML += "> Encrypting payload (AES-256)... <span style='color:#00C853;'>OK</span><br>"; }, 800); 
                setTimeout(() => { term.innerHTML += "> Requesting API permissions...<br>"; }, 1800); 
                setTimeout(() => { term.innerHTML += "<span style='color:#FF3D00; font-weight:bold;'>[!] EXECUTION REJECTED: TIER NOT AUTHORIZED</span><br>"; e.target.disabled = false; }, 3200); 
            } else { 
                term.innerHTML += "><span style='color:#ccc;'> " + val + "</span><br>> Command void. Type '<span style='color:#ccc;'>connect</span>'.<br>"; 
                e.target.value = ''; 
            } 
            let termDiv = document.getElementById('term'); 
            termDiv.scrollTop = termDiv.scrollHeight; 
        } 
    }
    </script>
    '''
    html = get_dashboard_layout("API Hub", content, active_page="dashboard")
    scrivi_file("api_hub.html", html)

def build_brokers_page():
    brokers = [
        {"name": "Binance", "type": "Spot & Derivatives", "pros": "Deepest Liquidity", "link": BINANCE_AFFILIATE_LINK, "cta": "PROVISION"},
        {"name": "Bybit", "type": "Perpetual Futures", "pros": "Low Latency API", "link": BYBIT_AFFILIATE_LINK, "cta": "PROVISION"},
        {"name": "MEXC", "type": "High Leverage", "pros": "0% Maker Fees", "link": AFF_MEXC, "cta": "PROVISION"}
    ]
    html_cards = "".join([f'''
        <div class="broker-card" style="border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a; padding:20px; transition:border-color 0.2s; display:flex; justify-content:space-between; align-items:center;">
            <div style="display:flex; align-items:center;">
                <div class="broker-info">
                    <h3 style="margin:0; color:#fff; font-size:1.2rem; font-weight:700;">{b["name"]}</h3>
                    <div class="broker-tags" style="margin-top:8px;">
                        <span style="background:#111; color:#888; border:1px solid #222; font-size:0.7rem; padding:4px 8px; border-radius:2px; display:inline-block; margin-right:5px; margin-bottom:5px;">{b["type"]}</span>
                        <span style="background:#111; color:#888; border:1px solid #222; font-size:0.7rem; padding:4px 8px; border-radius:2px; display:inline-block;">{b["pros"]}</span>
                    </div>
                </div>
            </div>
            <a href="{b["link"]}" target="_blank" style="padding:10px 20px; text-align:center; font-size:0.85rem; border-radius:2px; background:transparent; border:1px solid #333; color:#ccc; font-weight:600; letter-spacing:1px; text-decoration:none;">{b["cta"]}</a>
        </div>
    ''' for b in brokers])
    
    content = f'''
    <div style="max-width:800px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:50px;">
            <h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900; letter-spacing:-0.5px;">SUPPORTED VENUES</h1>
            <p style="color:#888; font-size:1rem; max-width:600px; margin:0 auto;">Certified exchange infrastructures for algorithmic deployment and secure custody.</p>
        </div>
        <div style="display:flex; flex-direction:column; gap:15px;">
            {html_cards}
        </div>
    </div>
    '''
    html = get_dashboard_layout("Exchanges", content, active_page="dashboard")
    scrivi_file("brokers.html", html)

def build_referral_page():
    content = '''
    <div style="max-width:800px; margin: 0 auto;">
        <div class="ref-box" style="border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a; padding:50px;">
            <h1 style="font-size:2rem; margin-top:0; color:#fff; font-weight:900; letter-spacing:-0.5px;">NETWORK EXPANSION</h1>
            <p style="color:#888; font-size:0.95rem; line-height:1.6;">Distribute your unique cryptographic identifier. Upon 3 successful network additions, Tier 2 clearance is granted automatically.</p>
            <div class="ref-link-container wallet-form" style="background:#000; border:1px solid #222; border-radius:4px; margin-top:30px; display:flex; align-items:center; justify-content:space-between; padding: 15px;">
                <div class="ref-link" id="ref-url" style="color:#ccc; font-family:monospace; font-size:0.85rem; overflow:hidden; text-overflow:ellipsis;">Loading link...</div>
                <button id="copy-btn" onclick="copyLink()" style="border-radius:2px; font-weight:600; letter-spacing:1px; background:#222; color:#fff; border:none; padding:15px 25px; cursor:pointer;">COPY LINK</button>
            </div>
        </div>
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        let user = localStorage.getItem("mip_user") || "profile_" + Math.floor(Math.random()*1000); 
        let link = `https://marketinsiderpro.com/invite/${user.toLowerCase()}`; 
        document.getElementById("ref-url").innerText = link; 
    }); 
    function copyLink() { 
        navigator.clipboard.writeText(document.getElementById("ref-url").innerText); 
        let btn = document.getElementById("copy-btn"); 
        btn.innerText = "COPIED"; 
        btn.style.background = "#fff"; 
        btn.style.color = "#000";
        setTimeout(() => { 
            btn.innerText = "COPY LINK"; 
            btn.style.background = "#222"; 
            btn.style.color = "#fff";
        }, 2000); 
    }
    </script>
    '''
    html = get_dashboard_layout("Referral", content, active_page="dashboard")
    scrivi_file("referral.html", html)

def build_pricing_page():
    content = '''
    <div style="max-width: 1400px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:50px;">
            <h1 style="font-size:3rem; margin-bottom:10px; font-weight:900; letter-spacing:-1px;">INSTITUTIONAL ACCESS</h1>
            <p style="color:#888; font-size:1rem; max-width:600px; margin:0 auto;">Upgrade data infrastructure. Access unmetered algorithmic feeds and the Paper Trading Simulator.</p>
        </div>
        
        <div class="pricing-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
            <div class="pricing-card" style="border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a; padding:40px;">
                <h3 style="color:#888; font-size:1rem; margin:0; letter-spacing:1px;">TIER 1 (STANDARD)</h3>
                <div class="price-tag" style="color:#ccc; font-size:2.5rem; font-weight:900; margin:15px 0;">$0<span style="color:#666; font-size:1rem; font-weight:normal;">/mo</span></div>
                <div style="margin-bottom:30px; font-size:0.85rem; color:#888; border-top:1px solid #111; padding-top:20px;">
                    <div class="plan-feature" style="margin-bottom:15px;">&#10003; Delayed Terminal Data</div>
                    <div class="plan-feature">&#10003; Basic Modeling</div>
                </div>
                <button style="width:100%; padding:15px; background:#111; color:#666; border:none; border-radius:2px; font-weight:600; font-size:0.9rem;">CURRENT TIER</button>
            </div>
            
            <div class="pricing-card pro" style="border-radius:4px; border:1px solid var(--gold); background:#050505; padding:40px; position:relative;">
                <div style="position:absolute; top:0; left:50%; transform:translate(-50%, -50%); background:var(--gold); color:#000; font-size:0.7rem; font-weight:bold; padding:4px 10px; border-radius:2px; letter-spacing:1px;">RECOMMENDED</div>
                <h3 style="color:var(--gold); font-size:1rem; margin:0; letter-spacing:1px;">TIER 2 (QUANT)</h3>
                <div class="price-tag" style="color:#fff; font-size:2.5rem; font-weight:900; margin:15px 0;">$49<span style="color:#888; font-size:1rem; font-weight:normal;">/mo</span></div>
                <div style="margin-bottom:30px; font-size:0.85rem; color:#ccc; border-top:1px solid #111; padding-top:20px;">
                    <div class="plan-feature" style="margin-bottom:15px;">&#10003; Real-Time Data Feeds</div>
                    <div class="plan-feature" style="margin-bottom:15px;">&#10003; Paper Trading Simulator</div>
                    <div class="plan-feature">&#10003; Signals Database</div>
                </div>
                <button onclick="openCheckoutChoice('https://buy.stripe.com/dRmcN56uTbIR6N8fux2Ry00')" style="width:100%; padding:15px; font-size:0.9rem; border-radius:2px; font-weight:700; background:var(--gold); color:#000; letter-spacing:1px; border:none; cursor:pointer;">PROVISION SECURELY</button>
            </div>
            
            <div class="pricing-card" style="border-radius:4px; border:1px solid #1a1a1a; background:#0a0a0a; padding:40px;">
                <h3 style="color:#2962FF; font-size:1rem; margin:0; letter-spacing:1px;">ENTERPRISE</h3>
                <div class="price-tag" style="color:#fff; font-size:2.5rem; font-weight:900; margin:15px 0;">$399<span style="color:#888; font-size:1rem; font-weight:normal;">/once</span></div>
                <div style="margin-bottom:30px; font-size:0.85rem; color:#ccc; border-top:1px solid #111; padding-top:20px;">
                    <div class="plan-feature" style="margin-bottom:15px;">&#10003; All Tier 2 Features</div>
                    <div class="plan-feature">&#10003; Perpetual Updates</div>
                </div>
                <button onclick="openCheckoutChoice('https://buy.stripe.com/14AfZh6uT9AJ3AW5TX2Ry01')" style="width:100%; padding:15px; border-radius:2px; font-weight:700; background:#fff; color:#000; letter-spacing:1px; border:none; cursor:pointer;">ACQUIRE LICENSE</button>
            </div>
        </div>
    </div>
    
    <div class="modal-overlay" id="checkout-choice-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:999; justify-content:center; align-items:center;">
        <div class="modal-content" style="max-width:400px; width:90%; text-align:center; padding:40px; border-radius:4px; border:1px solid #222; background:#0a0a0a; position:relative;">
            <span class="close-modal" onclick="document.getElementById('checkout-choice-modal').style.display='none'" style="position:absolute; top:15px; right:20px; font-size:1.5rem; color:#888; cursor:pointer;">&times;</span>
            <h2 style="color:#fff; margin-top:0; font-weight:900;">Authentication Required</h2>
            <p style="color:#888; font-size:0.85rem; margin-bottom:30px;">Select your provisioning pathway.</p>
            <div style="display:flex; flex-direction:column; gap:12px;">
                <button style="padding:15px; width:100%; border-radius:2px; font-weight:600; letter-spacing:1px; background:var(--gold); color:#000; border:none; cursor:pointer;" onclick="proceedToStripe('login')">
                    AUTHENTICATE FIRST
                </button>
                <button style="padding:15px; width:100%; background:transparent; border:1px solid #333; color:#aaa; border-radius:2px; font-weight:600; letter-spacing:1px; cursor:pointer;" onclick="proceedToStripe('guest')">
                    PROCEED AS GUEST
                </button>
            </div>
        </div>
    </div>
    <script>
    let currentStripeLink = ""; 
    function openCheckoutChoice(link) { 
        currentStripeLink = link; 
        let user = localStorage.getItem('mip_user'); 
        if(user) { 
            window.location.href = currentStripeLink; 
        } else { 
            document.getElementById('checkout-choice-modal').style.display = 'flex'; 
        } 
    } 
    function proceedToStripe(method) { 
        if(method === 'guest') { 
            window.location.href = currentStripeLink; 
        } else if(method === 'login') { 
            document.getElementById('checkout-choice-modal').style.display = 'none'; 
            // openLogin(); // Se hai una modal login
            alert("Login non ancora implementato");
        } 
    }
    </script>
    '''
    html = get_dashboard_layout("Pricing", content, active_page="pricing")
    scrivi_file("pricing.html", html)

def build_leaderboard_page():
    content = '''
    <div style="max-width:900px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:40px;">
            <h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900; letter-spacing:-0.5px;">GLOBAL METRICS</h1>
            <p style="color:#888; font-size:0.95rem; max-width:600px; margin:0 auto;">Statistical ranking of top network profiles by realized equity curve.</p>
        </div>
        <div class="panel table-responsive" style="padding:0; border-radius:4px; border:1px solid #1a1a1a;">
            <table style="width:100%; border-collapse:collapse;">
                <thead>
                    <tr style="background:#050505; border-bottom:1px solid #333; font-size:0.8rem; color:#666; text-align:left;">
                        <th style="padding:15px;">RANK</th>
                        <th>IDENTIFIER</th>
                        <th>CAPITAL DEPLOYED</th>
                        <th>30D YIELD</th>
                        <th>TIER</th>
                    </tr>
                </thead>
                <tbody id="lb-body">
                    <tr style="border-bottom:1px solid #222;">
                        <td class="rank-1" style="padding:15px; color:#fff; font-weight:bold;">#1</td>
                        <td><strong style="color:#ddd;">Entity_99</strong></td>
                        <td style="font-family:monospace; color:#aaa;">$1.2M</td>
                        <td style="color:#00C853; font-family:monospace;">+142.5%</td>
                        <td><span style="color:var(--gold); font-size:0.8rem; border:1px solid var(--gold); padding:2px 6px; border-radius:2px;">WHALE</span></td>
                    </tr>
                    <tr style="border-bottom:1px solid #222;">
                        <td class="rank-2" style="padding:15px; color:#fff; font-weight:bold;">#2</td>
                        <td><strong style="color:#ddd;">Quant_LDN</strong></td>
                        <td style="font-family:monospace; color:#aaa;">$450K</td>
                        <td style="color:#00C853; font-family:monospace;">+89.2%</td>
                        <td><span style="color:#888; font-size:0.8rem;">Tier 2</span></td>
                    </tr>
                    <tr style="border-bottom:1px solid #222;">
                        <td class="rank-3" style="padding:15px; color:#fff; font-weight:bold;">#3</td>
                        <td><strong style="color:#ddd;">CapitalX</strong></td>
                        <td style="font-family:monospace; color:#aaa;">$89K</td>
                        <td style="color:#00C853; font-family:monospace;">+64.8%</td>
                        <td><span style="color:#888; font-size:0.8rem;">Tier 2</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        let user = localStorage.getItem('mip_user'); 
        if(user) { 
            document.getElementById('lb-body').innerHTML += `<tr style="border-bottom:1px solid #222; background:#0a0a0a;"><td class="rank-3" style="padding:15px; color:#fff; font-weight:bold;">#8</td><td><strong style="color:#fff;">[YOU] ${user}</strong></td><td style="font-family:monospace; color:#aaa;">$14,250</td><td style="color:#00C853; font-family:monospace;">+18.4%</td><td><span style="color:#888; font-size:0.8rem;">Tier 2</span></td></tr>`; 
        } 
    });
    </script>
    '''
    html = get_dashboard_layout("Leaderboard", content, active_page="dashboard")
    scrivi_file("leaderboard.html", html)

def build_legal_page():
    content = '''
    <div style="max-width:800px; margin: 0 auto; color:#ccc;">
        <h1 style="color:#fff; font-weight:900;">Compliance & Policies</h1>
        <hr style="border-color:#222; margin-bottom:30px;">
        <h3 style="color:#fff; font-size:1.1rem; font-weight:700;">Data Policy</h3>
        <p style="color:#888; font-size:0.9rem; line-height:1.6;">Market Insider Pro utilizes client-side storage to minimize server dependency and enhance security. No identifiable data is harvested without consent.</p>
        <h3 style="color:#fff; font-size:1.1rem; margin-top:30px; font-weight:700;">Terms of Operation</h3>
        <p style="color:#888; font-size:0.9rem; line-height:1.6;">Platform access is contingent on adherence to network rules. Content is analytical, not advisory.</p>
    </div>
    '''
    html = get_dashboard_layout("Legal", content, active_page="dashboard")
    scrivi_file("legal.html", html)

def build_chart_pages(assets: List[Dict]):
    pass

def build_academy():
    sidebar = "".join([f"<div class='module-title' style='color:#666; font-size:0.7rem; font-weight:bold; letter-spacing:1px; margin-top:20px; border-bottom:1px solid #1a1a1a; padding-bottom:5px; margin-bottom:10px;'>{m['title']}</div>" + "".join([f'''<div onclick="window.location.href='academy_{l['id']}.html'" class="lesson-link" style="border-left:2px solid transparent; padding:8px 0; cursor:pointer; color:#aaa; font-size:0.85rem; transition:color 0.2s;">{"[LOCK]" if l.get("vip") else "[OPEN]"} {l['title']}</div>''' for l in m['lessons']]) for _, m in ACADEMY_CONTENT.items()])
    
    for _, m in ACADEMY_CONTENT.items():
        for l in m['lessons']:
            if l.get("vip"):
                c_html = f'''
                <div id="vip-content" style="filter: blur(12px); pointer-events: none; user-select: none; transition: 0.5s;">{l['html']}</div>
                <div id="vip-lock" style="position:absolute; top:40%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#050505; padding:40px; border:1px solid #222; border-radius:4px; z-index:10; width:90%; max-width:400px; box-shadow:0 20px 40px rgba(0,0,0,0.9);">
                    <h2 style="color:#fff; margin-top:0; font-weight:900;">RESTRICTED DATA</h2>
                    <p style="color:#888; margin-bottom:30px; font-size:0.85rem;">Protocol requires Tier 2 clearance.</p>
                    <a href="pricing.html" style="display:block; padding:12px; border-radius:2px; font-weight:600; letter-spacing:1px; background:var(--gold); color:#000; text-decoration:none;">AUTHENTICATE CLEARANCE</a>
                </div>
                <script>
                    document.addEventListener("DOMContentLoaded", function() {{ 
                        if(localStorage.getItem('mip_vip_status') === 'active') {{ 
                            document.getElementById('vip-content').style.filter = 'none'; 
                            document.getElementById('vip-content').style.pointerEvents = 'auto'; 
                            document.getElementById('vip-content').style.userSelect = 'auto'; 
                            document.getElementById('vip-lock').style.display = 'none'; 
                        }} 
                    }});
                </script>
                '''
            else:
                c_html = l['html']
                
            content = f'''
            <div class="academy-grid" style="display:grid; grid-template-columns: 280px 1fr; gap:40px; max-width: 1400px; margin: 0 auto;">
                <div class="academy-nav" style="background:#050505; border:1px solid #1a1a1a; border-radius:4px; padding:25px; height:fit-content;">{sidebar}</div>
                <div class="lesson-content" style="position:relative; background:#0a0a0a; padding:40px; border-radius:4px; border:1px solid #1a1a1a;">{c_html}</div>
            </div>
            '''
            html = get_dashboard_layout(l['title'], content, active_page="academy")
            scrivi_file(f"academy_{l['id']}.html", html)

def build_chat():
    content = '''
    <div style="max-width:800px; margin: 0 auto;">
        <h2 class="section-title" style="font-weight:900; font-size:2rem; text-align:center; margin-bottom:30px; letter-spacing:-0.5px; color:#fff;">QUANTITATIVE AI ANALYST</h2>
        <div class="chat-interface" style="border: 1px solid #1a1a1a; border-radius: 4px; background: #0a0a0a; height:600px; display:flex; flex-direction:column;">
            <div class="chat-history" id="hist" style="flex:1; padding:20px; overflow-y:auto;">
                <div class="msg msg-ai" style="text-align:left; margin-bottom:10px;">
                    <span style="background:#111; color:#888; border:1px solid #222; padding:10px 15px; border-radius:4px; display:inline-block; font-family:monospace; font-size:0.85rem;">System initialized. Awaiting parameters.</span>
                </div>
            </div>
            <div class="chat-input-area wallet-form" style="border-top: 1px solid #1a1a1a; padding:15px; display:flex; gap:10px; background:#050505;">
                <input type="text" class="chat-input" id="in" placeholder="Input query parameters..." style="flex:1; background:#000; border:1px solid #222; padding:15px; color:#fff; border-radius:2px; font-family: monospace; outline:none; font-size:0.9rem;">
                <button class="chat-btn" onclick="send()" style="background:#fff; color:#000; border:none; padding:15px 30px; border-radius: 2px; font-weight: 700; font-size:0.85rem; cursor:pointer; letter-spacing:1px;">EXECUTE</button>
            </div>
        </div>
    </div>
    <script>
    function send(){
        let i=document.getElementById('in'); 
        let v=i.value; 
        if(!v)return; 
        let h=document.getElementById('hist'); 
        h.innerHTML+=`<div class="msg msg-user" style="text-align:right; margin-bottom:10px;"><span style="background:#222; padding:10px 15px; border-radius:4px; display:inline-block; color:#fff; font-size:0.9rem;">${v}</span></div>`; 
        i.value=''; h.scrollTop=h.scrollHeight; 
        let t="t-"+Date.now(); 
        h.innerHTML+=`<div class="msg msg-ai" id="${t}" style="text-align:left; margin-bottom:10px;"><span style="background:#111; color:#888; border:1px solid #222; padding:10px 15px; border-radius:4px; display:inline-block; font-family:monospace; font-size:0.85rem;">Processing...</span></div>`; 
        h.scrollTop=h.scrollHeight; 
        setTimeout(()=>{
            document.getElementById(t).innerHTML=`<span style="background:#0a0a0a; color:#ccc; border:1px solid #333; padding:10px 15px; border-radius:4px; display:inline-block; font-family:monospace; font-size:0.85rem; line-height:1.5;">System Notice: Market sentiment variance detected. Consult the Quantitative Signals Engine.</span>`; 
            h.scrollTop=h.scrollHeight;
        }, 1200);
    } 
    document.getElementById('in').addEventListener("keypress", e=>{if(e.key==="Enter")send();});
    </script>
    '''
    html = get_dashboard_layout("AI Alpha Analyst", content, active_page="chat")
    scrivi_file("chat.html", html)

def build_wallet():
    content = '''
    <div style="max-width:900px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:40px;">
            <h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900; letter-spacing:-0.5px;">PORTFOLIO TRACKER</h1>
            <p style="color:#888; font-size:0.95rem;">Manual entry portfolio valuation using real-time Binance API pricing.</p>
        </div>
        
        <div style="text-align:center; padding: 50px; background:#0a0a0a; border-radius:4px; border:1px solid #1a1a1a; margin-bottom:30px;">
            <div style="color:#666; font-size:0.8rem; text-transform:uppercase; font-weight:bold; letter-spacing:1px;">Total Net Worth</div>
            <div id="total-net-worth" style="font-size:3rem; font-weight:900; color:#fff; font-family:monospace; margin:10px 0;">$0.00</div>
            <div style="font-size:0.75rem; color:#00C853; border:1px solid #00C853; display:inline-block; padding:2px 6px; border-radius:2px;">LIVE API SYNC</div>
        </div>
        
        <div class="wallet-form" style="background:#0a0a0a; border:1px solid #222; padding:20px; border-radius:4px; display:flex; gap:10px;">
            <input type="text" id="asset-select" placeholder="Asset Ticker (e.g. BTC)" style="flex:1; padding:12px; background:#000; border:1px solid #333; color:#fff; outline:none; text-transform:uppercase; font-family:monospace; border-radius:2px;">
            <input type="number" id="asset-amount" placeholder="Amount (e.g. 0.5)" style="flex:1; padding:12px; background:#000; border:1px solid #333; color:#fff; outline:none; font-family:monospace; border-radius:2px;">
            <button onclick="addAsset()" style="padding:12px 30px; border-radius:2px; font-weight:bold; letter-spacing:1px; background:#fff; color:#000; border:none; cursor:pointer;">ADD HOLDING</button>
        </div>
        
        <div class="panel table-responsive" style="padding:0; border-radius:4px; border:1px solid #1a1a1a; margin-top:30px;">
            <table style="width:100%; border-collapse:collapse;">
                <thead>
                    <tr style="background:#050505; border-bottom:1px solid #222; text-align:left; font-size:0.75rem; color:#666; text-transform:uppercase;">
                        <th style="padding:15px;">ASSET</th>
                        <th style="padding:15px;">AMOUNT</th>
                        <th style="padding:15px;">VALUE (USD)</th>
                        <th style="text-align:right; padding:15px;">ACTION</th>
                    </tr>
                </thead>
                <tbody id="wallet-body"></tbody>
            </table>
        </div>
    </div>
    <script>
    const W_KEY = "mip_manual_wallet"; 
    
    function loadWallet() { 
        let saved = localStorage.getItem(W_KEY); 
        let assets = saved ? JSON.parse(saved) : {}; 
        renderWalletTable(assets); 
        fetchLiveWorth(assets); 
    } 
    
    function addAsset() { 
        let id = document.getElementById("asset-select").value.toUpperCase(); 
        let amount = parseFloat(document.getElementById("asset-amount").value); 
        if(!id || isNaN(amount) || amount <= 0) return alert("Invalid amount."); 
        let saved = localStorage.getItem(W_KEY); 
        let assets = saved ? JSON.parse(saved) : {}; 
        assets[id] = (assets[id] || 0) + amount; 
        localStorage.setItem(W_KEY, JSON.stringify(assets)); 
        document.getElementById("asset-amount").value = ""; 
        document.getElementById("asset-select").value = "";
        loadWallet(); 
    } 
    
    function removeAsset(id) { 
        let saved = localStorage.getItem(W_KEY); 
        if(!saved) return; 
        let assets = JSON.parse(saved); 
        delete assets[id]; 
        localStorage.setItem(W_KEY, JSON.stringify(assets)); 
        loadWallet(); 
    } 
    
    function renderWalletTable(assets) { 
        let tbody = document.getElementById("wallet-body"); 
        tbody.innerHTML = ""; 
        if(Object.keys(assets).length === 0) { 
            tbody.innerHTML = "<tr><td colspan='4' style='text-align:center; color:#666; padding:20px;'>Portfolio empty. Add holdings above.</td></tr>"; 
            return; 
        } 
        for (const [id, amount] of Object.entries(assets)) { 
            tbody.innerHTML += `<tr style="border-bottom:1px solid #1a1a1a;"><td style="padding:15px; font-weight:bold; color:#fff;">${id}</td><td style="padding:15px; font-family:monospace; color:#aaa;">${amount}</td><td style="padding:15px; color:#fff; font-family:monospace; font-weight:bold;" id="val-${id}">Loading...</td><td style="text-align:right; padding:15px;"><button onclick="removeAsset('${id}')" style="background:transparent; color:#888; border:1px solid #333; padding:4px 8px; border-radius:2px; cursor:pointer; font-size:0.7rem;">REMOVE</button></td></tr>`; 
        } 
    } 
    
    async function fetchLiveWorth(assets) { 
        if(Object.keys(assets).length === 0) { 
            document.getElementById("total-net-worth").innerText = "$0.00"; return; 
        } 
        try { 
            let res = await fetch('https://api.binance.com/api/v3/ticker/price'); 
            let data = await res.json(); 
            let priceMap = {}; 
            data.forEach(item => { priceMap[item.symbol] = parseFloat(item.price); }); 
            
            let total = 0; 
            for (const [id, amount] of Object.entries(assets)) { 
                let symbol = id + "USDT"; 
                let currentPrice = priceMap[symbol]; 
                if(currentPrice) { 
                    let value = currentPrice * amount; 
                    total += value; 
                    let el = document.getElementById(`val-${id}`); 
                    if (el) el.innerText = "$" + value.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); 
                } 
            } 
            document.getElementById("total-net-worth").innerText = "$" + total.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); 
        } catch(e) {} 
    } 
    
    document.addEventListener("DOMContentLoaded", loadWallet); 
    setInterval(loadWallet, 5000); 
    </script>
    '''
    html = get_dashboard_layout("Portfolio Tracker", content, active_page="wallet")
    scrivi_file("wallet.html", html)

def build_success_page():
    content = '''
    <div style="text-align:center; padding: 120px 20px;">
        <h1 style="color:var(--gold); font-size:3rem; margin-top:10px; font-weight:900;">TIER UPGRADE COMPLETE</h1>
        <p style="color:#aaa; font-size:1.1rem; max-width:500px; margin:0 auto;">Payment verification successful. The Paper Trading Simulator and Institutional Data Pathways are now unlocked.</p>
        <div style="margin-top:40px;">
            <div style="width:40px; height:40px; border:3px solid var(--gold); border-top-color:transparent; border-radius:50%; animation:spin 1s linear infinite; margin:0 auto;"></div>
        </div>
    </div>
    <style>@keyframes spin { 100% { transform:rotate(360deg); } }</style>
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        localStorage.setItem('mip_vip_status', 'active'); 
        setTimeout(() => { window.location.href = "vip_lounge.html"; }, 3500); 
    });
    </script>
    '''
    html = get_dashboard_layout("Clearance Granted", content, active_page="pricing")
    scrivi_file("success.html", html)

def build_cheatsheets():
    ob_content = f'''
    <div style="max-width:800px; margin:0 auto; padding: 40px 20px;">
        <div style="background:#0a0a0a; border:1px solid #222; padding:40px; border-radius:4px;">
            <h1 style="color:var(--gold); margin-top:0; border-bottom:1px solid #1a1a1a; padding-bottom:15px; font-weight:900;">CONFIDENTIAL: ORDER BLOCK STRATEGY</h1>
            <p style="color:#666; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px; font-weight:bold;">Internal Training Document - Do not distribute</p>
            
            <h3 style="color:#fff; margin-top:30px; font-weight:700;">1. Identifying the Footprint</h3>
            <p style="color:#aaa; line-height:1.7; font-size:0.95rem;">An Order Block (OB) represents a massive accumulation of assets by institutions. It is visually identified on the chart as the <b>last bearish candle before a strong, impulsive bullish move</b> that breaks market structure.</p>
            
            <h3 style="color:#fff; margin-top:30px; font-weight:700;">2. The Institutional Execution</h3>
            <p style="color:#aaa; line-height:1.7; font-size:0.95rem;">Institutions cannot enter their entire position at once without moving the market against themselves. They push the price down to grab liquidity (retail stop losses), buy massive amounts, and wait for the price to return to their "Block" to fill the rest of their orders.</p>
            
            <ul style="color:#aaa; line-height:1.8; font-size:0.95rem;">
                <li><b>Step 1:</b> Mark the high and low of the OB candle.</li>
                <li><b>Step 2:</b> Wait patiently for the price to retrace back into this zone.</li>
                <li><b>Step 3:</b> Execute your entry exactly at the top of the OB.</li>
                <li><b>Step 4:</b> Place the Stop Loss slightly below the bottom of the OB.</li>
            </ul>
            
            <div style="margin-top:50px; padding:30px; background:#050505; border:1px solid #333; border-radius:4px; text-align:center;">
                <h3 style="color:#fff; margin-top:0; font-weight:700;">MAXIMIZE YOUR EDGE</h3>
                <p style="color:#888; font-size:0.9rem; margin-bottom:20px;">To execute Order Block strategies successfully, you need an exchange with deep liquidity, institutional-grade charts, and absolutely zero slippage.</p>
                <a href="{BYBIT_AFFILIATE_LINK}" target="_blank" style="background:var(--gold); color:#000; padding:12px 30px; font-size:0.95rem; display:inline-block; text-decoration:none; border-radius:2px; font-weight:bold; letter-spacing:1px;">OPEN PRO EXCHANGE ACCOUNT</a>
            </div>
            
            <button onclick="window.close()" style="background:none; border:none; color:#666; text-decoration:underline; cursor:pointer; display:block; margin:30px auto 0; font-size:0.85rem;">Close Document</button>
        </div>
    </div>
    '''
    html = get_dashboard_layout("Order Block Strategy", ob_content, active_page="vip")
    scrivi_file("cheatsheet_ob.html", html)

    risk_content = f'''
    <div style="max-width:800px; margin:0 auto; padding: 40px 20px;">
        <div style="background:#0a0a0a; border:1px solid #222; padding:40px; border-radius:4px;">
            <h1 style="color:#FF3D00; margin-top:0; border-bottom:1px solid #1a1a1a; padding-bottom:15px; font-weight:900;">RISK MANAGEMENT PROTOCOL</h1>
            <p style="color:#666; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px; font-weight:bold;">Capital Preservation Directive</p>
            
            <h3 style="color:#fff; margin-top:30px; font-weight:700;">The 1% Golden Rule</h3>
            <p style="color:#aaa; line-height:1.7; font-size:0.95rem;">Professional traders do not gamble. They protect capital. You must never risk more than <b>1% of your total account balance</b> on a single trade. If your account is $10,000, your absolute maximum allowed loss if the trade hits your Stop Loss is $100.</p>
            
            <h3 style="color:#fff; margin-top:30px; font-weight:700;">The Position Sizing Formula</h3>
            <p style="color:#aaa; line-height:1.7; font-size:0.95rem;">To calculate exactly how many dollars to invest in a trade to respect the 1% rule, use the following institutional formula:</p>
            
            <code style="background:#000; border:1px solid #333; padding:20px; display:block; color:#fff; border-radius:4px; margin:20px 0; font-size:1rem; text-align:center; font-family:monospace;">
                Position Size = (Account Balance * Risk %) / Stop Loss Distance %
            </code>
            
            <p style="color:#aaa; line-height:1.7; font-size:0.95rem;">Example: $10,000 balance, 1% risk ($100), and your Stop Loss is 5% away. <br>Your Position Size is: $100 / 0.05 = <b style="color:#fff;">$2,000</b>. You buy $2,000 worth of the asset.</p>
            
            <div style="margin-top:50px; padding:30px; background:#050505; border:1px solid #333; border-radius:4px; text-align:center;">
                <h3 style="color:#00C853; margin-top:0; font-weight:700;">SECURE YOUR PROFITS</h3>
                <p style="color:#888; font-size:0.9rem; margin-bottom:20px;">Hedge funds never keep their long-term capital or massive profits sitting on a live exchange. Once you hit your targets, move your wealth completely offline to cold storage.</p>
                <a href="{AMAZON_LINK_LEDGER}" target="_blank" style="background:#00C853; color:#000; padding:12px 30px; font-size:0.95rem; display:inline-block; text-decoration:none; font-weight:bold; border-radius:2px; letter-spacing:1px;">GET HARDWARE WALLET</a>
            </div>
            
            <button onclick="window.close()" style="background:none; border:none; color:#666; text-decoration:underline; cursor:pointer; display:block; margin:30px auto 0; font-size:0.85rem;">Close Document</button>
        </div>
    </div>
    '''
    html = get_dashboard_layout("Risk Management Protocol", risk_content, active_page="vip")
    scrivi_file("cheatsheet_risk.html", html)

def build_vip_lounge():
    build_cheatsheets() 
    content = '''
    <div style="position:relative; max-width: 1400px; margin: 0 auto;">
        
        <div id="vip-lock" style="text-align:center; background:#0a0a0a; padding:80px 20px; border:1px solid #1a1a1a; border-radius:4px;">
            <div style="width:40px; height:40px; border:2px solid #555; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto; color:#555; font-weight:bold;">!</div>
            <h2 style="color:#fff; margin-top:0; font-weight:900; font-size:2rem; letter-spacing:-0.5px;">RESTRICTED ENVIRONMENT</h2>
            <p style="color:#888; margin-bottom:30px; font-size:0.95rem; max-width:500px; margin-left:auto; margin-right:auto; line-height:1.6;">The Live Paper Trading Simulator utilizes the real-time Binance Order Book API to allow risk-free execution testing with $100,000 in simulated capital. Tier 2 verification required.</p>
            <a href="pricing.html" style="display:inline-block; padding:15px 35px; text-decoration:none; border-radius:2px; font-weight:700; margin-top:10px; letter-spacing:1px; background:var(--gold); color:#000;">INITIATE CLEARANCE</a>
        </div>

        <div id="vip-content" style="display:none;">
            
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:30px; border-bottom:1px solid #1a1a1a; padding-bottom:30px; flex-wrap:wrap; gap:20px;">
                <div>
                    <div style="font-size:0.75rem; color:var(--gold); letter-spacing:2px; font-weight:bold; margin-bottom:5px;">■ TIER 2 VERIFIED</div>
                    <h1 style="font-size:2.5rem; margin:0; font-weight:900; color:#fff; letter-spacing:-1px;">PAPER TRADING TERMINAL</h1>
                    <p style="color:#666; margin:5px 0 0 0; font-size:0.9rem;">Test algorithms without financial risk using live market data.</p>
                </div>
                
                <div style="display:flex; gap:30px;">
                    <div style="text-align:right;">
                        <div style="font-size:0.7rem; color:#666; text-transform:uppercase; font-weight:bold; letter-spacing:1px; margin-bottom:5px;">Available Liquidity</div>
                        <div id="pt-balance" style="font-size:2rem; font-weight:900; color:#fff; font-family:monospace;">$100,000.00</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:0.7rem; color:#666; text-transform:uppercase; font-weight:bold; letter-spacing:1px; margin-bottom:5px;">Unrealized PNL</div>
                        <div id="pt-unrealized" style="font-size:2rem; font-weight:900; color:#888; font-family:monospace;">$0.00</div>
                    </div>
                </div>
            </div>
            
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-bottom:40px;">
                <div class="panel" style="background:#0a0a0a; border:1px solid #1a1a1a; border-radius:4px; padding:25px;">
                    <h3 style="color:#fff; font-size:1.1rem; margin-top:0; border-bottom:1px solid #222; padding-bottom:10px;">PROPRIETARY ALPHA MODELS</h3>
                    <p style="color:#888; font-size:0.85rem; line-height:1.6; margin-bottom:20px;">Review the framework before executing simulated trades.</p>
                    
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                        <button style="flex:1; padding:10px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; font-size:0.8rem; font-weight:600; cursor:pointer; min-width:140px;" onclick="window.open('cheatsheet_ob.html', '_blank')">Order Block Model</button>
                        <button style="flex:1; padding:10px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; font-size:0.8rem; font-weight:600; cursor:pointer; min-width:140px;" onclick="window.open('cheatsheet_risk.html', '_blank')">Risk Algorithm</button>
                    </div>
                </div>

                <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px; padding:25px;">
                    <h3 style="color:#fff; font-size:1.1rem; margin-top:0; border-bottom:1px solid #222; padding-bottom:10px;">ORDER EXECUTION</h3>
                    <div class="pt-form" style="display:flex; gap:10px; align-items:center; margin-top:20px;">
                        <input type="text" id="pt-ticker" placeholder="TICKER (e.g. BTC)" style="width:130px; padding:12px; background:#000; border:1px solid #333; color:#fff; text-transform:uppercase; outline:none; font-family:monospace; border-radius:2px;">
                        <input type="number" id="pt-amount" placeholder="Size in USD ($)" style="flex:1; padding:12px; background:#000; border:1px solid #333; color:#fff; outline:none; font-family:monospace; border-radius:2px;">
                        <button id="pt-buy-btn" onclick="executePaperTrade()" style="padding:12px 25px; border-radius:2px; font-weight:bold; background:#fff; color:#000; border:none; cursor:pointer;">MARKET BUY</button>
                    </div>
                    <p style="color:#555; font-size:0.7rem; margin-top:15px;">Orders are routed to Binance spot pricing API. Zero slippage applied for theoretical testing.</p>
                </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #222; padding-bottom:10px; margin-bottom:15px;">
                <h3 style="color:#fff; font-size:1.1rem; margin:0;">ACTIVE HOLDINGS</h3>
                <div style="font-size:0.7rem; color:#00C853; border:1px solid #00C853; padding:2px 6px; border-radius:2px;">MARKET DATA LIVE</div>
            </div>

            <div class="panel table-responsive" style="padding:0; border:1px solid #1a1a1a; border-radius:4px; background:#0a0a0a;">
                <table style="width:100%; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#000; border-bottom:1px solid #222; text-align:left; font-size:0.7rem; color:#666; text-transform:uppercase;">
                            <th style="padding:15px;">ASSET</th>
                            <th style="padding:15px;">SIZE</th>
                            <th style="padding:15px;">ENTRY PRICE</th>
                            <th style="padding:15px;">LIVE PRICE</th>
                            <th style="padding:15px;">UNREALIZED PNL</th>
                            <th style="text-align:right; padding:15px;">ACTION</th>
                        </tr>
                    </thead>
                    <tbody id="pt-body"></tbody>
                </table>
            </div>
            
            <div style="text-align:right; margin-top:20px;">
                <button onclick="resetDemo()" style="background:transparent; border:none; color:#555; text-decoration:underline; cursor:pointer; font-size:0.75rem;">Reset Simulation Data</button>
            </div>
        </div>
        
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        if(localStorage.getItem('mip_vip_status') === 'active') {
            document.getElementById('vip-content').style.display = 'block';
            document.getElementById('vip-lock').style.display = 'none';
            loadPaperTrading();
        }
    });

    const PT_BAL_KEY = "mip_paper_balance";
    const PT_POS_KEY = "mip_paper_positions";
    let livePrices = {};

    function loadPaperTrading() {
        let bal = localStorage.getItem(PT_BAL_KEY);
        if(!bal) { bal = 100000; localStorage.setItem(PT_BAL_KEY, bal); }
        document.getElementById('pt-balance').innerText = "$" + parseFloat(bal).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});
        updatePT_Prices();
        setInterval(updatePT_Prices, 2000);
    }

    async function updatePT_Prices() {
        try {
            let res = await fetch('https://api.binance.com/api/v3/ticker/price');
            let data = await res.json();
            data.forEach(item => { livePrices[item.symbol] = parseFloat(item.price); });
            renderPT_Positions();
        } catch(e) {}
    }

    function executePaperTrade() {
        let ticker = document.getElementById('pt-ticker').value.toUpperCase() + "USDT";
        let amountUSD = parseFloat(document.getElementById('pt-amount').value);
        let bal = parseFloat(localStorage.getItem(PT_BAL_KEY));
        
        if(!livePrices[ticker]) return alert("Invalid Ticker or Live Price not available.");
        if(isNaN(amountUSD) || amountUSD <= 0 || amountUSD > bal) return alert("Invalid Amount or Insufficient Simulated Balance.");

        let price = livePrices[ticker];
        let qty = amountUSD / price;
        
        bal -= amountUSD;
        localStorage.setItem(PT_BAL_KEY, bal);
        document.getElementById('pt-balance').innerText = "$" + bal.toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});

        let pos = JSON.parse(localStorage.getItem(PT_POS_KEY) || "{}");
        if(pos[ticker]) {
            let newQty = pos[ticker].qty + qty;
            let newAvg = ((pos[ticker].qty * pos[ticker].avgPrice) + (qty * price)) / newQty;
            pos[ticker] = {qty: newQty, avgPrice: newAvg};
        } else {
            pos[ticker] = {qty: qty, avgPrice: price};
        }
        
        localStorage.setItem(PT_POS_KEY, JSON.stringify(pos));
        renderPT_Positions();
        
        document.getElementById('pt-amount').value = "";
        
        let btn = document.getElementById('pt-buy-btn');
        let oldText = btn.innerText;
        btn.innerText = "ORDER FILLED";
        btn.style.background = "#00C853";
        btn.style.color = "#000";
        setTimeout(()=>{ btn.innerText = oldText; btn.style.background = "#fff"; btn.style.color = "#000"; }, 1000);
    }

    function closePosition(ticker) {
        let pos = JSON.parse(localStorage.getItem(PT_POS_KEY) || "{}");
        if(!pos[ticker]) return;
        
        let currentPrice = livePrices[ticker];
        let value = pos[ticker].qty * currentPrice;
        
        let bal = parseFloat(localStorage.getItem(PT_BAL_KEY));
        bal += value;
        localStorage.setItem(PT_BAL_KEY, bal);
        document.getElementById('pt-balance').innerText = "$" + bal.toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});
        
        delete pos[ticker];
        localStorage.setItem(PT_POS_KEY, JSON.stringify(pos));
        renderPT_Positions();
    }

    function renderPT_Positions() {
        let pos = JSON.parse(localStorage.getItem(PT_POS_KEY) || "{}");
        let tbody = document.getElementById('pt-body');
        tbody.innerHTML = "";
        
        if(Object.keys(pos).length === 0) {
            tbody.innerHTML = "<tr><td colspan='6' style='text-align:center; padding:30px; color:#666;'>No active orders. Execute a paper trade to begin simulation.</td></tr>";
            
            let pnlEl = document.getElementById('pt-unrealized');
            pnlEl.innerText = "$0.00";
            pnlEl.style.color = "#888";
            return;
        }

        let totalUnrealized = 0;

        for(const [ticker, data] of Object.entries(pos)) {
            let currentPrice = livePrices[ticker] || data.avgPrice;
            let pnlPerc = ((currentPrice - data.avgPrice) / data.avgPrice) * 100;
            let pnlUSD = (currentPrice - data.avgPrice) * data.qty;
            totalUnrealized += pnlUSD;
            
            let pnlColor = pnlPerc >= 0 ? "#00C853" : "#FF3D00";

            tbody.innerHTML += `
            <tr style="border-bottom:1px solid #1a1a1a;">
                <td style="padding:15px; font-weight:bold; color:#fff;">${ticker.replace('USDT','')}</td>
                <td style="padding:15px; font-family:monospace; color:#aaa;">${data.qty.toFixed(4)}</td>
                <td style="padding:15px; font-family:monospace; color:#aaa;">$${data.avgPrice.toFixed(2)}</td>
                <td style="padding:15px; font-family:monospace; color:#fff; font-weight:bold;">$${currentPrice.toFixed(2)}</td>
                <td style="padding:15px; font-family:monospace; color:${pnlColor}; font-weight:bold;">${pnlPerc > 0 ? '+':''}${pnlPerc.toFixed(2)}% ($${pnlUSD.toFixed(2)})</td>
                <td style="padding:15px; text-align:right;"><button onclick="closePosition('${ticker}')" style="background:transparent; border:1px solid #333; color:#aaa; padding:6px 12px; cursor:pointer; font-size:0.7rem; border-radius:2px; font-weight:bold; transition:all 0.2s;" onmouseover="this.style.borderColor='#FF3D00'; this.style.color='#FF3D00';" onmouseout="this.style.borderColor='#333'; this.style.color='#aaa';">CLOSE</button></td>
            </tr>`;
        }
        
        let pnlEl = document.getElementById('pt-unrealized');
        pnlEl.innerText = (totalUnrealized >= 0 ? "+$" : "-$") + Math.abs(totalUnrealized).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});
        pnlEl.style.color = totalUnrealized >= 0 ? "#00C853" : "#FF3D00";
    }
    
    function resetDemo() {
        if(confirm("Warning: This will wipe your simulated portfolio history. Reset back to $100,000?")) {
            localStorage.setItem(PT_BAL_KEY, 100000);
            localStorage.setItem(PT_POS_KEY, "{}");
            loadPaperTrading();
        }
    }
    </script>
    '''
    html = get_dashboard_layout("VIP Lounge", content, active_page="vip")
    scrivi_file("vip_lounge.html", html)

def build_stories_page():
    content = '''
    <div style="max-width:1400px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:50px;">
            <h1 style="font-size:3rem; margin-bottom:10px; font-weight:900; letter-spacing:-1px;">CLIENT <span style="color:#fff;">CASE STUDIES</span></h1>
            <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Verified analytical accounts of retail participants transitioning to quantitative frameworks using our proprietary data.</p>
        </div>
        
        <div class="grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
            <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px; border-top: 3px solid #00C853; position:relative; padding:25px;">
                <div style="position:absolute; top:-15px; right:20px; background:#00C853; color:#000; padding:4px 8px; border-radius:2px; font-weight:bold; font-size:0.7rem; letter-spacing:1px;">FUNDED PORTFOLIO</div>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:10px;">"From discretionary bias to systematic execution."</h3>
                <p style="color:#888; font-size:0.9rem; line-height:1.6;">"Before integrating MIP, I traded on emotional sentiment. The Order Block metrics inside the VIP infrastructure eliminated prediction. I now execute solely on institutional liquidity footprints."</p>
                <div style="margin-top:20px; padding-top:20px; border-top:1px solid #111; display:flex; align-items:center; gap:15px;">
                    <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=100&q=80" style="width:40px; height:40px; border-radius:50%; object-fit:cover; border:1px solid #333;">
                    <div>
                        <strong style="color:#ccc; display:block; font-size:0.9rem;">Marcus T.</strong>
                        <span style="color:#666; font-size:0.75rem;">Quant Tier since Q3 2025</span>
                    </div>
                </div>
            </div>
            
            <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px; border-top: 3px solid var(--gold); position:relative; padding:25px;">
                <div style="position:absolute; top:-15px; right:20px; background:var(--gold); color:#000; padding:4px 8px; border-radius:2px; font-weight:bold; font-size:0.7rem; letter-spacing:1px;">DATA ARBITRAGE</div>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:10px;">"Uncovering the macro context."</h3>
                <p style="color:#888; font-size:0.9rem; line-height:1.6;">"The simulated Macro Correlation Matrix provided answers that standard retail charts obfuscate. Tracking cross-asset liquidity flows gave me an asymmetric edge over retail counterparts."</p>
                <div style="margin-top:20px; padding-top:20px; border-top:1px solid #111; display:flex; align-items:center; gap:15px;">
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=100&q=80" style="width:40px; height:40px; border-radius:50%; object-fit:cover; border:1px solid #333;">
                    <div>
                        <strong style="color:#ccc; display:block; font-size:0.9rem;">Elena S.</strong>
                        <span style="color:#666; font-size:0.75rem;">Quant Tier since Q4 2025</span>
                    </div>
                </div>
            </div>
            
            <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px; border-top: 3px solid #2962FF; position:relative; padding:25px;">
                <div style="position:absolute; top:-15px; right:20px; background:#2962FF; color:#fff; padding:4px 8px; border-radius:2px; font-weight:bold; font-size:0.7rem; letter-spacing:1px;">API AUTOMATION</div>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:10px;">"Removing the human error variable."</h3>
                <p style="color:#888; font-size:0.9rem; line-height:1.6;">"Connecting my Bybit architecture to the Execution Hub was the final step. The Risk Module handles position sizing, and the algorithm manages deployment. Complete isolation of capital management."</p>
                <div style="margin-top:20px; padding-top:20px; border-top:1px solid #111; display:flex; align-items:center; gap:15px;">
                    <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=100&q=80" style="width:40px; height:40px; border-radius:50%; object-fit:cover; border:1px solid #333;">
                    <div>
                        <strong style="color:#ccc; display:block; font-size:0.9rem;">David K.</strong>
                        <span style="color:#666; font-size:0.75rem;">Quant Tier since Q1 2026</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div style="text-align:center; margin-top:60px; padding:40px; background:#0a0a0a; border:1px solid #222; border-radius:4px;">
            <h2 style="color:#fff; margin-top:0; font-weight:900;">Ready to execute systematically?</h2>
            <p style="color:#888; margin-bottom:30px; font-size:0.95rem;">Stop gambling and start trading with an institutional edge.</p>
            <a href="pricing.html" style="padding:15px 40px; font-size:1rem; text-decoration:none; border-radius:2px; font-weight:bold; letter-spacing:1px; background:var(--gold); color:#000;">PROVISION TIER 2</a>
        </div>
    </div>
    '''
    html = get_dashboard_layout("Case Studies", content, active_page="dashboard")
    scrivi_file("stories.html", html)

def build_tools_page():
    content = f'''
    <style>
    .stack-category {{ color: #666; font-size: 0.75rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-top: 40px; border-bottom: 1px solid #1a1a1a; padding-bottom: 10px; margin-bottom: 20px; }}
    .stack-card {{ background: #0a0a0a; border: 1px solid #1a1a1a; border-radius: 4px; padding: 25px; transition: border-color 0.2s; }}
    .stack-card:hover {{ border-color: #333; }}
    .stack-badge {{ display: inline-block; padding: 3px 6px; font-size: 0.6rem; font-weight: bold; letter-spacing: 1px; border-radius: 2px; margin-bottom: 15px; text-transform:uppercase; }}
    </style>
    <div style="max-width: 1400px; margin: 0 auto;">
        <div style="text-align:center; margin-bottom:50px;">
            <h1 style="font-size:3rem; margin-bottom:10px; font-weight:900; letter-spacing:-1px;">INSTITUTIONAL <span style="color:#fff;">STACK</span></h1>
            <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">The mandatory software architecture for quantitative market integration.</p>
        </div>

        <div class="stack-category">LAYER 1: EXECUTION & LIQUIDITY</div>
        <div class="grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#00C853; border:1px solid #00C853;">CAPITAL FUNDING</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">FTMO Infrastructure</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Leverage external capital. Pass evaluation parameters to secure up to $200k in AUM.</p>
                <a href="{AFF_FTMO}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:#fff; color:#000; border-radius:2px; font-weight:600; text-decoration:none; box-sizing:border-box;">ALLOCATE FUNDS</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#FF5252; border:1px solid #FF5252;">DERIVATIVES</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">MEXC Global Engine</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">High-capacity order execution with 0% margin maker fees and deep market depth.</p>
                <a href="{AFF_MEXC}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">OPEN VENUE</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#2962FF; border:1px solid #2962FF;">AUTOMATION</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">Quantitative Bots</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Deploy continuous DCA and Grid algorithms natively via API without human error.</p>
                <a href="{AFF_MEXC_BOTS}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">DEPLOY BOTS</a>
            </div>
        </div>

        <div class="stack-category">LAYER 2: DATA & ANALYTICS</div>
        <div class="grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#fff; border:1px solid #fff;">VISUALIZATION</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">TradingView Pro</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">The standard for charting infrastructure. Mandatory for volume delta modeling.</p>
                <a href="{AFF_TRADINGVIEW}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">UPGRADE LICENSE</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:var(--gold); border:1px solid var(--gold);">ON-CHAIN</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">Glassnode Metrics</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Access raw blockchain data regarding miner outflow and institutional reserves.</p>
                <a href="{AFF_GLASSNODE}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">ACCESS DATA</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#00C853; border:1px solid #00C853;">FLOW TRACKING</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">CryptoQuant</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Monitor central exchange reserves and derivative funding rates in real-time.</p>
                <a href="{AFF_CRYPTOQUANT}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">TRACK INFLOWS</a>
            </div>
        </div>

        <div class="stack-category">LAYER 3: COMPLIANCE & SECURITY</div>
        <div class="grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px;">
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#FF3D00; border:1px solid #FF3D00;">ENCRYPTION</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">NordVPN Protocols</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Mandatory encryption standard for interacting with execution APIs over public networks.</p>
                <a href="{AFF_NORDVPN}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">SECURE CHANNEL</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#8A2BE2; border:1px solid #8A2BE2;">AUDIT</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">Koinly Tax Protocol</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">Automate regulatory reports and calculate fiscal liabilities via secure API reading.</p>
                <a href="{AFF_KOINLY}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">GENERATE REPORT</a>
            </div>
            <div class="stack-card">
                <span class="stack-badge" style="background:#111; color:#007BFF; border:1px solid #007BFF;">CUSTODY</span>
                <h3 style="color:#fff; font-size:1.2rem; margin-top:0;">Trezor Hardware</h3>
                <p style="color:#888; font-size:0.85rem; line-height:1.6;">The industry-standard open-source cold storage for securing private keys offline.</p>
                <a href="{AFF_TREZOR}" target="_blank" style="width:100%; display:block; text-align:center; padding:10px; margin-top:20px; background:transparent; border:1px solid #333; color:#ccc; border-radius:2px; text-decoration:none; box-sizing:border-box;">SECURE KEYS</a>
            </div>
        </div>
    </div>
    '''
    html = get_dashboard_layout("Institutional Stack", content, active_page="tools")
    scrivi_file("tools.html", html)

def build_seo_files():
    BASE_URL = "https://marketinsiderpro.com"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    pages = [
        "index.html", "signals.html", "api_hub.html", "brokers.html", 
        "referral.html", "pricing.html", "leaderboard.html", "legal.html",
        "academy_lez1_1.html", "academy_lez2_1.html", "academy_lez3_1.html", "academy_lez4_1.html", "academy_lez5_1.html",
        "chat.html", "wallet.html", "vip_lounge.html", "stories.html", "tools.html"
    ]
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:
        priority = "1.0" if page == "index.html" else ("0.9" if page == "pricing.html" else "0.8")
        sitemap_xml += f'  <url>\n    <loc>{BASE_URL}/{page}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
    
    sitemap_xml += '</urlset>'
    scrivi_file("sitemap.xml", sitemap_xml)
    
    robots_txt = f"User-agent: *\nAllow: /\nDisallow: /success.html\nDisallow: /cheatsheet_ob.html\nDisallow: /cheatsheet_risk.html\n\nSitemap: {BASE_URL}/sitemap.xml\n"
    scrivi_file("robots.txt", robots_txt)
    logger.info("Motore SEO generato con successo.")