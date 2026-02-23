import os
import json
import datetime
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import get_header, get_footer, MODALS_HTML

logger = get_logger("Builder")

# =========================================================
# 💰 CABINA DI REGIA AFFILIAZIONI (I TUOI LINK REALI INTACT)
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

# Placeholder per i link futuri
AFF_FTMO = "https://ftmo.com/en/?affiliates=TUO_CODICE"
AFF_GLASSNODE = "https://glassnode.com/?via=TUO_CODICE"
AFF_UDEMY_COURSE = "https://click.linksynergy.com/fs-bin/click?id=TUO_CODICE&offerid=UDEMY_TRADING_COURSE"
# =========================================================

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: QUANTITATIVE PSYCHOLOGY", 
        "lessons": [
            {
                "id": "lez1_1", 
                "title": "1.1 Institutional Mindset", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">The 1% Statistical Edge</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Retail market participants systematically lose capital due to emotional execution. At Market Insider Pro, we eliminate discretionary bias. We execute purely on quantitative probabilities.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FFD700; border-radius:8px;'>
                    <h3 style="color:#FFD700; margin-top:0;">Mandatory Literature</h3>
                    <p style="color:#ccc;">To align with institutional standards, "Trading in the Zone" by Mark Douglas is required reading for risk management conditioning.</p>
                    <a href='{AMAZON_LINK_BOOK}' target='_blank' class='vip-btn' style='background: linear-gradient(45deg, #ff9900, #ffc107); color:black; text-decoration:none; display:inline-block; margin-top:10px;'>ACQUIRE RESOURCE</a>
                </div>
                '''
            }
        ]
    },
    "mod2": {
        "title": "MODULE 2: TECHNICAL FRAMEWORKS", 
        "lessons": [
            {
                "id": "lez2_1", 
                "title": "2.1 Liquidity Architecture", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">Price Action & Volume Distribution</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Discard lagging indicators. Institutional algorithms track only raw volume nodes and liquidity sweeps.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FCD535; border-radius:8px;'>
                    <h3 style="color:#FCD535; margin-top:0;">Hardware Specifications</h3>
                    <p style="color:#ccc;">Multi-timeframe analysis requires significant screen real estate. An ultrawide display is standard protocol.</p>
                    <a href='{AMAZON_LINK_MONITOR}' target='_blank' class='vip-btn' style='background:#f5f5f5; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>HARDWARE UPGRADE</a>
                </div>
                <div style='margin-top:20px; padding:30px; background:#1a1a1a; border-left:4px solid #FCD535; border-radius:8px;'>
                    <h3 style="color:#FCD535; margin-top:0;">Execution Venue</h3>
                    <p style="color:#ccc;">Zero-slippage execution is mandatory. Connect to top-tier liquidity pools.</p>
                    <a href='{BINANCE_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background:#FCD535; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>ACCESS BINANCE POOL</a>
                </div>
                '''
            }
        ]
    },
    "mod3": {
        "title": "MODULE 3: ON-CHAIN ANALYSIS", 
        "lessons": [
            {
                "id": "lez3_1", 
                "title": "3.1 Order Block Dynamics", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">Identifying Accumulation Nodes</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Order Blocks (OBs) represent massive capital deployment by central entities. We trace these footprints to model predictive entries.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #00C853; border-radius:8px;'>
                    <h3 style="color:#00C853; margin-top:0;">Asset Custody Protocol</h3>
                    <p style="color:#ccc;">Long-term capital must remain disconnected from network attack vectors. Cold storage is strictly enforced.</p>
                    <a href='{AMAZON_LINK_LEDGER}' target='_blank' class='vip-btn' style='background:#00C853; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>SECURE HARDWARE</a>
                </div>
                '''
            }
        ]
    },
    "mod4": {
        "title": "MODULE 4: ALGORITHMIC EXECUTION", 
        "lessons": [
            {
                "id": "lez4_1", 
                "title": "4.1 API Environment Setup", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">System Integration</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Connect exchange APIs to deploy systematic logic without manual intervention.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FF9900; border-radius:8px;'>
                    <h3 style="color:#FF9900; margin-top:0;">Latency Optimization</h3>
                    <p style="color:#ccc;">High-frequency logic demands ultra-low latency. Dedicated futures accounts are recommended.</p>
                    <a href='{BYBIT_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background:#17181E; border:1px solid #FF9900; color:#FF9900; text-decoration:none; display:inline-block; margin-top:10px;'>INITIALIZE PRO ACCOUNT</a>
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
    "XRP": {"name": "Ripple", "symbol": "BINANCE:XRPUSDT", "type": "crypto", "has_chart": True},
    "ADA": {"name": "Cardano", "symbol": "BINANCE:ADAUSDT", "type": "crypto", "has_chart": True},
    "DOGE": {"name": "Dogecoin", "symbol": "BINANCE:DOGEUSDT", "type": "crypto", "has_chart": True},
    "PEPE": {"name": "Pepe", "symbol": "BINANCE:1000PEPEUSDT", "type": "crypto", "has_chart": True},
    "RNDR": {"name": "Render", "symbol": "BINANCE:RENDERUSDT", "type": "crypto", "has_chart": True}, 
    "NVDA": {"name": "Nvidia", "symbol": "NASDAQ:NVDA", "type": "stock", "has_chart": True},
    "AAPL": {"name": "Apple", "symbol": "NASDAQ:AAPL", "type": "stock", "has_chart": True},
    "TSLA": {"name": "Tesla", "symbol": "NASDAQ:TSLA", "type": "stock", "has_chart": True},
    "MIP_INDEX": {"name": "MIP Liquidity Index", "symbol": "NONE", "type": "index", "has_chart": False}
}

def scrivi_file(nome_file: str, contenuto: str) -> None:
    path = os.path.join(OUTPUT_FOLDER, nome_file)
    try:
        with open(path, "wb") as f: 
            f.write(contenuto.encode('utf-8'))
        logger.info(f"💾 Generato: {nome_file}")
    except IOError as e: 
        logger.error(f"❌ Errore scrittura: {e}")

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
        <div class="card-wrapper" data-id="{elem_id}">
            <span class="star-icon" id="star-{elem_id}" onclick="toggleStar('{elem_id}')">★</span>
            <a href="chart_{elem_id}.html" class="card-link" style="display:block; height:100%;">
                <div class="card">
                    <div class="card-head">
                        <span class="symbol">{ticker}</span>
                        <span class="name" style="color:#888; font-size:0.8rem;">{db_info['name']}</span>
                    </div>
                    <div class="price" id="price-{elem_id}">{format_price(d_asset["price"])}</div>
                    <div class="change {color}" id="change-{elem_id}">{( "+" if d_asset["change"] >= 0 else "" )}{d_asset["change"]}%</div>
                    <div class="signal-box">
                        <span>AI SIGNAL:</span>
                        <strong style="color:{d_asset["sig_col"]}">{d_asset["signal"]}</strong>
                    </div>
                </div>
            </a>
        </div>
        '''
        
        chart_content = ""
        if db_info["has_chart"]:
            chart_content = f'''
            <div class="tradingview-widget-container" style="height:100%;width:100%; margin-top:20px; border:1px solid #333; border-radius:12px; overflow:hidden;">
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
                    "toolbar_bg": "#f1f3f6",
                    "enable_publishing": false,
                    "allow_symbol_change": true,
                    "studies": ["RSI@tv-basicstudies"],
                    "container_id": "tv_{elem_id}"
                }});
                </script>
            </div>
            '''
        else:
            chart_content = f'''
            <div style="text-align:center; padding: 120px 20px; background:#111; border-radius:12px; margin-top:30px; border:1px solid #333;">
                <h1 style="font-size:4rem; margin:0;">🔒</h1>
                <h2 style="color:#FFD700; margin-top:20px; font-size: 2rem;">Proprietary Asset Data</h2>
                <p style="color:#aaa; font-size: 1.1rem; max-width: 600px; margin: 15px auto;">Standard charting unavailable for <b>{db_info['name']}</b>. <br>Our backend is computing internal liquidity structures.</p>
                <button class="vip-btn" onclick="window.history.back()" style="margin-top:30px; padding: 15px 40px;">RETURN</button>
            </div>
            '''

        chart_page = get_header("home") + f'''
        <main class="container">
            <a href="index.html" style="color:#888; text-decoration:none; display:inline-block; margin: 15px 0; font-size: 0.9rem; letter-spacing: 1px;">BACK TO TERMINAL</a>
            <h1 style="margin:0; font-size: 2.5rem;">{db_info['name']} <span style="color:var(--accent);">ANALYTICS</span></h1>
            {chart_content}
        </main>
        ''' + MODALS_HTML + get_footer()
        scrivi_file(f"chart_{elem_id}.html", chart_page)

    fng_color = "#FF3D00" if fng['value'] < 40 else ("#00C853" if fng['value'] > 60 else "#FFD700")
    fng_html = f'''
    <div class="fng-meter">
        <h3 style="margin:0; color:#888; text-transform:uppercase; font-size:0.9rem;">MARKET SENTIMENT</h3>
        <div class="fng-value" style="color:{fng_color};">{fng["value"]}</div>
        <div style="font-weight:bold; letter-spacing:1px;">{fng["text"]}</div>
        <div class="fng-bar">
            <div class="fng-indicator" style="left: {fng["value"]}%;"></div>
        </div>
    </div>
    '''
    
    watchlist_script = '''
    <script>
    const WL_KEY = "mip_watchlist_v1"; 
    function toggleStar(id) { 
        let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); 
        if(wl.includes(id)) { 
            wl = wl.filter(x => x !== id); 
        } else { 
            wl.push(id); 
        } 
        localStorage.setItem(WL_KEY, JSON.stringify(wl)); 
        sortGrid(); 
    } 
    function sortGrid() { 
        let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); 
        let grid = document.getElementById("markets-grid"); 
        let cards = Array.from(grid.children); 
        cards.forEach(c => { 
            let id = c.getAttribute("data-id"); 
            let star = document.getElementById("star-"+id); 
            if(wl.includes(id)) { 
                star.classList.add("active"); 
            } else { 
                star.classList.remove("active"); 
            } 
        }); 
        cards.sort((a, b) => { 
            let aStar = wl.includes(a.getAttribute("data-id")) ? 1 : 0; 
            let bStar = wl.includes(b.getAttribute("data-id")) ? 1 : 0; 
            return bStar - aStar; 
        }); 
        cards.forEach(c => grid.appendChild(c)); 
    } 
    document.addEventListener("DOMContentLoaded", sortGrid);
    </script>
    '''
    
    news_rows = "".join([f'''
        <tr style="border-bottom: 1px solid #333;">
            <td style="padding:15px 10px;">
                <a href="{n["link"]}" target="_blank" style="font-weight:700; color:#fff; display:block; margin-bottom:5px;">{n["title"]}</a>
                <span style="font-size:0.75rem; color:#888;">{n["source"]}</span>
            </td>
            <td style="text-align:right;">
                <a href="{n["link"]}" target="_blank" class="btn-trade" style="background:#222; color:#fff; border:none;">READ</a>
            </td>
        </tr>
    ''' for n in news])
    
    ticker_css = '''
    <style>
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-50%, 0, 0); } } 
    .ticker-wrap { width: 100%; overflow: hidden; background-color: #0a0a0a; border-bottom: 1px solid #333; padding: 8px 0; } 
    .ticker { display: inline-block; white-space: nowrap; padding-right: 100%; box-sizing: content-box; animation: ticker 40s linear infinite; font-family: monospace; font-size: 0.85rem; color: #00C853; } 
    .ticker-item { display: inline-block; padding: 0 2rem; } 
    .market-clocks { display: flex; justify-content: space-between; flex-wrap:wrap; gap:10px; background: #111; padding: 20px; border-radius: 8px; border: 1px solid #333; margin-bottom: 20px; font-family: monospace; color: #888; } 
    .clock { text-align: center; flex:1; min-width:120px; border-right: 1px solid #333;} 
    .clock:last-child { border:none; } 
    .clock span { display: block; font-size: 1.4rem; color: #fff; font-weight: bold; margin-top: 5px; letter-spacing:2px; }
    </style>
    '''
    
    ticker_html = f'''
    <div class="ticker-wrap">
        <div class="ticker">
            <div class="ticker-item">SYSTEM ALERT: 1,240 BTC outflow from Binance confirmed.</div>
            <div class="ticker-item" style="color:var(--red);">LIQUIDATION DATA: $4.2M wiped on ETH derivatives.</div>
            <div class="ticker-item" style="color:var(--gold);">MACRO CALENDAR: US CPI aligns with consensus.</div>
            <div class="ticker-item">DARK POOL: $15M block executed on NVDA.</div>
            <div class="ticker-item">SYSTEM ALERT: 1,240 BTC outflow from Binance confirmed.</div>
            <div class="ticker-item" style="color:var(--red);">LIQUIDATION DATA: $4.2M wiped on ETH derivatives.</div>
        </div>
    </div>
    '''
    
    clocks_html = '''
    <div class="market-clocks">
        <div class="clock">NEW YORK (NYSE) <span id="clock-ny">--:--</span></div>
        <div class="clock">LONDON (LSE) <span id="clock-lon">--:--</span></div>
        <div class="clock">TOKYO (TSE) <span id="clock-tok">--:--</span></div>
        <div class="clock">DIGITAL ASSETS <span style="color:#00C853; font-size:1.1rem; padding-top:4px;">24/7 OPEN</span></div>
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

    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Market Insider Pro</title>
        {CSS_CORE}
        {ticker_css}
    </head>
    <body>
        {get_header('home')}
        {ticker_html}
        <div class="container">
            {clocks_html}
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                <h2 class="section-title" style="margin:0;">GLOBAL MACRO PULSE</h2>
                <div style="font-size:0.8rem; color:#00C853;"><span style="height:8px;width:8px;background:#00C853;border-radius:50%;display:inline-block;animation:pulse 1s infinite;"></span> SECURE CONNECTION</div>
            </div>
            <p style="color:#888; margin-top:-10px; margin-bottom:20px; font-size:0.9rem;">Mark assets to construct custom watchlist.</p>
            <div class="grid" id="markets-grid">
                {grid_html}
            </div>
            <div class="split-layout">
                <div class="panel">
                    {fng_html}
                </div>
                <div class="panel">
                    <h2 class="section-title">MARKET INTELLIGENCE</h2>
                    <table style="width:100%;">
                        <tbody>{news_rows}</tbody>
                    </table>
                </div>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()} 
        {watchlist_script}
    </body>
    </html>'''
    scrivi_file("index.html", html)

def build_signals_page(assets: List[Dict]):
    hot_assets = [a for a in assets if abs(a['change']) >= 1.0]
    
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
            tp2 = p * (1 + (vol_mult * 4.0))
        else:
            sig = "SHORT BIAS"
            css = "signal-sell"
            sl = p * (1 + (vol_mult * 1.5))
            tp1 = p * (1 - (vol_mult * 2.0))
            tp2 = p * (1 - (vol_mult * 4.0))
            
        rows += f'''
        <tr style="border-bottom: 1px solid #333; background: rgba(0,0,0,0.2);">
            <td style="padding:20px;">
                <strong style="font-size:1.2rem; color:#fff;">{a["symbol"]}</strong><br>
                <span style="font-size:0.8rem;color:#888;">{a["name"]}</span>
            </td>
            <td style="padding:20px; font-weight:bold; font-size:1.1rem;" class="{css}">{sig}</td>
            <td style="padding:20px;">
                <div style="font-size:0.7rem; color:#888; text-transform:uppercase;">Entry Price</div>
                <strong style="color:#fff;">{format_price(p)}</strong>
            </td>
            <td style="padding:20px;">
                <div style="font-size:0.7rem; color:#888; text-transform:uppercase;">Target Matrix</div>
                <strong style="color:var(--gold);">{format_price(tp1)} - {format_price(tp2)}</strong>
            </td>
            <td style="padding:20px;">
                <div style="font-size:0.7rem; color:#888; text-transform:uppercase;">Risk Invalidation</div>
                <strong style="color:#FF3D00;">{format_price(sl)}</strong>
            </td>
            <td style="padding:20px; text-align:right;">
                <a href="chart_{a["id"]}.html" class="btn-trade" style="padding: 10px 20px;">DATA</a>
            </td>
        </tr>
        '''

    risk_manager_html = '''
    <div class="panel" style="margin-bottom:30px; border-left:4px solid var(--accent); background: linear-gradient(135deg, #111, #0a0a0a);">
        <h3 style="margin-top:0; color:#fff;">QUANTITATIVE RISK MODEL</h3>
        <p style="color:#aaa; font-size:0.9rem;">Calculate exact position exposure based on strict institutional tolerance algorithms.</p>
        <div class="wallet-form" style="padding:0; background:none; border:none; flex-wrap:wrap; gap:15px; margin-bottom:0;">
            <div style="flex:1; min-width:150px;">
                <label style="font-size:0.75rem; color:#888; text-transform:uppercase;">Capital ($)</label>
                <input type="number" id="rm-balance" value="10000" style="width:100%; box-sizing:border-box; margin-top:5px;">
            </div>
            <div style="flex:1; min-width:150px;">
                <label style="font-size:0.75rem; color:#888; text-transform:uppercase;">Risk Exposure (%)</label>
                <input type="number" id="rm-risk" value="1" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px;">
            </div>
            <div style="flex:1; min-width:150px;">
                <label style="font-size:0.75rem; color:#888; text-transform:uppercase;">Invalidation Distance (%)</label>
                <input type="number" id="rm-sl" value="2.5" step="0.1" style="width:100%; box-sizing:border-box; margin-top:5px;">
            </div>
            <div style="display:flex; align-items:flex-end;">
                <button class="btn-trade" onclick="calcRisk()" style="padding:12px 24px; height:42px;">CALCULATE</button>
            </div>
        </div>
        <div id="rm-result" style="display:none; margin-top:20px; padding:15px; background:#000; border-radius:6px; border:1px solid #333;">
            <span style="color:#888; text-transform:uppercase; font-size:0.8rem;">Optimal Allocation Size:</span> 
            <strong id="rm-size" style="color:var(--gold); font-size:1.5rem; margin-left:10px;">$0</strong>
        </div>
    </div>
    <script>
    function calcRisk() {
        let bal = parseFloat(document.getElementById('rm-balance').value);
        let risk = parseFloat(document.getElementById('rm-risk').value);
        let sl = parseFloat(document.getElementById('rm-sl').value);
        if(bal>0 && risk>0 && sl>0) {
            let riskAmt = bal * (risk/100);
            let posSize = riskAmt / (sl/100);
            document.getElementById('rm-result').style.display = 'flex';
            document.getElementById('rm-result').style.alignItems = 'center';
            document.getElementById('rm-size').innerText = '$' + posSize.toLocaleString('en-US', {maximumFractionDigits:2});
        }
    }
    </script>
    '''

    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Signals Engine</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('signals')}
        <div class="container">
            {risk_manager_html}
            <div style="background: rgba(255, 61, 0, 0.1); border: 1px solid #FF3D00; padding: 15px; border-radius: 8px; margin-bottom: 30px; text-align: center;">
                <strong style="color: #FF3D00;">SYSTEM ADVISORY:</strong> 
                <span style="color: #ccc; font-size: 0.9rem;">Algorithmic targets are generated based on mathematical variance (ATR). Do not execute discretionary trades blindly.</span>
            </div>
            <h2 class="section-title">QUANTITATIVE SIGNALS ENGINE</h2>
            <div class="panel" style="padding:0; overflow-x:auto;">
                <table style="width:100%;">
                    <thead>
                        <tr style="background:#0a0a0a;">
                            <th>ASSET</th>
                            <th>ALGO SIGNAL</th>
                            <th>ENTRY</th>
                            <th>TARGET ZONES</th>
                            <th>INVALIDATION</th>
                            <th style="text-align:right;">DATA</th>
                        </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("signals.html", html)

def build_api_hub():
    js_script = '''
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
                term.innerHTML += "><span style='color:#fff;'> connect</span><br>> Establishing secure bridge...<br>"; 
                setTimeout(() => { term.innerHTML += "> Encrypting payload (AES-256)... <span style='color:#00C853;'>OK</span><br>"; }, 800); 
                setTimeout(() => { term.innerHTML += "> Requesting API permissions...<br>"; }, 1800); 
                setTimeout(() => { term.innerHTML += "<span style='color:var(--red); font-weight:bold;'>! EXECUTION REJECTED: TIER NOT AUTHORIZED</span><br>"; openWaitlist(); e.target.disabled = false; }, 3200); 
            } else { 
                term.innerHTML += "><span style='color:#fff;'> " + val + "</span><br>> Command void. Type '<span style='color:#fff;'>connect</span>'.<br>"; 
                e.target.value = ''; 
            } 
            let termDiv = document.getElementById('term'); 
            termDiv.scrollTop = termDiv.scrollHeight; 
        } 
    }
    </script>
    '''
    
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>API Execution Hub</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('api')}
        <div class="container" style="max-width:800px;">
            <div style="text-align:center; margin-bottom:40px;">
                <h1 style="font-size:2.5rem; margin-bottom:10px;">ALGORITHMIC EXECUTION HUB</h1>
                <p style="color:#888; font-size:1.1rem;">Bridge exchange infrastructures to deploy automated strategy logic.</p>
            </div>
            <div class="panel" style="padding:40px;">
                <div id="api-form-container" class="wallet-form" style="background:none; border:none; padding:0; flex-direction:column; gap:20px;">
                    <div>
                        <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Protocol</label>
                        <select style="width:100%; margin-top:5px; padding:15px; background:#000; border:1px solid #333; color:#fff;">
                            <option>Binance FIX/REST API</option>
                            <option>Bybit Linear API</option>
                            <option>MEXC v3 API</option>
                        </select>
                    </div>
                    <div>
                        <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Public Key</label>
                        <input type="text" style="width:96%; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #333; color:#fff;" placeholder="Enter Public Key">
                    </div>
                    <div>
                        <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Private Key</label>
                        <input type="password" style="width:96%; margin-top:5px; padding:15px; font-family:monospace; background:#000; border:1px solid #333; color:#fff;" placeholder="Enter Private Key">
                    </div>
                    <button class="btn-trade" style="padding:20px; font-size:1.1rem; margin-top:10px;" onclick="connectAPI()">INITIALIZE CONNECTION</button>
                </div>
                <div class="hacker-terminal" id="term" style="display:none; cursor:text; height:250px;" onclick="document.getElementById('term-input').focus()">
                    <div id="term-content">> SYSTEM READY.<br>> Awaiting execution... (Type 'connect')<br></div>
                    <div style="display:flex;">> <input type="text" id="term-input" onkeypress="checkTerminalCommand(event)" style="background:transparent; border:none; color:var(--accent); font-family:monospace; outline:none; width:100%; margin-left:5px; font-size:1rem;" autocomplete="off" spellcheck="false"></div>
                </div>
            </div>
        </div>
        {js_script}
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("api_hub.html", html)

def build_brokers_page():
    brokers = [
        {"name": "Binance", "type": "Spot & Derivatives", "pros": "Deepest Liquidity Depth", "link": BINANCE_AFFILIATE_LINK, "cta": "OPEN ACCOUNT"},
        {"name": "Bybit", "type": "Perpetual Futures", "pros": "Low Latency API", "link": BYBIT_AFFILIATE_LINK, "cta": "PROVISION ACCOUNT"},
        {"name": "MEXC", "type": "High Leverage", "pros": "0% Maker Fees", "link": AFF_MEXC, "cta": "ACCESS PLATFORM"}
    ]
    html_cards = "".join([f'''
        <div class="broker-card">
            <div style="display:flex; align-items:center;">
                <div class="broker-info">
                    <h3 style="margin:0; color:#fff;">{b["name"]}</h3>
                    <div class="broker-tags"><span>{b["type"]}</span><span>{b["pros"]}</span></div>
                </div>
            </div>
            <a href="{b["link"]}" target="_blank" class="btn-trade" style="padding:12px 24px; text-align:center;">{b["cta"]}</a>
        </div>
    ''' for b in brokers])
    
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Partner Exchanges</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('brokers')}
        <div class="container">
            <h2 class="section-title">SUPPORTED VENUES</h2>
            <p style="color:#888; margin-bottom:30px;">Certified exchange infrastructures for algorithmic deployment and secure custody.</p>
            <div style="max-width:800px; margin:0 auto;">
                {html_cards}
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("brokers.html", html)

