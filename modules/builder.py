import os
import json
import datetime
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import get_header, get_footer, MODALS_HTML

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

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE I: QUANTITATIVE PSYCHOLOGY", 
        "lessons": [
            {
                "id": "lez1_1", 
                "title": "1.1 Institutional Mindset", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px; font-weight:900;">The 1% Statistical Edge</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Retail market participants systematically lose capital due to emotional execution. At Market Insider Pro, we eliminate discretionary bias. We execute purely on quantitative probabilities.</p>
                <div style='margin-top:40px; padding:30px; background:#111; border-left:4px solid #FFD700; border-radius:4px;'>
                    <h3 style="color:#FFD700; margin-top:0;">Mandatory Literature</h3>
                    <p style="color:#ccc;">To align with institutional standards, "Trading in the Zone" by Mark Douglas is required reading for risk management conditioning.</p>
                    <a href='{AMAZON_LINK_BOOK}' target='_blank' class='vip-btn' style='background: #FFD700; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>ACQUIRE RESOURCE</a>
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
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px; font-weight:900;">Price Action & Volume Distribution</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Discard lagging indicators. Institutional algorithms track only raw volume nodes and liquidity sweeps.</p>
                <div style='margin-top:40px; padding:30px; background:#111; border-left:4px solid #555; border-radius:4px;'>
                    <h3 style="color:#fff; margin-top:0;">Hardware Specifications</h3>
                    <p style="color:#ccc;">Multi-timeframe analysis requires significant screen real estate. An ultrawide display is standard protocol.</p>
                    <a href='{AMAZON_LINK_MONITOR}' target='_blank' class='btn-trade' style='display:inline-block; margin-top:10px;'>HARDWARE UPGRADE</a>
                </div>
                <div style='margin-top:20px; padding:30px; background:#111; border-left:4px solid #FCD535; border-radius:4px;'>
                    <h3 style="color:#FCD535; margin-top:0;">Execution Venue</h3>
                    <p style="color:#ccc;">Zero-slippage execution is mandatory. Connect to top-tier liquidity pools.</p>
                    <a href='{BINANCE_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background:#FCD535; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>ACCESS BINANCE POOL</a>
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
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px; font-weight:900;">Identifying Accumulation Nodes</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Order Blocks (OBs) represent massive capital deployment by central entities. We trace these footprints to model predictive entries.</p>
                <div style='margin-top:40px; padding:30px; background:#111; border-left:4px solid #00C853; border-radius:4px;'>
                    <h3 style="color:#00C853; margin-top:0;">Asset Custody Protocol</h3>
                    <p style="color:#ccc;">Long-term capital must remain disconnected from network attack vectors. Cold storage is strictly enforced.</p>
                    <a href='{AMAZON_LINK_LEDGER}' target='_blank' class='vip-btn' style='background:#00C853; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>SECURE HARDWARE</a>
                </div>
                '''
            }
        ]
    }
}

# DATABASE ASSET 100% REALI (SOLO CRYPTO)
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
        logger.info(f" Generato: {nome_file}")
    except IOError as e: 
        logger.error(f" Errore scrittura: {e}")

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
            <span class="star-icon" id="star-{elem_id}" onclick="toggleStar('{elem_id}')" style="font-size:12px;">[+]</span>
            <a href="chart_{elem_id}.html" class="card-link" style="display:block; height:100%;">
                <div class="card" style="border-radius:4px;">
                    <div class="card-head">
                        <span class="symbol" style="font-weight:900;">{ticker}</span>
                        <span class="name" style="color:#666; font-size:0.75rem; text-transform:uppercase;">{db_info['name']}</span>
                    </div>
                    <div class="price" id="price-{elem_id}" style="font-family:monospace; font-size:1.6rem;">{format_price(d_asset["price"])}</div>
                    <div class="change {color}" id="change-{elem_id}" style="font-family:monospace;">{( "+" if d_asset["change"] >= 0 else "" )}{d_asset["change"]}%</div>
                    <div class="signal-box" style="border-top:1px solid #222; padding-top:10px; margin-top:10px;">
                        <span style="font-size:0.7rem; color:#555;">ALGO BIAS:</span>
                        <strong style="color:{d_asset["sig_col"]}; font-size:0.8rem;">{d_asset["signal"]}</strong>
                    </div>
                </div>
            </a>
        </div>
        '''
        
        chart_page = get_header("home") + f'''
        <main class="container">
            <a href="index.html" style="color:#888; text-decoration:none; display:inline-block; margin: 15px 0; font-size: 0.8rem; letter-spacing: 1px; border:1px solid #333; padding:5px 10px;">RETURN TO TERMINAL</a>
            <h1 style="margin:0 0 20px 0; font-size: 2rem; font-weight:900;">{db_info['name']} <span style="color:var(--accent);">DATA</span></h1>
            <div class="tradingview-widget-container" style="height:100%;width:100%; border:1px solid #222; border-radius:4px; overflow:hidden;">
                <div id="tv_{elem_id}" style="height:650px;width:100%"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({{ "autosize": true, "symbol": "{db_info['symbol']}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "studies": ["RSI@tv-basicstudies", "Volume@tv-basicstudies"], "container_id": "tv_{elem_id}" }});
                </script>
            </div>
        </main>
        ''' + MODALS_HTML + get_footer()
        scrivi_file(f"chart_{elem_id}.html", chart_page)

    fng_color = "#FF3D00" if fng['value'] < 40 else ("#00C853" if fng['value'] > 60 else "#FFD700")
    fng_html = f'''
    <div class="fng-meter" style="border-radius:4px; border:1px solid #222;">
        <h3 style="margin:0; color:#888; text-transform:uppercase; font-size:0.8rem; font-weight:700;">MACRO SENTIMENT INDEX</h3>
        <div class="fng-value" style="color:{fng_color}; font-family:monospace;">{fng["value"]}</div>
        <div style="font-weight:bold; letter-spacing:1px; color:#ccc;">{fng["text"]}</div>
        <div class="fng-bar" style="border-radius:2px;"><div class="fng-indicator" style="left: {fng["value"]}%; width:4px; border-radius:0;"></div></div>
    </div>
    '''
    
    filter_html = '''
    <div class="market-filters" style="margin-bottom: 30px; display: flex; gap: 15px; align-items:center;">
        <input type="text" id="asset-search" placeholder="Query ticker (e.g. BTC, SOL)..." onkeyup="filterAssets()" style="padding: 12px 20px; background: #0a0a0a; border: 1px solid #333; color: #fff; width: 100%; max-width: 350px; border-radius: 4px; outline:none; font-family:monospace;">
    </div>
    <script>
    function filterAssets() {
        let search = document.getElementById('asset-search').value.toLowerCase();
        let cards = document.querySelectorAll('.card-wrapper');
        cards.forEach(c => {
            let id = c.getAttribute('data-id');
            if (id.includes(search) || c.innerText.toLowerCase().includes(search)) { c.style.display = 'block'; } else { c.style.display = 'none'; }
        });
    }
    </script>
    '''
    
    watchlist_script = '''
    <script>
    const WL_KEY = "mip_watchlist_v1"; 
    function toggleStar(id) { 
        let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); 
        if(wl.includes(id)) { wl = wl.filter(x => x !== id); } else { wl.push(id); } 
        localStorage.setItem(WL_KEY, JSON.stringify(wl)); sortGrid(); 
    } 
    function sortGrid() { 
        let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); 
        let grid = document.getElementById("markets-grid"); 
        let cards = Array.from(grid.children); 
        cards.forEach(c => { 
            let id = c.getAttribute("data-id"); 
            let star = document.getElementById("star-"+id); 
            if(wl.includes(id)) { star.style.color = "var(--gold)"; } else { star.style.color = "#444"; } 
        }); 
        cards.sort((a, b) => { let aStar = wl.includes(a.getAttribute("data-id")) ? 1 : 0; let bStar = wl.includes(b.getAttribute("data-id")) ? 1 : 0; return bStar - aStar; }); 
        cards.forEach(c => grid.appendChild(c)); 
    } 
    document.addEventListener("DOMContentLoaded", sortGrid);
    </script>
    '''
    
    news_rows = "".join([f'''<tr style="border-bottom: 1px solid #222;"><td style="padding:15px 10px;"><a href="{n["link"]}" target="_blank" style="font-weight:600; color:#ddd; display:block; margin-bottom:5px; text-decoration:none;">{n["title"]}</a><span style="font-size:0.7rem; color:#666; text-transform:uppercase;">SOURCE: {n["source"]}</span></td><td style="text-align:right;"><a href="{n["link"]}" target="_blank" class="btn-trade" style="background:transparent; color:#888; border:1px solid #444; padding:5px 10px; font-size:0.7rem;">ACCESS</a></td></tr>''' for n in news])
    
    ticker_css = '''
    <style>
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-50%, 0, 0); } } 
    .ticker-wrap { width: 100%; overflow: hidden; background-color: #050505; border-bottom: 1px solid #222; padding: 6px 0; } 
    .ticker { display: inline-block; white-space: nowrap; padding-right: 100%; box-sizing: content-box; animation: ticker 40s linear infinite; font-family: monospace; font-size: 0.8rem; color: #aaa; text-transform:uppercase; } 
    .ticker-item { display: inline-block; padding: 0 2rem; border-right:1px solid #333; } 
    .market-clocks { display: flex; justify-content: space-between; flex-wrap:wrap; gap:10px; background: #0a0a0a; padding: 15px; border-radius: 4px; border: 1px solid #222; margin-bottom: 20px; font-family: monospace; color: #666; } 
    .clock { text-align: center; flex:1; min-width:120px; border-right: 1px solid #222;} 
    .clock:last-child { border:none; } 
    .clock span { display: block; font-size: 1.2rem; color: #ccc; font-weight: normal; margin-top: 5px; letter-spacing:1px; }
    </style>
    '''
    
    ticker_html = f'''<div class="ticker-wrap"><div class="ticker"><div class="ticker-item"><span style="color:#00C853;">[LIQUIDITY]</span> 1,240 BTC outflow from Binance confirmed</div><div class="ticker-item"><span style="color:#FF3D00;">[DERIVATIVES]</span> $4.2M wiped on ETH perpetuals</div><div class="ticker-item"><span style="color:var(--gold);">[MACRO]</span> US CPI aligns with consensus</div><div class="ticker-item"><span style="color:#2962FF;">[ON-CHAIN]</span> Major accumulation spotted on SOL</div><div class="ticker-item"><span style="color:#00C853;">[LIQUIDITY]</span> 1,240 BTC outflow from Binance confirmed</div><div class="ticker-item"><span style="color:#FF3D00;">[DERIVATIVES]</span> $4.2M wiped on ETH perpetuals</div></div></div>'''
    clocks_html = '''<div class="market-clocks"><div class="clock">NY (NYSE) <span id="clock-ny">--:--</span></div><div class="clock">LON (LSE) <span id="clock-lon">--:--</span></div><div class="clock">TOK (TSE) <span id="clock-tok">--:--</span></div><div class="clock">NETWORK STATUS <span style="color:#00C853;">ONLINE</span></div></div><script>function updateClocks() { let d = new Date(); document.getElementById("clock-ny").innerText = d.toLocaleTimeString("en-US", {timeZone: "America/New_York", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); document.getElementById("clock-lon").innerText = d.toLocaleTimeString("en-US", {timeZone: "Europe/London", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); document.getElementById("clock-tok").innerText = d.toLocaleTimeString("en-US", {timeZone: "Asia/Tokyo", hour12: false, hour: "2-digit", minute: "2-digit", second:"2-digit"}); } setInterval(updateClocks, 1000); updateClocks();</script>'''

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Market Insider Pro | Terminal</title>{CSS_CORE}{ticker_css}</head><body>{get_header('home')}{ticker_html}<div class="container">{clocks_html}<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;"><h2 class="section-title" style="margin:0; font-size:1.5rem;">GLOBAL MACRO DATA</h2><div style="font-size:0.7rem; color:#00C853; font-family:monospace; border:1px solid #00C853; padding:2px 6px; border-radius:2px;">REAL-TIME CONNECTION</div></div>{filter_html}<div class="grid" id="markets-grid">{grid_html}</div><div class="split-layout"><div class="panel" style="border-radius:4px;">{fng_html}</div><div class="panel" style="border-radius:4px;"><h2 class="section-title" style="font-size:1.2rem;">MARKET INTELLIGENCE</h2><table style="width:100%;"><tbody>{news_rows}</tbody></table></div></div></div>{MODALS_HTML} {get_footer()} {watchlist_script}</body></html>'''
    scrivi_file("index.html", html)

def build_signals_page(assets: List[Dict]):
    hot_assets = [a for a in assets if abs(a['change']) >= 1.0][:10]
    rows = ""
    for a in hot_assets:
        p = a["price"]
        c = a["change"]
        vol_mult = abs(c) / 100
        if c > 0: sig, css, sl, tp1, tp2 = "LONG BIAS", "signal-buy", p * (1 - (vol_mult * 1.5)), p * (1 + (vol_mult * 2.0)), p * (1 + (vol_mult * 4.0))
        else: sig, css, sl, tp1, tp2 = "SHORT BIAS", "signal-sell", p * (1 + (vol_mult * 1.5)), p * (1 - (vol_mult * 2.0)), p * (1 - (vol_mult * 4.0))
        rows += f'''<tr style="border-bottom: 1px solid #222;"><td style="padding:15px;"><strong style="font-size:1.1rem; color:#fff;">{a["symbol"]}</strong><br><span style="font-size:0.7rem;color:#666;">{a["name"]}</span></td><td style="padding:15px; font-weight:bold; font-size:0.9rem;" class="{css}">{sig}</td><td style="padding:15px; font-family:monospace;"><div style="font-size:0.65rem; color:#666;">ENTRY</div><strong style="color:#ccc;">{format_price(p)}</strong></td><td style="padding:15px; font-family:monospace;"><div style="font-size:0.65rem; color:#666;">TARGET</div><strong style="color:var(--gold);">{format_price(tp1)}</strong></td><td style="padding:15px; font-family:monospace;"><div style="font-size:0.65rem; color:#666;">INVALIDATION</div><strong style="color:#FF3D00;">{format_price(sl)}</strong></td><td style="padding:15px; text-align:right;"><a href="chart_{a["id"]}.html" class="btn-trade" style="padding: 8px 15px; font-size:0.8rem; background:transparent; border:1px solid #555; color:#aaa;">DATA</a></td></tr>'''

    risk_manager_html = '''<div class="panel" style="margin-bottom:30px; border-left:4px solid var(--accent); background: #0a0a0a; border-radius:4px;"><h3 style="margin-top:0; color:#fff; font-size:1.2rem;">QUANTITATIVE RISK MODEL</h3><p style="color:#888; font-size:0.85rem;">Calculate exact position exposure based on strict institutional tolerance algorithms.</p><div class="wallet-form" style="padding:0; background:none; border:none; flex-wrap:wrap; gap:15px; margin-bottom:0;"><div style="flex:1; min-width:150px;"><label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Capital ($)</label><input type="number" id="rm-balance" value="10000" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #333; color:#fff; font-family:monospace;"></div><div style="flex:1; min-width:150px;"><label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Risk Exposure (%)</label><input type="number" id="rm-risk" value="1" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #333; color:#fff; font-family:monospace;"></div><div style="flex:1; min-width:150px;"><label style="font-size:0.7rem; color:#666; text-transform:uppercase;">Invalidation Dist. (%)</label><input type="number" id="rm-sl" value="2.5" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px; background:#000; border:1px solid #333; color:#fff; font-family:monospace;"></div><div style="display:flex; align-items:flex-end;"><button class="btn-trade" onclick="calcRisk()" style="padding:12px 24px; height:42px;">CALCULATE</button></div></div><div id="rm-result" style="display:none; margin-top:20px; padding:15px; background:#000; border-radius:4px; border:1px solid #222;"><span style="color:#666; text-transform:uppercase; font-size:0.75rem;">Optimal Allocation Size:</span> <strong id="rm-size" style="color:var(--gold); font-size:1.3rem; margin-left:10px; font-family:monospace;">$0</strong></div></div><script>function calcRisk() { let bal = parseFloat(document.getElementById('rm-balance').value); let risk = parseFloat(document.getElementById('rm-risk').value); let sl = parseFloat(document.getElementById('rm-sl').value); if(bal>0 && risk>0 && sl>0) { let riskAmt = bal * (risk/100); let posSize = riskAmt / (sl/100); document.getElementById('rm-result').style.display = 'flex'; document.getElementById('rm-result').style.alignItems = 'center'; document.getElementById('rm-size').innerText = '$' + posSize.toLocaleString('en-US', {maximumFractionDigits:2}); } }</script>'''

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Signals Engine</title>{CSS_CORE}</head><body>{get_header('signals')}<div class="container">{risk_manager_html}<div style="border: 1px solid #333; padding: 15px; border-radius: 4px; margin-bottom: 30px; text-align: center; background:#050505;"><strong style="color: #FF3D00; font-size:0.8rem; letter-spacing:1px;">SYSTEM ADVISORY:</strong> <span style="color: #888; font-size: 0.8rem;">Algorithmic targets are generated based on mathematical variance (ATR). Do not execute discretionary trades blindly.</span></div><h2 class="section-title" style="font-size:1.5rem;">QUANTITATIVE SIGNALS ENGINE</h2><div class="panel" style="padding:0; overflow-x:auto; border-radius:4px;"><table style="width:100%;"><thead><tr style="background:#0a0a0a; font-size:0.8rem; color:#666;"><th style="padding:15px;">ASSET</th><th>ALGO SIGNAL</th><th>ENTRY</th><th>TARGET ZONES</th><th>INVALIDATION</th><th style="text-align:right; padding-right:15px;">DATA</th></tr></thead><tbody>{rows}</tbody></table></div></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("signals.html", html)

def build_api_hub():
    js_script = '''<script>function connectAPI() { document.getElementById('api-form-container').style.display = 'none'; document.getElementById('term').style.display = 'block'; document.getElementById('term-input').focus(); } function checkTerminalCommand(e) { if(e.key === 'Enter') { let val = e.target.value.trim().toLowerCase(); let term = document.getElementById('term-content'); if(val === 'connect') { e.target.value = ''; e.target.disabled = true; term.innerHTML += "><span style='color:#ccc;'> connect</span><br>> Establishing secure bridge...<br>"; setTimeout(() => { term.innerHTML += "> Encrypting payload (AES-256)... <span style='color:#00C853;'>OK</span><br>"; }, 800); setTimeout(() => { term.innerHTML += "> Requesting API permissions...<br>"; }, 1800); setTimeout(() => { term.innerHTML += "<span style='color:var(--red); font-weight:bold;'>[!] EXECUTION REJECTED: TIER NOT AUTHORIZED</span><br>"; openWaitlist(); e.target.disabled = false; }, 3200); } else { term.innerHTML += "><span style='color:#ccc;'> " + val + "</span><br>> Command void. Type '<span style='color:#ccc;'>connect</span>'.<br>"; e.target.value = ''; } let termDiv = document.getElementById('term'); termDiv.scrollTop = termDiv.scrollHeight; } }</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>API Execution Hub</title>{CSS_CORE}</head><body>{get_header('api')}<div class="container" style="max-width:800px;"><div style="text-align:center; margin-bottom:40px;"><h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900;">EXECUTION HUB</h1><p style="color:#888; font-size:1rem;">Bridge exchange infrastructures to deploy automated strategy logic.</p></div><div class="panel" style="padding:40px; border-radius:4px;"><div id="api-form-container" class="wallet-form" style="background:none; border:none; padding:0; flex-direction:column; gap:20px;"><div><label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold;">Protocol</label><select style="width:100%; margin-top:5px; padding:15px; background:#000; border:1px solid #333; color:#ccc; outline:none;"><option>Binance FIX/REST API</option><option>Bybit Linear API</option><option>MEXC v3 API</option></select></div><div><label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold;">Public Key</label><input type="text" style="width:96%; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #333; color:#ccc; outline:none;" placeholder="Enter Public Key"></div><div><label style="color:#666; font-size:0.75rem; text-transform:uppercase; font-weight:bold;">Private Key</label><input type="password" style="width:96%; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #333; color:#ccc; outline:none;" placeholder="Enter Private Key"></div><button class="btn-trade" style="padding:15px; font-size:1rem; margin-top:10px; letter-spacing:1px;" onclick="connectAPI()">INITIALIZE CONNECTION</button></div><div class="hacker-terminal" id="term" style="display:none; cursor:text; height:250px; background:#050505; border:1px solid #222; border-radius:4px; padding:20px; font-family:monospace; color:#888; font-size:0.9rem;" onclick="document.getElementById('term-input').focus()"><div id="term-content">> SYSTEM READY.<br>> Awaiting execution... (Type 'connect')<br></div><div style="display:flex;">> <input type="text" id="term-input" onkeypress="checkTerminalCommand(event)" style="background:transparent; border:none; color:#ccc; font-family:monospace; outline:none; width:100%; margin-left:5px; font-size:0.9rem;" autocomplete="off" spellcheck="false"></div></div></div></div>{js_script}{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("api_hub.html", html)

def build_brokers_page():
    brokers = [
        {"name": "Binance", "type": "Spot & Derivatives", "pros": "Deepest Liquidity Depth", "link": BINANCE_AFFILIATE_LINK, "cta": "PROVISION ACCOUNT"},
        {"name": "Bybit", "type": "Perpetual Futures", "pros": "Low Latency API", "link": BYBIT_AFFILIATE_LINK, "cta": "PROVISION ACCOUNT"},
        {"name": "MEXC", "type": "High Leverage", "pros": "0% Maker Fees", "link": AFF_MEXC, "cta": "PROVISION ACCOUNT"}
    ]
    html_cards = "".join([f'<div class="broker-card" style="border-radius:4px; border:1px solid #222; background:#0a0a0a;"><div style="display:flex; align-items:center;"><div class="broker-info"><h3 style="margin:0; color:#fff; font-size:1.2rem;">{b["name"]}</h3><div class="broker-tags" style="margin-top:8px;"><span style="background:#111; color:#888; border:1px solid #333;">{b["type"]}</span><span style="background:#111; color:#888; border:1px solid #333;">{b["pros"]}</span></div></div></div><a href="{b["link"]}" target="_blank" class="btn-trade" style="padding:10px 20px; text-align:center; font-size:0.85rem; border-radius:2px;">{b["cta"]}</a></div>' for b in brokers])
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Partner Exchanges</title>{CSS_CORE}</head><body>{get_header('brokers')}<div class="container"><div style="text-align:center; margin-bottom:50px;"><h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900;">SUPPORTED VENUES</h1><p style="color:#888; font-size:1rem; max-width:600px; margin:0 auto;">Certified exchange infrastructures for algorithmic deployment and secure custody.</p></div><div style="max-width:800px; margin:0 auto;">{html_cards}</div></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("brokers.html", html)

def build_referral_page():
    js = '''<script>document.addEventListener("DOMContentLoaded", function() { let user = localStorage.getItem('mip_user') || 'profile_' + Math.floor(Math.random()*1000); let link = `https://marketinsiderpro.com/invite/${user.toLowerCase()}`; document.getElementById('ref-url').innerText = link; }); function copyLink() { navigator.clipboard.writeText(document.getElementById('ref-url').innerText); let btn = document.getElementById('copy-btn'); btn.innerText = "COPIED"; btn.style.background = "#00C853"; btn.style.color = "#000"; setTimeout(() => { btn.innerText = "COPY LINK"; btn.style.background = "var(--accent)"; btn.style.color = "#fff"; }, 2000); }</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Referral Network</title>{CSS_CORE}</head><body>{get_header('referral')}<div class="container" style="max-width:800px;"><div class="ref-box" style="border-radius:4px; border:1px solid #333; background:#0a0a0a; padding:50px;"><h1 style="font-size:2rem; margin-top:0; color:#fff; font-weight:900;">NETWORK EXPANSION</h1><p style="color:#888; font-size:1rem; line-height:1.6;">Distribute your unique cryptographic identifier. Upon 3 successful network additions, Tier 2 (VIP) clearance is granted automatically.</p><div class="ref-link-container" style="background:#000; border:1px solid #222; border-radius:4px;"><div class="ref-link" id="ref-url" style="color:#ccc; font-family:monospace; font-size:0.9rem;">Loading link...</div><button class="ref-copy" id="copy-btn" onclick="copyLink()" style="border-radius:2px; font-weight:bold; letter-spacing:1px;">COPY LINK</button></div></div></div>{MODALS_HTML} {get_footer()} {js}</body></html>'''
    scrivi_file("referral.html", html)

def build_pricing_page():
    checkout_modal_html = '''<div class="modal-overlay" id="checkout-choice-modal"><div class="modal-content" style="max-width:450px; text-align:center; padding:40px; border-radius:4px; border:1px solid #333;"><span class="close-modal" onclick="document.getElementById('checkout-choice-modal').style.display='none'">&times;</span><h2 style="color:#fff; margin-top:0; font-weight:900;">Authentication Check</h2><p style="color:#888; font-size:0.9rem; margin-bottom:30px;">Select pathway to provision your Tier.</p><div style="display:flex; flex-direction:column; gap:15px;"><button class="vip-btn" style="padding:15px; width:100%; border-radius:2px; font-weight:bold; letter-spacing:1px;" onclick="proceedToStripe('login')">AUTHENTICATE FIRST</button><button class="btn-trade" style="padding:15px; width:100%; background:#050505; border:1px solid #333; color:#aaa; border-radius:2px; font-weight:bold; letter-spacing:1px;" onclick="proceedToStripe('guest')">PROCEED AS GUEST</button></div></div></div><script>let currentStripeLink = ""; function openCheckoutChoice(link) { currentStripeLink = link; let user = localStorage.getItem('mip_user'); if(user) { window.location.href = currentStripeLink; } else { document.getElementById('checkout-choice-modal').style.display = 'flex'; } } function proceedToStripe(method) { if(method === 'guest') { window.location.href = currentStripeLink; } else if(method === 'login') { document.getElementById('checkout-choice-modal').style.display = 'none'; openLogin(); } }</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Pricing</title>{CSS_CORE}</head><body>{get_header('pricing')}<div class="container"><div style="text-align:center; margin-bottom:40px;"><h1 style="font-size:3rem; margin-bottom:10px; font-weight:900;">INSTITUTIONAL ACCESS</h1><p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Upgrade data infrastructure. Access unmetered algorithmic feeds and strictly professional analytical models.</p></div><div class="pricing-grid"><div class="pricing-card" style="border-radius:4px; background:#0a0a0a;"><h3 style="color:#888; font-size:1.2rem; margin:0; letter-spacing:1px;">TIER 1 (STANDARD)</h3><div class="price-tag" style="color:#ccc;">$0<span style="color:#666;">/mo</span></div><div style="margin-bottom:30px; font-size:0.9rem; color:#888;"><div class="plan-feature" style="border-color:#222;">Delayed Terminal Data</div><div class="plan-feature" style="border-color:#222;">Basic Modeling</div><div class="plan-feature" style="border-color:#222;">Academy Core</div></div><button class="vip-btn" style="width:100%; background:#222; color:#888; border-radius:2px; cursor:default;">CURRENT TIER</button></div><div class="pricing-card pro" style="border-radius:4px; border:1px solid var(--gold); background:#111;"><h3 style="color:var(--gold); font-size:1.2rem; margin:0; letter-spacing:1px;">TIER 2 (QUANT)</h3><div class="price-tag" style="color:#fff;">$49<span style="color:#888;">/mo</span></div><div style="margin-bottom:30px; font-size:0.9rem;"><div class="plan-feature" style="color:#ccc; border-color:#222;">Real-Time Data Feeds</div><div class="plan-feature" style="color:#ccc; border-color:#222;">Advanced Academy Access</div><div class="plan-feature" style="color:#ccc; border-color:#222;">Signals Database</div><div class="plan-feature" style="color:#ccc; border-color:#222;">Portfolio Aggregator</div></div><button class="btn-trade checkout-btn" onclick="openCheckoutChoice('https://buy.stripe.com/dRmcN56uTbIR6N8fux2Ry00')" style="width:100%; padding:15px; font-size:1rem; border-radius:2px; letter-spacing:1px; background:var(--gold); color:#000;">PROVISION SECURELY</button></div><div class="pricing-card" style="border-radius:4px; background:#0a0a0a;"><h3 style="color:#2962FF; font-size:1.2rem; margin:0; letter-spacing:1px;">ENTERPRISE (LIFETIME)</h3><div class="price-tag" style="color:#fff;">$399<span style="color:#888;">/once</span></div><div style="margin-bottom:30px; font-size:0.9rem; color:#ccc;"><div class="plan-feature" style="border-color:#222;">All Tier 2 Features</div><div class="plan-feature" style="border-color:#222;">Private Network Access</div><div class="plan-feature" style="border-color:#222;">Perpetual Updates</div></div><button class="vip-btn checkout-btn" onclick="openCheckoutChoice('https://buy.stripe.com/14AfZh6uT9AJ3AW5TX2Ry01')" style="width:100%; padding:15px; border-radius:2px; letter-spacing:1px;">ACQUIRE LICENSE</button></div></div></div>{checkout_modal_html}{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("pricing.html", html)

def build_leaderboard_page():
    js = '''<script>document.addEventListener("DOMContentLoaded", function() { let user = localStorage.getItem('mip_user'); if(user) { document.getElementById('lb-body').innerHTML += `<tr class="user-row" style="background:#111;"><td class="rank-3">#8</td><td><strong style="color:#fff;">[YOU] ${user}</strong></td><td style="font-family:monospace;">$14,250</td><td class="change green" style="font-family:monospace;">+18.4%</td><td>Tier 2</td></tr>`; } });</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Leaderboard</title>{CSS_CORE}</head><body>{get_header('leaderboard')}<div class="container"><div style="text-align:center; margin-bottom:40px;"><h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900;">GLOBAL METRICS</h1><p style="color:#888; font-size:1rem; max-width:600px; margin:0 auto;">Statistical ranking of top network profiles by realized equity curve.</p></div><div class="panel" style="max-width:900px; margin:0 auto; padding:0; border-radius:4px; overflow:hidden;"><table><thead><tr style="background:#050505; border-bottom:1px solid #333; font-size:0.8rem; color:#666;"><th style="padding:15px;">RANK</th><th>IDENTIFIER</th><th>CAPITAL DEPLOYED</th><th>30D YIELD</th><th>TIER</th></tr></thead><tbody id="lb-body"><tr style="border-bottom:1px solid #222;"><td class="rank-1" style="padding:15px; color:#fff; font-weight:bold;">#1</td><td><strong style="color:#ddd;">Entity_99</strong></td><td style="font-family:monospace; color:#aaa;">$1.2M</td><td class="change green" style="font-family:monospace;">+142.5%</td><td><span style="color:var(--gold); font-size:0.8rem; border:1px solid var(--gold); padding:2px 6px; border-radius:2px;">WHALE</span></td></tr><tr style="border-bottom:1px solid #222;"><td class="rank-2" style="padding:15px; color:#fff; font-weight:bold;">#2</td><td><strong style="color:#ddd;">Quant_LDN</strong></td><td style="font-family:monospace; color:#aaa;">$450K</td><td class="change green" style="font-family:monospace;">+89.2%</td><td><span style="color:#888; font-size:0.8rem;">Tier 2</span></td></tr><tr style="border-bottom:1px solid #222;"><td class="rank-3" style="padding:15px; color:#fff; font-weight:bold;">#3</td><td><strong style="color:#ddd;">CapitalX</strong></td><td style="font-family:monospace; color:#aaa;">$89K</td><td class="change green" style="font-family:monospace;">+64.8%</td><td><span style="color:#888; font-size:0.8rem;">Tier 2</span></td></tr></tbody></table></div></div>{MODALS_HTML} {get_footer()} {js}</body></html>'''
    scrivi_file("leaderboard.html", html)

def build_legal_page():
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Legal</title>{CSS_CORE}</head><body>{get_header('legal')}<div class="container" style="max-width:800px; color:#ccc;"><h1 style="color:#fff;">Compliance & Policies</h1><hr style="border-color:#333; margin-bottom:30px;"><h3 style="color:var(--accent);">Data Policy</h3><p>Market Insider Pro utilizes client-side storage to minimize server dependency and enhance security. No identifiable data is harvested without consent.</p><h3 style="color:var(--accent);">Terms of Operation</h3><p>Platform access is contingent on adherence to network rules. Content is analytical, not advisory.</p></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("legal.html", html)

def build_chart_pages(assets: List[Dict]):
    pass

def build_academy():
    sidebar = "".join([f"<div class='module-title' style='color:#666; font-size:0.75rem; letter-spacing:1px;'>{m['title']}</div>" + "".join([f'''<div onclick="window.location.href='academy_{l['id']}.html'" class="lesson-link" style="border-left:2px solid transparent;">{"[RESTRICTED]" if l.get("vip") else "[OPEN]"} {l['title']}</div>''' for l in m['lessons']]) for _, m in ACADEMY_CONTENT.items()])
    
    for _, m in ACADEMY_CONTENT.items():
        for l in m['lessons']:
            if l.get("vip"):
                c_html = f'''<div id="vip-content" style="filter: blur(12px); pointer-events: none; user-select: none; transition: 0.5s;">{l['html']}</div><div id="vip-lock" style="position:absolute; top:40%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#050505; padding:40px; border:1px solid #333; border-radius:4px; z-index:10; width:90%; max-width:400px; box-shadow:0 20px 40px rgba(0,0,0,0.9);"><div style="width:50px; height:50px; border:2px solid #FF3D00; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto; color:#FF3D00; font-weight:bold;">!</div><h2 style="color:#fff; margin-top:0; font-weight:900;">RESTRICTED DATA</h2><p style="color:#888; margin-bottom:30px; font-size:0.9rem;">Protocol requires Tier 2 (VIP) clearance.</p><a href="pricing.html" class="btn-trade" style="display:block; padding:15px; border-radius:2px; letter-spacing:1px;">AUTHENTICATE CLEARANCE</a></div><script>document.addEventListener("DOMContentLoaded", function() {{ if(localStorage.getItem('mip_vip_status') === 'active') {{ document.getElementById('vip-content').style.filter = 'none'; document.getElementById('vip-content').style.pointerEvents = 'auto'; document.getElementById('vip-content').style.userSelect = 'auto'; document.getElementById('vip-lock').style.display = 'none'; }} }});</script>'''
            else:
                c_html = l['html']
                
            html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{l['title']}</title>{CSS_CORE}</head><body>{get_header('academy')}<div class="container"><div class="academy-grid" style="gap:40px;"><div class="sidebar" style="background:#0a0a0a; border:1px solid #222; border-radius:4px; padding:20px;">{sidebar}</div><div class="lesson-content" style="position:relative; background:#0a0a0a; padding:40px; border-radius:4px; border:1px solid #222;">{c_html}</div></div></div>{MODALS_HTML}{get_footer()}</body></html>'''
            scrivi_file(f"academy_{l['id']}.html", html)

# LA VERA DASHBOARD VIP DA HEDGE FUND (Sostituisce il vecchio VIP Lounge)
def build_vip_lounge():
    build_cheatsheets() 
    lounge_html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Tier 2 Dashboard</title>
        {CSS_CORE}
        <style>
        .hedge-panel {{ background: #050505; border: 1px solid #222; border-radius: 4px; padding: 25px; }}
        .hedge-title {{ color: #fff; font-size: 1rem; font-weight: 900; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid #222; padding-bottom: 10px; margin-top: 0; margin-bottom: 20px; }}
        .data-row {{ display: flex; justify-content: space-between; border-bottom: 1px solid #111; padding: 10px 0; font-family: monospace; font-size: 0.9rem; }}
        .data-row:last-child {{ border: none; }}
        .val-pos {{ color: #00C853; }}
        .val-neg {{ color: #FF3D00; }}
        .val-neu {{ color: #888; }}
        
        .ticker-scroller {{ height: 150px; overflow: hidden; position: relative; background: #000; border: 1px solid #111; padding: 10px; font-family: monospace; font-size: 0.8rem; color: #666; }}
        .ticker-scroller-inner {{ animation: scrollUp 20s linear infinite; }}
        .ticker-line {{ padding: 5px 0; border-bottom: 1px solid #0a0a0a; }}
        @keyframes scrollUp {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-50%); }} }}
        </style>
    </head>
    <body>
        {get_header('vip')}
        <div class="container" style="position:relative; max-width: 1200px;">
            
            <div id="vip-content" style="filter: blur(12px); pointer-events: none; user-select: none; transition: 0.5s;">
                <div style="margin-bottom:40px; border-bottom: 1px solid #222; padding-bottom: 20px;">
                    <div style="font-size:0.75rem; color:var(--gold); letter-spacing:2px; font-weight:bold; margin-bottom:5px;">■ TIER 2 CLEARANCE ACTIVE</div>
                    <h1 style="font-size:2.5rem; margin:0; font-weight:900; color:#fff;">QUANTITATIVE COMMAND CENTER</h1>
                </div>
                
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-bottom: 20px;">
                    
                    <div class="hedge-panel">
                        <h3 class="hedge-title">Macro Correlation Matrix</h3>
                        <div class="data-row"><span>BTC / SPX500 (30D)</span><span class="val-pos">+ 0.82</span></div>
                        <div class="data-row"><span>BTC / DXY (30D)</span><span class="val-neg">- 0.75</span></div>
                        <div class="data-row"><span>BTC / GOLD (30D)</span><span class="val-neu">+ 0.12</span></div>
                        <div class="data-row"><span>ETH / SOL (7D)</span><span class="val-pos">+ 0.65</span></div>
                        <div class="data-row"><span>US10Y Yield Variance</span><span class="val-neg">- 0.04 bps</span></div>
                    </div>
                    
                    <div class="hedge-panel">
                        <h3 class="hedge-title">Institutional Custody</h3>
                        <div class="data-row"><span style="color:#fff;">Entity</span><span>Reserves (BTC)</span><span>7D Delta</span></div>
                        <div class="data-row"><span>MicroStrategy</span><span>205,000</span><span class="val-pos">+ 850</span></div>
                        <div class="data-row"><span>BlackRock (IBIT)</span><span>195,985</span><span class="val-pos">+ 2,100</span></div>
                        <div class="data-row"><span>Fidelity (FBTC)</span><span>124,000</span><span class="val-pos">+ 1,050</span></div>
                        <div class="data-row"><span>Grayscale (GBTC)</span><span>350,000</span><span class="val-neg">- 4,200</span></div>
                    </div>
                    
                    <div class="hedge-panel">
                        <h3 class="hedge-title">Simulated OTC Block Tape</h3>
                        <div class="ticker-scroller">
                            <div class="ticker-scroller-inner">
                                <div class="ticker-line"><span class="val-pos">BUY</span> 500 BTC @ 64,250 - Venue: Coinbase Prime</div>
                                <div class="ticker-line"><span class="val-neg">SELL</span> 12,000 ETH @ 3,450 - Venue: Binance OTC</div>
                                <div class="ticker-line"><span class="val-pos">BUY</span> 150,000 SOL @ 145.2 - Venue: FalconX</div>
                                <div class="ticker-line"><span class="val-neg">SELL</span> 800 BTC @ 64,100 - Venue: Kraken Custody</div>
                                <div class="ticker-line"><span class="val-pos">BUY</span> 2.5M XRP @ 0.55 - Venue: Wintermute</div>
                                <div class="ticker-line"><span class="val-pos">BUY</span> 500 BTC @ 64,250 - Venue: Coinbase Prime</div>
                                <div class="ticker-line"><span class="val-neg">SELL</span> 12,000 ETH @ 3,450 - Venue: Binance OTC</div>
                                <div class="ticker-line"><span class="val-pos">BUY</span> 150,000 SOL @ 145.2 - Venue: FalconX</div>
                            </div>
                        </div>
                    </div>
                </div>

                <h2 class="section-title" style="margin-top:40px; font-size:1.5rem;">PROPRIETARY ALPHA MODELS (PDF)</h2>
                <div class="grid">
                    <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px;">
                        <h3 style="color:#fff; margin-top:0; font-size:1.1rem;">Order Block Framework</h3>
                        <p style="color:#888; font-size:0.85rem;">The definitive guide to isolating institutional entry nodes.</p>
                        <button class="btn-trade" style="width:100%; margin-top:10px; background:transparent; border:1px solid #555; color:#ccc;" onclick="window.open('cheatsheet_ob.html', '_blank')">ACCESS DOCUMENT</button>
                    </div>
                    <div class="panel" style="background:#0a0a0a; border:1px solid #222; border-radius:4px;">
                        <h3 style="color:#fff; margin-top:0; font-size:1.1rem;">Risk Sizing Algorithm</h3>
                        <p style="color:#888; font-size:0.85rem;">Mathematical models for optimal capital preservation.</p>
                        <button class="btn-trade" style="width:100%; margin-top:10px; background:transparent; border:1px solid #555; color:#ccc;" onclick="window.open('cheatsheet_risk.html', '_blank')">ACCESS DOCUMENT</button>
                    </div>
                </div>
            </div>
            
            <div id="vip-lock" style="position:absolute; top:30%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#050505; padding:50px; border:1px solid #333; border-radius:4px; z-index:10; width:90%; max-width:450px; box-shadow: 0 20px 50px rgba(0,0,0,0.9);">
                <div style="width:50px; height:50px; border:2px solid #FF3D00; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto; color:#FF3D00; font-weight:bold;">!</div>
                <h2 style="color:#fff; margin-top:0; font-weight:900;">RESTRICTED AREA</h2>
                <p style="color:#888; margin-bottom:30px; font-size:0.95rem; line-height:1.6;">The Quantitative Command Center contains proprietary flow data and requires Tier 2 verification.</p>
                <a href="pricing.html" class="vip-btn" style="display:block; padding:15px; text-decoration:none; border-radius:2px; letter-spacing:1px;">INITIATE CLEARANCE</a>
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
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("vip_lounge.html", lounge_html)


# IL NUOVO WALLET (PORTFOLIO AGGREGATOR)
def build_wallet():
    js = '''
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        if(localStorage.getItem('mip_vip_status') === 'active') {
            document.getElementById('vip-aggregator').style.display = 'block';
            document.getElementById('lock-screen').style.display = 'none';
        }
    });

    function simulateSync() {
        let input = document.getElementById('wallet-input').value;
        let btn = document.getElementById('sync-btn');
        if(!input) return alert("System requires input string.");
        
        btn.innerText = "QUERYING NODE...";
        btn.style.opacity = "0.5";
        
        setTimeout(() => {
            btn.innerText = "DATA IMPORTED";
            btn.style.background = "#00C853";
            btn.style.color = "#000";
            document.getElementById('portfolio-stats').style.display = 'grid';
            
            let total = (Math.random() * 80000 + 20000).toFixed(2);
            document.getElementById('val-total').innerText = "$" + Number(total).toLocaleString();
            document.getElementById('val-pnl').innerText = "+" + (Math.random() * 12 + 1).toFixed(2) + "%";
            
            setTimeout(() => { 
                btn.innerText = "SYNC DATA"; 
                btn.style.background = "var(--accent)"; 
                btn.style.color = "#fff";
                btn.style.opacity = "1"; 
                document.getElementById('wallet-input').value = "";
            }, 3000);
        }, 2500);
    }
    </script>
    '''
    
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Portfolio Aggregator</title>
        {CSS_CORE}
        <style>
        .metric-box {{ background:#050505; padding:25px; border:1px solid #222; border-radius:4px; text-align:center; }}
        .metric-title {{ color:#666; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; font-weight:700; }}
        .metric-value {{ font-size:2rem; color:#fff; font-weight:900; font-family:monospace; }}
        </style>
    </head>
    <body>
        {get_header('wallet')}
        <div class="container" style="max-width:1000px;">
            <div style="text-align:center; margin-bottom:40px;">
                <h1 style="font-size:2.5rem; margin-bottom:10px; font-weight:900;">PORTFOLIO ANALYTICS</h1>
                <p style="color:#888; font-size:1rem;">Cross-chain aggregation and risk modeling.</p>
            </div>
            
            <div id="lock-screen" style="text-align:center; padding: 80px 20px; background:#050505; border-radius:4px; border:1px solid #222;">
                <div style="width:40px; height:40px; border:2px solid #555; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 20px auto; color:#555; font-weight:bold;">?</div>
                <h2 style="color:#fff; font-size: 1.8rem; margin-top:0;">RESTRICTED INFRASTRUCTURE</h2>
                <p style="color:#666; font-size: 0.95rem; max-width: 500px; margin: 15px auto;">The API Aggregator calculates real-time drawdown, beta, and exposure across decentralized networks. Tier 2 required.</p>
                <a href="pricing.html" class="vip-btn" style="display:inline-block; margin-top:20px; padding: 12px 30px; text-decoration:none; border-radius:2px; font-size:0.9rem;">UNLOCK MODULE</a>
            </div>

            <div id="vip-aggregator" style="display:none;">
                <div class="panel" style="margin-bottom:30px; background:#0a0a0a; border:1px solid #222; border-radius:4px;">
                    <h3 style="margin-top:0; color:#fff; border-bottom:1px solid #111; padding-bottom:15px; font-size:1rem;">ADD DATA LAYER</h3>
                    <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:20px;">
                        <select style="padding:15px; background:#000; color:#ccc; border:1px solid #333; border-radius:2px; min-width:200px; outline:none;">
                            <option>EVM Network (ETH/BSC)</option>
                            <option>Solana Node</option>
                            <option>Binance Read-Only API</option>
                            <option>Bybit Read-Only API</option>
                        </select>
                        <input type="text" id="wallet-input" placeholder="Paste Public Address or API Key..." style="flex:1; padding:15px; background:#000; color:#fff; border:1px solid #333; border-radius:2px; font-family:monospace; outline:none;">
                        <button id="sync-btn" class="btn-trade" onclick="simulateSync()" style="padding:15px 30px; border-radius:2px; letter-spacing:1px; font-weight:bold;">SYNC</button>
                    </div>
                    <p style="color:#555; font-size:0.75rem; margin-top:15px;">Keys are hashed client-side. Zero server retention.</p>
                </div>

                <div id="portfolio-stats" style="display:none; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:15px; margin-bottom:30px;">
                    <div class="metric-box">
                        <div class="metric-title">Total Capital</div>
                        <div class="metric-value" id="val-total" style="color:var(--gold);">--</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">Realized Yield (30D)</div>
                        <div class="metric-value" id="val-pnl" style="color:#00C853;">--</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">Systematic Beta</div>
                        <div class="metric-value" style="color:#ccc;">0.85</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">Exposure</div>
                        <div class="metric-value" style="font-size:1.2rem; margin-top:10px;">
                            <span style="color:#F7931A;">60% BTC</span> <span style="color:#444;">|</span> <span style="color:#627EEA;">40% ETH</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()} 
        {js}
    </body>
    </html>'''
    scrivi_file("wallet.html", html)


# NUOVA PAGINA TOOLS (INSTITUTIONAL STACK)
def build_tools_page():
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Institutional Stack</title>
        {CSS_CORE}
        <style>
        .stack-category {{ color: #666; font-size: 0.8rem; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; margin-top: 40px; border-bottom: 1px solid #222; padding-bottom: 10px; margin-bottom: 20px; }}
        .stack-card {{ background: #050505; border: 1px solid #1a1a1a; border-radius: 4px; padding: 25px; transition: all 0.2s; }}
        .stack-card:hover {{ border-color: #333; transform: translateY(-3px); }}
        .stack-badge {{ display: inline-block; padding: 3px 8px; font-size: 0.65rem; font-weight: bold; letter-spacing: 1px; border-radius: 2px; margin-bottom: 15px; }}
        </style>
    </head>
    <body>
        {get_header('tools')}
        <div class="container" style="max-width: 1000px;">
            <div style="text-align:center; margin-bottom:50px;">
                <h1 style="font-size:3rem; margin-bottom:10px; font-weight:900;">INSTITUTIONAL <span style="color:var(--accent);">STACK</span></h1>
                <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">The mandatory software architecture for quantitative market integration.</p>
            </div>

            <div class="stack-category">LAYER 1: EXECUTION & LIQUIDITY</div>
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                <div class="stack-card">
                    <span class="stack-badge" style="background:#00C853; color:#000;">CAPITAL FUNDING</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">FTMO Infrastructure</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Leverage external capital. Pass evaluation parameters to secure up to $200k in AUM.</p>
                    <a href="{AFF_FTMO}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #00C853; color:#00C853;">ALLOCATE FUNDS</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#FF5252; color:#fff;">DERIVATIVES</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">MEXC Global Engine</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">High-capacity order execution with 0% margin maker fees and deep market depth.</p>
                    <a href="{AFF_MEXC}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #FF5252; color:#FF5252;">OPEN VENUE</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#2962FF; color:#fff;">AUTOMATION</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">Quantitative Bots</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Deploy continuous DCA and Grid algorithms natively via API without human error.</p>
                    <a href="{AFF_MEXC_BOTS}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #2962FF; color:#2962FF;">DEPLOY BOTS</a>
                </div>
            </div>

            <div class="stack-category">LAYER 2: DATA & ANALYTICS</div>
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                <div class="stack-card">
                    <span class="stack-badge" style="background:#fff; color:#000;">VISUALIZATION</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">TradingView Pro</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">The standard for charting infrastructure. Mandatory for volume delta modeling.</p>
                    <a href="{AFF_TRADINGVIEW}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #fff; color:#fff;">UPGRADE LICENSE</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#FFD700; color:#000;">ON-CHAIN</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">Glassnode Metrics</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Access raw blockchain data regarding miner outflow and institutional reserves.</p>
                    <a href="{AFF_GLASSNODE}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid var(--gold); color:var(--gold);">ACCESS DATA</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#00C853; color:#000;">FLOW TRACKING</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">CryptoQuant</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Monitor central exchange reserves and derivative funding rates in real-time.</p>
                    <a href="{AFF_CRYPTOQUANT}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #00C853; color:#00C853;">TRACK INFLOWS</a>
                </div>
            </div>

            <div class="stack-category">LAYER 3: COMPLIANCE & SECURITY</div>
            <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
                <div class="stack-card">
                    <span class="stack-badge" style="background:#FF3D00; color:#fff;">ENCRYPTION</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">NordVPN Protocols</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Mandatory encryption standard for interacting with execution APIs over public networks.</p>
                    <a href="{AFF_NORDVPN}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #FF3D00; color:#FF3D00;">SECURE CHANNEL</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#8A2BE2; color:#fff;">AUDIT</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">Koinly Tax Protocol</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">Automate regulatory reports and calculate fiscal liabilities via secure API reading.</p>
                    <a href="{AFF_KOINLY}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #8A2BE2; color:#8A2BE2;">GENERATE REPORT</a>
                </div>
                <div class="stack-card">
                    <span class="stack-badge" style="background:#007BFF; color:#fff;">CUSTODY</span>
                    <h3 style="color:#fff; font-size:1.3rem; margin-top:0;">Trezor Hardware</h3>
                    <p style="color:#888; font-size:0.9rem; line-height:1.6;">The industry-standard open-source cold storage for securing private keys offline.</p>
                    <a href="{AFF_TREZOR}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:12px; margin-top:20px; background:transparent; border:1px solid #007BFF; color:#007BFF;">SECURE KEYS</a>
                </div>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("tools.html", html)

def build_stories_page():
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Case Studies</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('stories')}
        <div class="container">
            <div style="text-align:center; margin-bottom:50px;">
                <h1 style="font-size:3rem; margin-bottom:10px; font-weight:900;">CLIENT <span style="color:var(--accent);">CASE STUDIES</span></h1>
                <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Verified analytical accounts of retail participants transitioning to quantitative frameworks using our proprietary data.</p>
            </div>
            
            <div class="grid">
                <div class="panel" style="background:#050505; border:1px solid #222; border-radius:4px; border-top: 3px solid #00C853; position:relative;">
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
                
                <div class="panel" style="background:#050505; border:1px solid #222; border-radius:4px; border-top: 3px solid var(--gold); position:relative;">
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
                
                <div class="panel" style="background:#050505; border:1px solid #222; border-radius:4px; border-top: 3px solid var(--accent); position:relative;">
                    <div style="position:absolute; top:-15px; right:20px; background:var(--accent); color:#fff; padding:4px 8px; border-radius:2px; font-weight:bold; font-size:0.7rem; letter-spacing:1px;">API AUTOMATION</div>
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
                <p style="color:#666; margin-bottom:30px; font-size:0.9rem;">Stop gambling and start trading with an institutional edge.</p>
                <a href="pricing.html" class="vip-btn" style="padding:15px 40px; font-size:1rem; text-decoration:none; border-radius:2px; letter-spacing:1px;">PROVISION TIER 2</a>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("stories.html", html)

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
    logger.info(" Motore SEO generato.")