def build_referral_page():
    js = '''
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        let user = localStorage.getItem('mip_user') || 'trader' + Math.floor(Math.random()*1000); 
        let link = `https://marketinsiderpro.com/invite/${user.toLowerCase()}`; 
        document.getElementById('ref-url').innerText = link; 
    }); 
    function copyLink() { 
        navigator.clipboard.writeText(document.getElementById('ref-url').innerText); 
        let btn = document.getElementById('copy-btn'); 
        btn.innerText = "COPIED"; 
        btn.style.background = "#00C853"; 
        setTimeout(() => { 
            btn.innerText = "COPY LINK"; 
            btn.style.background = "var(--accent)"; 
        }, 2000); 
    }
    </script>
    '''
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Referral Network</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('referral')}
        <div class="container" style="max-width:800px;">
            <div class="ref-box">
                <h1 style="font-size:2.5rem; margin-top:0; color:var(--gold);">NETWORK EXPANSION</h1>
                <p style="color:#ccc; font-size:1.1rem;">Distribute your unique identifier. Upon 3 successful network additions, institutional tier is granted.</p>
                <div class="ref-link-container">
                    <div class="ref-link" id="ref-url">Loading link...</div>
                    <button class="ref-copy" id="copy-btn" onclick="copyLink()">COPY LINK</button>
                </div>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()} 
        {js}
    </body>
    </html>'''
    scrivi_file("referral.html", html)

def build_pricing_page():
    checkout_modal_html = '''
    <div class="modal-overlay" id="checkout-choice-modal">
        <div class="modal-content" style="max-width:450px; text-align:center; padding:30px;">
            <span class="close-modal" onclick="document.getElementById('checkout-choice-modal').style.display='none'">&times;</span>
            <h2 style="color:var(--gold); margin-top:0;">Authentication Check</h2>
            <p style="color:#aaa; font-size:0.95rem; margin-bottom:25px;">Select pathway to provision your Tier.</p>
            <div style="display:flex; flex-direction:column; gap:15px;">
                <button class="vip-btn" style="padding:15px; width:100%; border-radius:8px;" onclick="proceedToStripe('login')">
                    <span style="font-size:1.1rem; display:block; margin-bottom:5px;">AUTHENTICATE FIRST</span>
                </button>
                <button class="btn-trade" style="padding:15px; width:100%; background:#111; border:1px solid #555; color:#aaa; border-radius:8px;" onclick="proceedToStripe('guest')">
                    <span style="font-size:1.1rem; display:block; margin-bottom:5px;">PROCEED AS GUEST</span>
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
            openLogin(); 
        } 
    }
    </script>
    '''
    
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Pricing</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('pricing')}
        <div class="container">
            <div style="text-align:center; margin-bottom:20px;">
                <h1 style="font-size:3rem; margin-bottom:10px;">INSTITUTIONAL <span style="color:var(--gold);">ACCESS</span></h1>
                <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Upgrade data infrastructure. Access unmetered algorithmic feeds and strictly professional analytical models.</p>
            </div>
            
            <div class="pricing-grid">
                <div class="pricing-card">
                    <h3 style="color:#aaa; font-size:1.5rem; margin:0;">STANDARD</h3>
                    <div class="price-tag">$0<span>/mo</span></div>
                    <div style="margin-bottom:30px;">
                        <div class="plan-feature">Delayed Terminal Data</div>
                        <div class="plan-feature">Basic Modeling</div>
                        <div class="plan-feature">Academy Core</div>
                    </div>
                    <button class="vip-btn" style="width:100%; background:#333; cursor:default;">CURRENT TIER</button>
                </div>
                
                <div class="pricing-card pro">
                    <h3 style="color:var(--gold); font-size:1.5rem; margin:0;">QUANT TIER</h3>
                    <div class="price-tag">$49<span>/mo</span></div>
                    <div style="margin-bottom:30px;">
                        <div class="plan-feature" style="color:#fff;">Real-Time Data Feeds</div>
                        <div class="plan-feature" style="color:#fff;">Advanced Academy Access</div>
                        <div class="plan-feature" style="color:#fff;">Signals Database</div>
                        <div class="plan-feature" style="color:#fff;">Portfolio Aggregator</div>
                    </div>
                    <button class="btn-trade checkout-btn" onclick="openCheckoutChoice('https://buy.stripe.com/dRmcN56uTbIR6N8fux2Ry00')" style="width:100%; padding:15px; font-size:1.2rem;">PROVISION SECURELY</button>
                </div>
                
                <div class="pricing-card">
                    <h3 style="color:#2962FF; font-size:1.5rem; margin:0;">LIFETIME</h3>
                    <div class="price-tag">$399<span>/once</span></div>
                    <div style="margin-bottom:30px;">
                        <div class="plan-feature">All Quant Tier Features</div>
                        <div class="plan-feature">Private Network Access</div>
                        <div class="plan-feature">Perpetual Updates</div>
                    </div>
                    <button class="vip-btn checkout-btn" onclick="openCheckoutChoice('https://buy.stripe.com/14AfZh6uT9AJ3AW5TX2Ry01')" style="width:100%; padding:15px;">ACQUIRE LICENSE</button>
                </div>
            </div>
        </div>
        {checkout_modal_html}
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("pricing.html", html)

def build_leaderboard_page():
    js = '''
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        let user = localStorage.getItem('mip_user'); 
        if(user) { 
            document.getElementById('lb-body').innerHTML += `<tr class="user-row"><td class="rank-3">#8</td><td><strong>👤 ${user}</strong></td><td>$14,250</td><td class="change green">+18.4%</td><td>Pro</td></tr>`; 
        } 
    });
    </script>
    '''
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Leaderboard</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('leaderboard')}
        <div class="container">
            <h2 class="section-title" style="text-align:center; font-size:2rem; border:none; margin-bottom:10px;">GLOBAL METRICS</h2>
            <p style="text-align:center; color:#888; margin-bottom:40px;">Statistical ranking of top network profiles by realized equity curve.</p>
            <div class="panel" style="max-width:900px; margin:0 auto;">
                <table>
                    <thead>
                        <tr style="border-bottom:2px solid #333;">
                            <th>RANK</th>
                            <th>IDENTIFIER</th>
                            <th>CAPITAL DEPLOYED</th>
                            <th>30D YIELD</th>
                            <th>TIER</th>
                        </tr>
                    </thead>
                    <tbody id="lb-body">
                        <tr><td class="rank-1">#1</td><td><strong>Entity_99</strong></td><td>$1.2M</td><td class="change green">+142.5%</td><td><span style="color:var(--gold);">Whale</span></td></tr>
                        <tr><td class="rank-2">#2</td><td><strong>Quant_LDN</strong></td><td>$450K</td><td class="change green">+89.2%</td><td>Quant</td></tr>
                        <tr><td class="rank-3">#3</td><td><strong>CapitalX</strong></td><td>$89K</td><td class="change green">+64.8%</td><td>Quant</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()} 
        {js}
    </body>
    </html>'''
    scrivi_file("leaderboard.html", html)

def build_legal_page():
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Legal</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('legal')}
        <div class="container" style="max-width:800px; color:#ccc;">
            <h1 style="color:#fff;">Compliance & Policies</h1>
            <hr style="border-color:#333; margin-bottom:30px;">
            <h3 style="color:var(--accent);">Data Policy</h3>
            <p>Market Insider Pro utilizes client-side storage to minimize server dependency and enhance security. No identifiable data is harvested without consent.</p>
            <h3 style="color:var(--accent);">Terms of Operation</h3>
            <p>Platform access is contingent on adherence to network rules. Content is analytical, not advisory.</p>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("legal.html", html)

def build_chart_pages(assets: List[Dict]):
    pass

def build_academy():
    sidebar = "".join([f"<div class='module-title'>{m['title']}</div>" + "".join([f'''<div onclick="window.location.href='academy_{l['id']}.html'" class="lesson-link">{"🔒" if l.get("vip") else "📄"} {l['title']}</div>''' for l in m['lessons']]) for _, m in ACADEMY_CONTENT.items()])
    
    for _, m in ACADEMY_CONTENT.items():
        for l in m['lessons']:
            if l.get("vip"):
                c_html = f'''
                <div id="vip-content" style="filter: blur(8px); pointer-events: none; user-select: none; transition: 0.5s;">{l['html']}</div>
                <div id="vip-lock" style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--accent); border-radius:12px; z-index:10; width:90%; max-width:400px;">
                    <h2 style="color:#FFD700; margin-top:0;">RESTRICTED DATA</h2>
                    <p style="color:#aaa; margin-bottom:20px;">Protocol requires VIP clearance.</p>
                    <a href="pricing.html" class="btn-trade" style="display:block; padding:15px;">AUTHENTICATE VIP</a>
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
                
            html = f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{l['title']}</title>
                {CSS_CORE}
            </head>
            <body>
                {get_header('academy')}
                <div class="container">
                    <div class="academy-grid">
                        <div class="sidebar">{sidebar}</div>
                        <div class="lesson-content" style="position:relative;">{c_html}</div>
                    </div>
                </div>
                {MODALS_HTML}
                {get_footer()}
            </body>
            </html>'''
            scrivi_file(f"academy_{l['id']}.html", html)

def build_chat():
    js = '''
    <script>
    function send(){
        let i=document.getElementById('in'); 
        let v=i.value; 
        if(!v)return; 
        let h=document.getElementById('hist'); 
        h.innerHTML+=`<div class="msg msg-user">${v}</div>`; 
        i.value=''; h.scrollTop=h.scrollHeight; 
        let t="t-"+Date.now(); 
        h.innerHTML+=`<div class="msg msg-ai" id="${t}">🤖 Analyzing...</div>`; 
        h.scrollTop=h.scrollHeight; 
        setTimeout(()=>{
            document.getElementById(t).innerHTML=`🤖 Market sentiment is actively shifting. Always check the Signals Room before entering a trade.`; 
            h.scrollTop=h.scrollHeight;
        }, 1000);
    } 
    document.getElementById('in').addEventListener("keypress", e=>{if(e.key==="Enter")send();});
    </script>
    '''
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AI Analyst</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('chat')}
        <div class="container">
            <h2 class="section-title">AI MARKET ANALYST 🤖</h2>
            <div class="chat-interface">
                <div class="chat-history" id="hist">
                    <div class="msg msg-ai">🤖 Welcome.</div>
                </div>
                <div class="chat-input-area">
                    <input type="text" class="chat-input" id="in" placeholder="Type here...">
                    <button class="chat-btn" onclick="send()">ANALYZE</button>
                </div>
            </div>
        </div>
        {js}
        {MODALS_HTML}
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("chat.html", html)


# === IL NUOVO WALLET (PORTFOLIO AGGREGATOR VIP) ESTESO ===
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
        if(!input) return alert("System requires input address/API key.");
        
        btn.innerText = "QUERYING NETWORK...";
        btn.style.opacity = "0.7";
        
        setTimeout(() => {
            btn.innerText = "DATA IMPORTED";
            btn.style.background = "#00C853";
            document.getElementById('portfolio-stats').style.display = 'grid';
            
            let total = (Math.random() * 50000 + 10000).toFixed(2);
            document.getElementById('val-total').innerText = "$" + Number(total).toLocaleString();
            document.getElementById('val-pnl').innerText = "+" + (Math.random() * 15 + 2).toFixed(2) + "%";
            
            setTimeout(() => { 
                btn.innerText = "SYNC DATA"; 
                btn.style.background = "var(--accent)"; 
                btn.style.opacity = "1"; 
                document.getElementById('wallet-input').value = "";
            }, 3000);
        }, 2000);
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
        .metric-box {{ background:#000; padding:20px; border:1px solid #333; border-radius:8px; text-align:center; }}
        .metric-title {{ color:#888; font-size:0.8rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; }}
        .metric-value {{ font-size:2rem; color:#fff; font-weight:bold; }}
        </style>
    </head>
    <body>
        {get_header('wallet')}
        <div class="container">
            <h2 class="section-title">PORTFOLIO ANALYTICS PLATFORM</h2>
            
            <div id="lock-screen" style="text-align:center; padding: 100px 20px; background:#111; border-radius:12px; border:1px solid #333;">
                <h2 style="color:#FFD700; font-size: 2rem; margin-top:0;">RESTRICTED INFRASTRUCTURE</h2>
                <p style="color:#aaa; font-size: 1.1rem; max-width: 600px; margin: 15px auto;">The API & Blockchain Aggregator is reserved for Tier 2 (VIP) users. It calculates real-time drawdown, beta, and asset allocation across decentralized networks.</p>
                <a href="pricing.html" class="vip-btn" style="display:inline-block; margin-top:20px; padding: 15px 40px; text-decoration:none;">UNLOCK ACCESS</a>
            </div>

            <div id="vip-aggregator" style="display:none;">
                <div class="panel" style="margin-bottom:30px;">
                    <h3 style="margin-top:0; color:#fff; border-bottom:1px solid #333; padding-bottom:15px;">ADD DATA SOURCE</h3>
                    <div style="display:flex; gap:15px; flex-wrap:wrap; margin-top:20px;">
                        <select style="padding:15px; background:#000; color:#fff; border:1px solid #333; border-radius:4px; min-width:200px;">
                            <option>EVM Network (ETH/BSC/ARB)</option>
                            <option>Solana Network</option>
                            <option>Binance Read-Only API</option>
                            <option>Bybit Read-Only API</option>
                        </select>
                        <input type="text" id="wallet-input" placeholder="Paste Public Address or API Key..." style="flex:1; padding:15px; background:#000; color:#fff; border:1px solid #333; border-radius:4px; font-family:monospace;">
                        <button id="sync-btn" class="btn-trade" onclick="simulateSync()" style="padding:15px 30px;">SYNC DATA</button>
                    </div>
                    <p style="color:#666; font-size:0.8rem; margin-top:15px;">Keys are encrypted client-side. We do not store your API credentials.</p>
                </div>

                <div id="portfolio-stats" style="display:none; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:20px; margin-bottom:30px;">
                    <div class="metric-box">
                        <div class="metric-title">Aggregated Balance</div>
                        <div class="metric-value" id="val-total" style="color:var(--gold);">--</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">30D Realized PNL</div>
                        <div class="metric-value" id="val-pnl" style="color:#00C853;">--</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">Risk Beta (Market)</div>
                        <div class="metric-value" style="color:#fff;">0.85</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-title">Asset Allocation</div>
                        <div class="metric-value" style="font-size:1.2rem; margin-top:10px;">
                            <span style="color:#F7931A;">60% BTC</span> | <span style="color:#627EEA;">40% ETH</span>
                        </div>
                    </div>
                </div>
                
                <div class="panel">
                    <h3 style="margin-top:0; color:#fff;">SYNCHRONIZED SOURCES</h3>
                    <table style="width:100%; text-align:left; color:#ccc; border-collapse:collapse; margin-top:15px;">
                        <tr style="border-bottom:1px solid #333;"><th style="padding:10px;">Source</th><th style="padding:10px;">Status</th><th style="padding:10px;">Last Sync</th></tr>
                        <tr><td style="padding:10px;">Awaiting Integration...</td><td style="padding:10px;">-</td><td style="padding:10px;">-</td></tr>
                    </table>
                </div>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()} 
        {js}
    </body>
    </html>'''
    scrivi_file("wallet.html", html)

def build_success_page():
    js = '''
    <script>
    document.addEventListener("DOMContentLoaded", function() { 
        localStorage.setItem('mip_vip_status', 'active'); 
        setTimeout(() => { window.location.href = "vip_lounge.html"; }, 3500); 
    });
    </script>
    '''
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Clearance Granted</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('pricing')}
        <div class="container" style="text-align:center; padding: 120px 20px;">
            <h1 style="color:var(--gold); font-size:3rem; margin-top:10px;">TIER UPGRADE COMPLETE</h1>
            <p style="color:#aaa; font-size:1.2rem;">Payment verification successful. Institutional data pathways unlocked.</p>
            <div style="margin-top:40px;">
                <div style="width:40px; height:40px; border:3px solid var(--accent); border-top-color:transparent; border-radius:50%; animation:spin 1s linear infinite; margin:0 auto;"></div>
            </div>
        </div>
        <style>@keyframes spin {{ 100% {{ transform:rotate(360deg); }} }}</style>
        {MODALS_HTML} 
        {get_footer()} 
        {js}
    </body>
    </html>'''
    scrivi_file("success.html", html)

def build_cheatsheets():
    ob_html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Order Block Strategy Document</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('vip')}
        <div class="container" style="max-width:800px; padding: 40px 20px;">
            <div style="background:#111; border:1px solid var(--accent); padding:40px; border-radius:8px; box-shadow: 0 10px 30px rgba(41, 98, 255, 0.1);">
                <h1 style="color:var(--accent); margin-top:0; border-bottom:1px solid #333; padding-bottom:15px;">📂 CONFIDENTIAL: Order Block Strategy</h1>
                <p style="color:#888; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">Internal Training Document - Do not distribute</p>
                <h3 style="color:#fff; margin-top:30px;">1. Identifying the Footprint</h3>
                <p style="color:#ccc; line-height:1.6;">An Order Block (OB) represents a massive accumulation of assets by institutions. It is visually identified on the chart as the <b>last bearish candle before a strong, impulsive bullish move</b> that breaks market structure.</p>
                <h3 style="color:#fff; margin-top:30px;">2. The Institutional Execution</h3>
                <p style="color:#ccc; line-height:1.6;">Institutions cannot enter their entire position at once without moving the market against themselves. They push the price down to grab liquidity (retail stop losses), buy massive amounts, and wait for the price to return to their "Block" to fill the rest of their orders.</p>
                <ul style="color:#ccc; line-height:1.8;">
                    <li><b>Step 1:</b> Mark the high and low of the OB candle.</li>
                    <li><b>Step 2:</b> Wait patiently for the price to retrace back into this zone.</li>
                    <li><b>Step 3:</b> Execute your entry exactly at the top of the OB.</li>
                    <li><b>Step 4:</b> Place the Stop Loss slightly below the bottom of the OB.</li>
                </ul>
                <div style="margin-top:50px; padding:30px; background:rgba(255,215,0,0.05); border:1px dashed var(--gold); border-radius:8px; text-align:center;">
                    <h3 style="color:var(--gold); margin-top:0;">⚡ MAXIMIZE YOUR EDGE</h3>
                    <p style="color:#aaa; font-size:0.95rem; margin-bottom:20px;">To execute Order Block strategies successfully, you need an exchange with deep liquidity, institutional-grade charts, and absolutely zero slippage.</p>
                    <a href="{BYBIT_AFFILIATE_LINK}" target="_blank" class="btn-trade" style="padding:15px 30px; font-size:1.1rem; display:inline-block; text-decoration:none;">OPEN PRO EXCHANGE ACCOUNT ↗</a>
                </div>
                <button onclick="window.close()" style="background:none; border:none; color:#888; text-decoration:underline; cursor:pointer; display:block; margin:30px auto 0;">Close Document</button>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("cheatsheet_ob.html", ob_html)

    risk_html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Risk Management Protocol</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('vip')}
        <div class="container" style="max-width:800px; padding: 40px 20px;">
            <div style="background:#111; border:1px solid #FF3D00; padding:40px; border-radius:8px; box-shadow: 0 10px 30px rgba(255, 61, 0, 0.1);">
                <h1 style="color:#FF3D00; margin-top:0; border-bottom:1px solid #333; padding-bottom:15px;">🛡️ RISK MANAGEMENT PROTOCOL</h1>
                <p style="color:#888; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">Capital Preservation Directive</p>
                <h3 style="color:#fff; margin-top:30px;">The 1% Golden Rule</h3>
                <p style="color:#ccc; line-height:1.6;">Professional traders do not gamble. They protect capital. You must never risk more than <b>1% of your total account balance</b> on a single trade. If your account is $10,000, your absolute maximum allowed loss if the trade hits your Stop Loss is $100.</p>
                <h3 style="color:#fff; margin-top:30px;">The Position Sizing Formula</h3>
                <p style="color:#ccc; line-height:1.6;">To calculate exactly how many dollars to invest in a trade to respect the 1% rule, use the following institutional formula:</p>
                <code style="background:#000; padding:20px; display:block; color:var(--accent); border-radius:6px; margin:20px 0; font-size:1.1rem; text-align:center;">
                    Position Size = (Account Balance * Risk %) / Stop Loss Distance %
                </code>
                <p style="color:#ccc; line-height:1.6;">Example: $10,000 balance, 1% risk ($100), and your Stop Loss is 5% away. <br>Your Position Size is: $100 / 0.05 = <b>$2,000</b>. You buy $2,000 worth of the asset.</p>
                <div style="margin-top:50px; padding:30px; background:rgba(0,200,83,0.05); border:1px dashed #00C853; border-radius:8px; text-align:center;">
                    <h3 style="color:#00C853; margin-top:0;">🔒 SECURE YOUR PROFITS</h3>
                    <p style="color:#aaa; font-size:0.95rem; margin-bottom:20px;">Hedge funds never keep their long-term capital or massive profits sitting on a live exchange. Once you hit your targets, move your wealth completely offline to cold storage.</p>
                    <a href="{AMAZON_LINK_LEDGER}" target="_blank" class="vip-btn" style="background:#00C853; color:#000; padding:15px 30px; font-size:1.1rem; display:inline-block; text-decoration:none;">GET HARDWARE WALLET ON AMAZON 🛒</a>
                </div>
                <button onclick="window.close()" style="background:none; border:none; color:#888; text-decoration:underline; cursor:pointer; display:block; margin:30px auto 0;">Close Document</button>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("cheatsheet_risk.html", risk_html)

def build_vip_lounge():
    lounge_html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>VIP Interface</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('vip')}
        <div class="container" style="position:relative;">
            <div id="vip-content" style="filter: blur(8px); pointer-events: none; user-select: none; transition: 0.5s;">
                <div style="text-align:center; margin-bottom:40px;">
                    <h1 style="font-size:3rem; margin-bottom:10px; color:var(--gold);">INSTITUTIONAL DASHBOARD</h1>
                    <p style="color:#aaa; font-size:1.1rem;">Restricted analytics architecture.</p>
                </div>
                <div class="split-layout">
                    <div class="panel">
                        <h3 style="color:#fff; margin-top:0; border-bottom:1px solid #333; padding-bottom:10px;">CUSTODIAL WALLET TRACKER</h3>
                        <table>
                            <tr><th style="color:#888; text-align:left;">Entity</th><th style="color:#888; text-align:left;">Holdings (BTC)</th><th style="color:#888; text-align:left;">Net Value</th></tr>
                            <tr><td><strong style="color:var(--gold);">MicroStrategy</strong></td><td>205,000</td><td style="color:#00C853;">$13.5B</td></tr>
                            <tr><td><strong>BlackRock</strong></td><td>195,985</td><td style="color:#00C853;">$12.9B</td></tr>
                        </table>
                    </div>
                    <div class="panel">
                        <h3 style="color:#fff; margin-top:0; border-bottom:1px solid #333; padding-bottom:10px;">MACRO CORRELATION</h3>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-top:20px;">
                            <div style="background:#000; padding:15px; border-radius:6px; border:1px solid #333; text-align:center;">
                                <div style="color:#888; font-size:0.8rem;">BTC/SPX</div>
                                <div style="color:var(--green); font-size:1.5rem; font-weight:bold;">+ 0.82</div>
                            </div>
                            <div style="background:#000; padding:15px; border-radius:6px; border:1px solid #333; text-align:center;">
                                <div style="color:#888; font-size:0.8rem;">BTC/DXY</div>
                                <div style="color:var(--red); font-size:1.5rem; font-weight:bold;">- 0.75</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div id="vip-lock" style="position:absolute; top:30%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--gold); border-radius:12px; z-index:10; width:90%; max-width:400px;">
                <h2 style="color:#FFD700; margin-top:0;">RESTRICTED AREA</h2>
                <p style="color:#aaa; margin-bottom:20px;">Data requires Tier 2 verification.</p>
                <a href="pricing.html" class="vip-btn" style="display:block; padding:15px; text-decoration:none;">INITIATE CLEARANCE</a>
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
                <h1 style="font-size:3rem; margin-bottom:10px;">CLIENT <span style="color:var(--accent);">CASE STUDIES</span></h1>
                <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Verified analytical accounts of retail participants transitioning to quantitative frameworks using our proprietary data.</p>
            </div>
            
            <div class="grid">
                <div class="panel" style="border-top: 3px solid #00C853; position:relative;">
                    <div style="position:absolute; top:-15px; right:20px; background:#00C853; color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">FUNDED PORTFOLIO</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">"From discretionary bias to systematic execution."</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6; font-style:italic;">"Before integrating MIP, I traded on emotional sentiment. The Order Block metrics inside the VIP infrastructure eliminated prediction. I now execute solely on institutional liquidity footprints."</p>
                    <div style="margin-top:20px; padding-top:20px; border-top:1px solid #333; display:flex; align-items:center; gap:15px;">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=100&q=80" style="width:50px; height:50px; border-radius:50%; object-fit:cover; border:2px solid #333;">
                        <div>
                            <strong style="color:#fff; display:block;">Marcus T.</strong>
                            <span style="color:#888; font-size:0.8rem;">Quant Tier since Q3 2025</span>
                        </div>
                    </div>
                </div>
                
                <div class="panel" style="border-top: 3px solid var(--gold); position:relative;">
                    <div style="position:absolute; top:-15px; right:20px; background:var(--gold); color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">DATA ARBITRAGE</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">"Uncovering the macro context."</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6; font-style:italic;">"The simulated Macro Correlation Matrix provided answers that standard retail charts obfuscate. Tracking cross-asset liquidity flows gave me an asymmetric edge over retail counterparts."</p>
                    <div style="margin-top:20px; padding-top:20px; border-top:1px solid #333; display:flex; align-items:center; gap:15px;">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=100&q=80" style="width:50px; height:50px; border-radius:50%; object-fit:cover; border:2px solid #333;">
                        <div>
                            <strong style="color:#fff; display:block;">Elena S.</strong>
                            <span style="color:#888; font-size:0.8rem;">Quant Tier since Q4 2025</span>
                        </div>
                    </div>
                </div>
                
                <div class="panel" style="border-top: 3px solid var(--accent); position:relative;">
                    <div style="position:absolute; top:-15px; right:20px; background:var(--accent); color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">API AUTOMATION</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">"Removing the human error variable."</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6; font-style:italic;">"Connecting my Bybit architecture to the Execution Hub was the final step. The Risk Module handles position sizing, and the algorithm manages deployment. Complete isolation of capital management."</p>
                    <div style="margin-top:20px; padding-top:20px; border-top:1px solid #333; display:flex; align-items:center; gap:15px;">
                        <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=100&q=80" style="width:50px; height:50px; border-radius:50%; object-fit:cover; border:2px solid #333;">
                        <div>
                            <strong style="color:#fff; display:block;">David K.</strong>
                            <span style="color:#888; font-size:0.8rem;">Quant Tier since Q1 2026</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div style="text-align:center; margin-top:60px; padding:40px; background:linear-gradient(135deg, #111, #0a0a0a); border:1px solid #333; border-radius:12px;">
                <h2 style="color:#fff; margin-top:0;">Ready to execute systematically?</h2>
                <p style="color:#888; margin-bottom:30px;">Stop gambling and start trading with an institutional edge.</p>
                <a href="pricing.html" class="vip-btn" style="padding:15px 40px; font-size:1.2rem; text-decoration:none;">GET VIP PASS TODAY</a>
            </div>
        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("stories.html", html)

def build_tools_page():
    html = f'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Institutional Stack</title>
        {CSS_CORE}
    </head>
    <body>
        {get_header('tools')}
        <div class="container">
            <div style="text-align:center; margin-bottom:50px;">
                <h1 style="font-size:3rem; margin-bottom:10px;">INSTITUTIONAL <span style="color:var(--accent);">STACK</span></h1>
                <p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">The required software architecture for quantitative integration.</p>
            </div>

            <div class="grid">
                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#fff; color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">CAPITAL FUNDING</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">FTMO Infrastructure</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Leverage external capital. Pass evaluation parameters to secure up to $200k in AUM.</p>
                    <a href="{AFF_FTMO}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; background:#00C853; color:#000;">ALLOCATE FUNDS ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:var(--accent); color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">DATA VISUALIZATION</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">TradingView Pro</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">The standard for charting infrastructure. Mandatory for order block and volume delta modeling.</p>
                    <a href="{AFF_TRADINGVIEW}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box;">UPGRADE LICENSE ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#2962FF; color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">API AUTOMATION</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">MEXC Quantitative Bots</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Deploy continuous DCA and Grid algorithms natively via exchange with null maker fees.</p>
                    <a href="{AFF_MEXC_BOTS}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:#2962FF; color:#2962FF;">DEPLOY BOTS ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#FFD700; color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">ON-CHAIN METRICS</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">Glassnode Engine</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Access raw blockchain data regarding miner outflow and institutional reserves.</p>
                    <a href="{AFF_GLASSNODE}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:var(--gold); color:var(--gold);">ACCESS DATA ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#00C853; color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">LIQUIDITY TRACKING</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">CryptoQuant Data</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Monitor central exchange reserves and derivative funding rates in real-time.</p>
                    <a href="{AFF_CRYPTOQUANT}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:#00C853; color:#00C853;">TRACK INFLOWS ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#FF5252; color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">EXECUTION VENUE</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">MEXC Derivatives</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">High-capacity order execution with 0% margin and deep market depth.</p>
                    <a href="{AFF_MEXC}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:#FF5252; color:#FF5252;">OPEN VENUE ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:var(--gold); color:#000; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">COMPLIANCE AUDIT</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">Koinly Tax Protocol</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Automate regulatory reports and calculate fiscal liabilities via secure API reading.</p>
                    <a href="{AFF_KOINLY}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:var(--gold); color:var(--gold);">GENERATE REPORT ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#8A2BE2; color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">THEORY & MODELS</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">Technical Masterclass</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Supplement platform signals with rigorous technical modeling provided by partner institutions.</p>
                    <a href="{AFF_UDEMY_COURSE}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:#8A2BE2; color:#8A2BE2;">ACCESS FRAMEWORK ↗</a>
                </div>

                <div class="panel" style="border:1px solid #333; position:relative;">
                    <div style="position:absolute; top:-15px; left:20px; background:#FF3D00; color:#fff; padding:5px 10px; border-radius:4px; font-weight:bold; font-size:0.8rem;">NETWORK SECURITY</div>
                    <h3 style="color:#fff; font-size:1.4rem; margin-top:10px;">NordVPN Protocols</h3>
                    <p style="color:#aaa; font-size:0.95rem; line-height:1.6;">Mandatory encryption standard for interacting with execution APIs over public architecture.</p>
                    <a href="{AFF_NORDVPN}" target="_blank" class="btn-trade" style="width:100%; display:block; text-align:center; padding:15px; margin-top:20px; box-sizing:border-box; border-color:#FF3D00; color:#FF3D00;">SECURE CHANNEL ↗</a>
                </div>
            </div>

        </div>
        {MODALS_HTML} 
        {get_footer()}
    </body>
    </html>'''
    scrivi_file("tools.html", html)


def build_seo_files():
    BASE_URL = "https://marketinsiderpro.com"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    pages = [
        "index.html", "signals.html", "api_hub.html", "brokers.html", 
        "referral.html", "pricing.html", "leaderboard.html", "legal.html",
        "academy_lez1_1.html", "academy_lez2_1.html", "academy_lez3_1.html", "academy_lez4_1.html",
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
    logger.info("🕸️ Motore SEO generato: sitemap.xml e robots.txt pronti per Google.")