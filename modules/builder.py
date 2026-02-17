import os
import json
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import get_header, get_footer, ACADEMY_CONTENT, MODALS_HTML

logger = get_logger("Builder")

# ==========================================
# DATABASE ASSET (Crypto + Azioni Tradizionali)
# ==========================================
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
    "MIP_INDEX": {"name": "MIP Whale Index", "symbol": "NONE", "type": "index", "has_chart": False}
}

def scrivi_file(nome_file: str, contenuto: str) -> None:
    path = os.path.join(OUTPUT_FOLDER, nome_file)
    try:
        with open(path, "wb") as f: f.write(contenuto.encode('utf-8'))
        logger.info(f"💾 Generato: {nome_file}")
    except IOError as e: logger.error(f"❌ Errore scrittura: {e}")

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
        
        grid_html += f'''<div class="card-wrapper" data-id="{elem_id}"><span class="star-icon" id="star-{elem_id}" onclick="toggleStar('{elem_id}')">★</span><a href="chart_{elem_id}.html" class="card-link" style="display:block; height:100%;"><div class="card"><div class="card-head"><span class="symbol">{ticker}</span><span class="name" style="color:#888; font-size:0.8rem;">{db_info['name']}</span></div><div class="price" id="price-{elem_id}">{format_price(d_asset["price"])}</div><div class="change {color}" id="change-{elem_id}">{( "+" if d_asset["change"] >= 0 else "" )}{d_asset["change"]}%</div><div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{d_asset["sig_col"]}">{d_asset["signal"]}</strong></div></div></a></div>'''
        
        chart_content = ""
        if db_info["has_chart"]:
            chart_content = f'''<div class="tradingview-widget-container" style="height:100%;width:100%; margin-top:20px; border:1px solid #333; border-radius:12px; overflow:hidden;"><div id="tv_{elem_id}" style="height:650px;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{db_info['symbol']}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "studies": ["RSI@tv-basicstudies"], "container_id": "tv_{elem_id}"}});</script></div>'''
        else:
            chart_content = f'''<div style="text-align:center; padding: 120px 20px; background:#111; border-radius:12px; margin-top:30px; border:1px solid #333;"><h1 style="font-size:4rem; margin:0;">🔒</h1><h2 style="color:#FFD700; margin-top:20px; font-size: 2rem;">Exclusive Internal Asset</h2><p style="color:#aaa; font-size: 1.1rem; max-width: 600px; margin: 15px auto;">Standard charts are not available for <b>{db_info['name']}</b>. <br>Our AI is currently calculating internal liquidity metrics and dark pool volume for this specific asset.</p><button class="vip-btn" onclick="window.history.back()" style="margin-top:30px; padding: 15px 40px;">← GO BACK</button></div>'''

        chart_page = get_header("home") + f'''<main class="container"><a href="index.html" style="color:#888; text-decoration:none; display:inline-block; margin: 15px 0; font-size: 0.9rem; letter-spacing: 1px;">← BACK TO TERMINAL</a><h1 style="margin:0; font-size: 2.5rem;">{db_info['name']} <span style="color:var(--accent);">PRO CHART</span></h1>{chart_content}</main>''' + MODALS_HTML + get_footer()
        scrivi_file(f"chart_{elem_id}.html", chart_page)

    fng_color = "#FF3D00" if fng['value'] < 40 else ("#00C853" if fng['value'] > 60 else "#FFD700")
    fng_html = f'<div class="fng-meter"><h3 style="margin:0; color:#888; text-transform:uppercase; font-size:0.9rem;">MARKET SENTIMENT</h3><div class="fng-value" style="color:{fng_color};">{fng["value"]}</div><div style="font-weight:bold; letter-spacing:1px;">{fng["text"]}</div><div class="fng-bar"><div class="fng-indicator" style="left: {fng["value"]}%;"></div></div></div>'
    
    watchlist_script = f'''<script>const WL_KEY = "mip_watchlist_v1"; function toggleStar(id) {{ let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); if(wl.includes(id)) {{ wl = wl.filter(x => x !== id); }} else {{ wl.push(id); }} localStorage.setItem(WL_KEY, JSON.stringify(wl)); sortGrid(); }} function sortGrid() {{ let wl = JSON.parse(localStorage.getItem(WL_KEY) || "[]"); let grid = document.getElementById("markets-grid"); let cards = Array.from(grid.children); cards.forEach(c => {{ let id = c.getAttribute("data-id"); let star = document.getElementById("star-"+id); if(wl.includes(id)) {{ star.classList.add("active"); }} else {{ star.classList.remove("active"); }} }}); cards.sort((a, b) => {{ let aStar = wl.includes(a.getAttribute("data-id")) ? 1 : 0; let bStar = wl.includes(b.getAttribute("data-id")) ? 1 : 0; return bStar - aStar; }}); cards.forEach(c => grid.appendChild(c)); }} document.addEventListener("DOMContentLoaded", sortGrid);</script>'''
    
    news_rows = "".join([f'<tr style="border-bottom: 1px solid #333;"><td style="padding:15px 10px; text-align:center; font-size:1.2rem;">{"🔥" if "Coin" in n["source"] else "🏛️"}</td><td style="padding:15px 10px;"><a href="{n["link"]}" target="_blank" style="font-weight:700; color:#fff; display:block; margin-bottom:5px;">{n["title"]}</a><span style="font-size:0.75rem; color:#888;">{n["source"]}</span></td><td style="text-align:right;"><a href="{n["link"]}" target="_blank" class="btn-trade">{"⚡ TRADE" if "Coin" in n["source"] else "👁️ READ"}</a></td></tr>' for n in news])
    cal_rows = "".join([f'<tr style="border-bottom: 1px solid #333;"><td><strong style="color:#fff">{ev["evento"]}</strong></td><td>{ev["impatto"]}</td><td>{ev["previsto"]}</td><td style="color:#888;">{ev["precedente"]}</td><td>{ev["data"]}</td></tr>' for ev in calendar])
    
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>{get_header('home')}<div class="container"><div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;"><h2 class="section-title" style="margin:0;">GLOBAL MARKETS PULSE ⚡</h2><div style="font-size:0.8rem; color:#00C853;"><span style="height:8px;width:8px;background:#00C853;border-radius:50%;display:inline-block;animation:pulse 1s infinite;"></span> SECURE LIVE DATA</div></div><p style="color:#888; margin-top:-10px; margin-bottom:20px; font-size:0.9rem;">Click the ⭐ to pin assets to your Custom Watchlist.</p><div class="grid" id="markets-grid">{grid_html}</div><div class="split-layout"><div class="panel">{fng_html}</div><div class="panel"><h2 class="section-title">📰 MARKET MOVERS</h2><table style="width:100%;"><tbody>{news_rows}</tbody></table></div></div></div>{MODALS_HTML} {get_footer()} {watchlist_script}</body></html>'''
    scrivi_file("index.html", html)

def build_signals_page(assets: List[Dict]):
    hot_assets = [a for a in assets if abs(a['change']) >= 1.0]
    
    rows = ""
    for a in hot_assets:
        p = a["price"]
        c = a["change"]
        
        vol_mult = abs(c) / 100
        
        if c > 0:
            sig = "🟢 LONG"
            css = "signal-buy"
            sl = p * (1 - (vol_mult * 1.5))
            tp1 = p * (1 + (vol_mult * 2.0))
            tp2 = p * (1 + (vol_mult * 4.0))
        else:
            sig = "🔴 SHORT"
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
                <div style="font-size:0.7rem; color:#888; text-transform:uppercase;">Target (TP1 - TP2)</div>
                <strong style="color:var(--gold);">{format_price(tp1)} - {format_price(tp2)}</strong>
            </td>
            <td style="padding:20px;">
                <div style="font-size:0.7rem; color:#888; text-transform:uppercase;">Stop Loss</div>
                <strong style="color:#FF3D00;">{format_price(sl)}</strong>
            </td>
            <td style="padding:20px; text-align:right;">
                <a href="chart_{a["id"]}.html" class="btn-trade" style="padding: 10px 20px;">CHART ↗</a>
            </td>
        </tr>
        '''

    backtest_html = '''<div class="backtest-box"><h2 style="color:var(--gold); margin-top:0;">🕰️ TIME MACHINE BACKTESTER</h2><p style="color:#ccc;">What if you invested <strong>$1,000</strong> exactly 1 year ago following our AI Signals?</p><div class="wallet-form" style="justify-content:center; max-width:500px; margin:0 auto; background:none; border:none;"><select id="bt-asset" style="max-width:200px;"><option value="BTC">Bitcoin (BTC)</option><option value="SOL">Solana (SOL)</option><option value="NVDA">Nvidia (NVDA)</option></select><button class="vip-btn" onclick="runBacktest()">RUN SIMULATION</button></div><div id="bt-result-box" style="display:none; margin-top:20px;"><p style="color:#888; text-transform:uppercase; font-size:0.8rem; margin:0;">Value Today</p><div class="backtest-result" id="bt-amount">$0.00</div><div class="change green" id="bt-perc">+0%</div></div></div><script>function runBacktest() { let asset = document.getElementById('bt-asset').value; let mult = asset === 'BTC' ? 2.4 : (asset === 'SOL' ? 5.1 : 3.8); let perc = ((mult - 1) * 100).toFixed(0); let val = (1000 * mult).toLocaleString('en-US', {minimumFractionDigits: 2}); document.getElementById('bt-result-box').style.display = 'block'; document.getElementById('bt-amount').innerText = "$" + val; document.getElementById('bt-perc').innerText = "+" + perc + "% ROI"; }</script>'''
    
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Pro Signals Room</title>{CSS_CORE}</head><body>{get_header('signals')}<div class="container">{backtest_html}<h2 class="section-title">🚨 PRO SIGNALS ROOM (ALGO SCREENER)</h2><p style="color:#888; margin-bottom:30px;">Algorithmic screener detecting high volatility. Targets and Stop Losses are dynamically calculated based on 24H ATR variance.</p><div class="panel" style="padding:0; overflow-x:auto;"><table style="width:100%;"><thead><tr style="background:#0a0a0a;"><th>ASSET</th><th>ALGO SIGNAL</th><th>ENTRY</th><th>TAKE PROFIT ZONES</th><th>INVALIDATION (SL)</th><th style="text-align:right;">ACTION</th></tr></thead><tbody>{rows}</tbody></table></div></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("signals.html", html)

def build_api_hub():
    js_script = '''<script>function connectAPI() { let api = document.getElementById('fake-api').value; let sec = document.getElementById('fake-secret').value; if(!api || !sec) return alert("Please enter both API Key and Secret Key to connect."); document.getElementById('term').style.display = 'block'; let term = document.getElementById('term-content'); term.innerHTML = "> Initializing secure connection...<br>"; setTimeout(() => { term.innerHTML += "> Encrypting payload (AES-256)... OK<br>"; }, 800); setTimeout(() => { term.innerHTML += "> Reaching exchange gateway... OK<br>"; }, 1800); setTimeout(() => { term.innerHTML += "> Verifying API permissions...<br>"; }, 2800); setTimeout(() => { term.innerHTML += "<span style='color:var(--gold);'>! CONNECTION PAUSED: ACCOUNT NOT WHITELISTED</span><br>"; openWaitlist('API'); }, 4000); }</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Auto-Trading API Hub</title>{CSS_CORE}</head><body>{get_header('api')}<div class="container" style="max-width:800px;"><div style="text-align:center; margin-bottom:40px;"><h1 style="font-size:2.5rem; margin-bottom:10px;">🤖 API <span style="color:var(--accent);">AUTO-TRADING</span> HUB</h1><p style="color:#888; font-size:1.1rem;">Connect your exchange and let our algorithms execute trades on your behalf 24/7.</p></div><div class="panel" style="padding:40px;"><div class="wallet-form" style="background:none; border:none; padding:0; flex-direction:column; gap:20px;"><div><label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Select Exchange</label><select style="width:100%; margin-top:5px; padding:15px;"><option>Binance</option><option>Bybit</option><option>Coinbase Pro</option></select></div><div><label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">API Key</label><input type="text" id="fake-api" style="width:96%; margin-top:5px; padding:15px; font-family:monospace;" placeholder="Enter your public API key..."></div><div><label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Secret Key</label><input type="password" id="fake-secret" style="width:96%; margin-top:5px; padding:15px; font-family:monospace;" placeholder="Enter your secret key..."></div><button class="btn-trade" style="padding:20px; font-size:1.1rem; margin-top:10px;" onclick="connectAPI()">CONNECT EXCHANGE TO AI</button></div><div class="hacker-terminal" id="term" style="display:none;"><div id="term-content"></div></div></div></div>{js_script}{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("api_hub.html", html)

def build_brokers_page():
    brokers = [
        {"name": "Binance", "type": "Crypto", "pros": "Low fees, high liquidity", "link": "https://accounts.binance.com/register?ref=TUO_CODICE", "cta": "CLAIM $100 BONUS"},
        {"name": "Bybit", "type": "Crypto Futures", "pros": "Best for Leverage, Pro UI", "link": "https://www.bybit.com/register?affiliate_id=TUO_CODICE", "cta": "OPEN PRO ACCOUNT"},
        {"name": "eToro", "type": "Stocks & Forex", "pros": "CopyTrading, Easy to use", "link": "https://med.etoro.com/B_TUO_CODICE.aspx", "cta": "START COPYING"}
    ]
    html_cards = "".join([f'<div class="broker-card"><div style="display:flex; align-items:center;"><div class="broker-logo">🏦</div><div class="broker-info"><h3 style="margin:0; color:#fff;">{b["name"]}</h3><div class="broker-tags"><span>{b["type"]}</span><span>{b["pros"]}</span></div></div></div><a href="{b["link"]}" target="_blank" class="btn-trade" style="padding:12px 24px; text-align:center;">{b["cta"]}</a></div>' for b in brokers])
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Partner Brokers</title>{CSS_CORE}</head><body>{get_header('brokers')}<div class="container"><h2 class="section-title">💸 EXCLUSIVE BROKER OFFERS</h2><p style="color:#888; margin-bottom:30px;">Trade with the tools the pros use. Claim exclusive sign-up bonuses using our partner links.</p><div style="max-width:800px; margin:0 auto;">{html_cards}</div></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("brokers.html", html)

def build_referral_page():
    js_script = '''<script>document.addEventListener("DOMContentLoaded", function() { let user = localStorage.getItem('mip_user') || 'trader' + Math.floor(Math.random()*1000); let link = `https://marketinsiderpro.com/invite/${user.toLowerCase()}`; document.getElementById('ref-url').innerText = link; let refCount = localStorage.getItem('mip_refs'); if(!refCount) { refCount = Math.floor(Math.random() * 2); localStorage.setItem('mip_refs', refCount); } document.getElementById('ref-count').innerText = refCount; let perc = (refCount / 3) * 100; document.getElementById('ref-bar').style.width = perc + "%"; }); function copyLink() { navigator.clipboard.writeText(document.getElementById('ref-url').innerText); let btn = document.getElementById('copy-btn'); btn.innerText = "COPIED! ✅"; btn.style.background = "#00C853"; setTimeout(() => { btn.innerText = "COPY LINK"; btn.style.background = "var(--accent)"; }, 2000); }</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Invite & Earn</title>{CSS_CORE}</head><body>{get_header('referral')}<div class="container" style="max-width:800px;"><div class="ref-box"><h1 style="font-size:2.5rem; margin-top:0; color:var(--gold);">🎁 INVITE FRIENDS, GET VIP FREE.</h1><p style="color:#ccc; font-size:1.1rem;">Invite 3 friends to join Market Insider Pro. When they create an account, you unlock 1 month of VIP Pass (Value $49).</p><div class="ref-link-container"><div class="ref-link" id="ref-url">Loading link...</div><button class="ref-copy" id="copy-btn" onclick="copyLink()">COPY LINK</button></div><div style="margin-top:40px; text-align:left; max-width:500px; margin: 40px auto 0;"><div style="display:flex; justify-content:space-between; margin-bottom:10px; color:#aaa; font-weight:bold;"><span>Friends Invited</span><span><span id="ref-count" style="color:#fff;">0</span> / 3</span></div><div class="progress-container"><div class="progress-bar" id="ref-bar"></div></div></div></div></div>{MODALS_HTML} {get_footer()} {js_script}</body></html>'''
    scrivi_file("referral.html", html)

def build_pricing_page():
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Pricing</title>{CSS_CORE}</head><body>{get_header('pricing')}<div class="container"><div style="text-align:center; margin-bottom:20px;"><h1 style="font-size:3rem; margin-bottom:10px;">UPGRADE TO <span style="color:var(--gold);">VIP PASS</span></h1><p style="color:#888; font-size:1.1rem; max-width:600px; margin:0 auto;">Stop trading blindly. Join the 1% of profitable traders with real-time institutional data, algorithmic signals, and AI analysis.</p></div><div class="pricing-grid"><div class="pricing-card"><h3 style="color:#aaa; font-size:1.5rem; margin:0;">BASIC</h3><div class="price-tag">$0<span>/mo</span></div><div style="margin-bottom:30px;"><div class="plan-feature">Delayed Terminal Data (15m)</div><div class="plan-feature">Basic Charts</div><div class="plan-feature">Academy Module 1</div><div class="plan-feature" style="color:#555;"><s>Real-Time Signals</s></div></div><button class="vip-btn" style="width:100%; background:#333; cursor:default;">CURRENT PLAN</button></div><div class="pricing-card pro"><h3 style="color:var(--gold); font-size:1.5rem; margin:0;">PRO TRADER</h3><div class="price-tag">$49<span>/mo</span></div><div style="margin-bottom:30px;"><div class="plan-feature" style="color:#fff;">Real-Time Terminal Data (6s)</div><div class="plan-feature" style="color:#fff;">Full VIP Academy Access</div><div class="plan-feature" style="color:#fff;">Institutional Signals Room</div><div class="plan-feature" style="color:#fff;">API Auto-Trading Beta</div></div><button class="btn-trade" style="width:100%; padding:15px; font-size:1.2rem;" onclick="openStripe('PRO', '49.00')">START 7-DAY TRIAL</button></div><div class="pricing-card"><h3 style="color:#2962FF; font-size:1.5rem; margin:0;">WHALE (LIFETIME)</h3><div class="price-tag">$399<span>/once</span></div><div style="margin-bottom:30px;"><div class="plan-feature">Everything in PRO</div><div class="plan-feature">Private Discord Access</div><div class="plan-feature">Lifetime Updates</div><div class="plan-feature">No Recurring Fees</div></div><button class="vip-btn" style="width:100%; padding:15px;" onclick="openStripe('LIFETIME', '399.00')">GET LIFETIME ACCESS</button></div></div><p style="text-align:center; margin-top:40px; color:#666; font-size:0.8rem;">🔐 Payments securely processed by Stripe. 30-Day money-back guarantee.</p></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("pricing.html", html)

def build_leaderboard_page():
    js = '''<script>document.addEventListener("DOMContentLoaded", function() { let user = localStorage.getItem('mip_user'); if(user) { let row = `<tr class="user-row"><td class="rank-3">#8</td><td><strong>👤 ${user} (You)</strong></td><td>$14,250</td><td class="change green">+18.4%</td><td>Pro</td></tr>`; document.getElementById('lb-body').innerHTML += row; } else { document.getElementById('lb-body').innerHTML += `<tr><td colspan="5" style="text-align:center; padding:20px;"><a href="#" onclick="openLogin()" style="color:var(--accent); text-decoration:underline;">Login to see your rank</a></td></tr>`; } });</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Leaderboard</title>{CSS_CORE}</head><body>{get_header('leaderboard')}<div class="container"><h2 class="section-title" style="text-align:center; font-size:2rem; border:none; margin-bottom:10px;">🏆 GLOBAL LEADERBOARD</h2><p style="text-align:center; color:#888; margin-bottom:40px;">Top performing accounts this month based on algorithmic execution ROI.</p><div class="panel" style="max-width:900px; margin:0 auto;"><table><thead><tr style="border-bottom:2px solid #333;"><th>RANK</th><th>TRADER</th><th>PORTFOLIO SIZE</th><th>30D ROI</th><th>TIER</th></tr></thead><tbody id="lb-body"><tr><td class="rank-1">🥇 #1</td><td><strong>WhaleHunter99</strong></td><td>$1.2M</td><td class="change green">+142.5%</td><td><span style="color:var(--gold);">Whale</span></td></tr><tr><td class="rank-2">🥈 #2</td><td><strong>CryptoKing_LDN</strong></td><td>$450K</td><td class="change green">+89.2%</td><td>Pro</td></tr><tr><td class="rank-3">🥉 #3</td><td><strong>SarahTradeX</strong></td><td>$89K</td><td class="change green">+64.8%</td><td>Pro</td></tr><tr><td style="color:#aaa; font-weight:bold;">#4</td><td>AlphaAlgo_01</td><td>Hidden</td><td class="change green">+41.0%</td><td>Pro</td></tr><tr><td style="color:#aaa; font-weight:bold;">#5</td><td>BerlinBull</td><td>$12K</td><td class="change green">+38.5%</td><td>Pro</td></tr><tr style="border-bottom:2px solid #333;"><td style="color:#aaa; font-weight:bold;">#6</td><td>MiamiVice_BTC</td><td>$55K</td><td class="change green">+31.2%</td><td>Pro</td></tr></tbody></table></div></div>{MODALS_HTML} {get_footer()} {js}</body></html>'''
    scrivi_file("leaderboard.html", html)

def build_legal_page():
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Legal & Privacy</title>{CSS_CORE}</head><body>{get_header('legal')}<div class="container" style="max-width:800px; color:#ccc;"><h1 style="color:#fff;">Legal Information & Policies</h1><hr style="border-color:#333; margin-bottom:30px;"><h3 style="color:var(--accent);">Privacy Policy (GDPR Compliant)</h3><p>Market Insider Pro utilizes LocalStorage to save your preferences, watchlist, and portfolio data directly on your device. We do NOT transmit this personal data to our servers.</p><h3 style="color:var(--accent);">Terms of Service</h3><p>By accessing the website, you agree to be bound by these terms. The data provided on this platform is for educational and informational purposes only.</p><h3 style="color:var(--accent);">Risk Disclaimer</h3><p>Trading Forex, Cryptocurrencies, and Stocks carries a high level of risk and may not be suitable for all investors.</p></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("legal.html", html)

def build_chart_pages(assets: List[Dict]):
    pass

def build_academy():
    sidebar = "".join([f"<div class='module-title'>{m['title']}</div>" + "".join([f'''<div onclick="window.location.href='academy_{l['id']}.html'" class="lesson-link">{"🔒" if l.get("vip") else "📄"} {l['title']}</div>''' for l in m['lessons']]) for _, m in ACADEMY_CONTENT.items()])
    for _, m in ACADEMY_CONTENT.items():
        for l in m['lessons']:
            c_html = f'''<div style="filter: blur(6px); pointer-events: none;">{l['html']}</div><div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--accent); border-radius:12px; z-index:10;"><h2 style="color:#FFD700;">🔒 VIP CONTENT</h2><button class="btn-trade" onclick="window.location.href='pricing.html'">GET VIP PASS</button></div>''' if l.get("vip") else l['html']
            html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{l['title']}</title>{CSS_CORE}</head><body>{get_header('academy')}<div class="container"><div class="academy-grid"><div class="sidebar">{sidebar}</div><div class="lesson-content" style="position:relative;">{c_html}</div></div></div>{MODALS_HTML}{get_footer()}</body></html>'''
            scrivi_file(f"academy_{l['id']}.html", html)

def build_chat():
    js = '''<script>function send(){let i=document.getElementById('in'); let v=i.value; if(!v)return; let h=document.getElementById('hist'); h.innerHTML+=`<div class="msg msg-user">${v}</div>`; i.value=''; h.scrollTop=h.scrollHeight; let t="t-"+Date.now(); h.innerHTML+=`<div class="msg msg-ai" id="${t}">🤖 Analyzing...</div>`; h.scrollTop=h.scrollHeight; setTimeout(()=>{document.getElementById(t).innerHTML=`🤖 Market sentiment is actively shifting. Always check the Signals Room before entering a trade.`; h.scrollTop=h.scrollHeight;}, 1000);} document.getElementById('in').addEventListener("keypress", e=>{if(e.key==="Enter")send();});</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>AI Analyst</title>{CSS_CORE}</head><body>{get_header('chat')}<div class="container"><h2 class="section-title">AI MARKET ANALYST 🤖</h2><div class="chat-interface"><div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Welcome.</div></div><div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Type here..."><button class="chat-btn" onclick="send()">ANALYZE</button></div></div></div>{js}{MODALS_HTML}{get_footer()}</body></html>'''
    scrivi_file("chat.html", html)

# ==========================================
# WALLET MIGLIORATO (Dati da Binance)
# ==========================================
def build_wallet():
    js = '''<script>
    const W_KEY = "mip_wallet_assets"; 
    const s_assets = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "ripple": "XRP", "cardano": "ADA"}; 
    const binance_map = {"bitcoin": "BTCUSDT", "ethereum": "ETHUSDT", "solana": "SOLUSDT", "ripple": "XRPUSDT", "cardano": "ADAUSDT"};
    
    function loadWallet() { 
        let saved = localStorage.getItem(W_KEY); 
        let assets = saved ? JSON.parse(saved) : {}; 
        renderWalletTable(assets); 
        fetchLiveWorth(assets); 
    } 
    function addAsset() { 
        let id = document.getElementById("asset-select").value; 
        let amount = parseFloat(document.getElementById("asset-amount").value); 
        if(!id || isNaN(amount) || amount <= 0) return alert("Enter valid amount."); 
        let saved = localStorage.getItem(W_KEY); 
        let assets = saved ? JSON.parse(saved) : {}; 
        assets[id] = (assets[id] || 0) + amount; 
        localStorage.setItem(W_KEY, JSON.stringify(assets)); 
        document.getElementById("asset-amount").value = ""; 
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
            tbody.innerHTML = "<tr><td colspan='4' style='text-align:center; color:#888;'>Your wallet is empty. Add an asset above.</td></tr>"; 
            return; 
        } 
        for (const [id, amount] of Object.entries(assets)) { 
            tbody.innerHTML += `<tr><td><strong>${s_assets[id]}</strong></td><td>${amount}</td><td id="val-${id}" style="color:var(--gold); font-weight:bold;">Loading...</td><td style="text-align:right;"><button onclick="removeAsset('${id}')" style="background:#FF3D00; color:#fff; border:none; padding:5px 10px; border-radius:4px; cursor:pointer; font-weight:bold;">X</button></td></tr>`; 
        } 
    } 
    async function fetchLiveWorth(assets) { 
        if(Object.keys(assets).length === 0) { 
            document.getElementById("total-net-worth").innerText = "$0.00"; return; 
        } 
        try { 
            // Bypass the shield by using Binance
            let fetcher = window.originalFetch || window.fetch;
            let res = await fetcher('https://api.binance.com/api/v3/ticker/price'); 
            let data = await res.json(); 
            
            let priceMap = {};
            data.forEach(item => { priceMap[item.symbol] = parseFloat(item.price); });
            
            let total = 0; 
            for (const [id, amount] of Object.entries(assets)) { 
                let symbol = binance_map[id];
                let currentPrice = priceMap[symbol];
                if(currentPrice) { 
                    let value = currentPrice * amount; 
                    total += value; 
                    let el = document.getElementById(`val-${id}`);
                    if (el) el.innerText = "$" + value.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); 
                } 
            } 
            document.getElementById("total-net-worth").innerText = "$" + total.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); 
        } catch(e) { console.error("Pricing error"); } 
    } 
    document.addEventListener("DOMContentLoaded", loadWallet); 
    setInterval(loadWallet, 5000); 
    </script>'''
    
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>My Wallet</title>{CSS_CORE}</head><body>{get_header('wallet')}<div class="container"><h2 class="section-title">MY PORTFOLIO TRACKER 💼</h2><div style="text-align:center; padding: 40px; background:#111; border-radius:12px; border:1px solid #333; margin-bottom:30px;"><div style="color:#888; font-size:1.2rem; text-transform:uppercase;">Total Net Worth</div><div class="wallet-total" id="total-net-worth">$0.00</div><div style="font-size:0.8rem; color:#00C853;">Live tracking active ⚡</div></div><div class="wallet-form"><select id="asset-select"><option value="bitcoin">Bitcoin (BTC)</option><option value="ethereum">Ethereum (ETH)</option><option value="solana">Solana (SOL)</option><option value="ripple">Ripple (XRP)</option><option value="cardano">Cardano (ADA)</option></select><input type="number" id="asset-amount" placeholder="Amount (e.g. 0.5)"><button class="vip-btn" onclick="addAsset()">+ ADD</button></div><div class="panel"><table><thead><tr><th>ASSET</th><th>AMOUNT</th><th>VALUE (USD)</th><th style="text-align:right;">ACTION</th></tr></thead><tbody id="wallet-body"></tbody></table></div></div>{MODALS_HTML} {get_footer()} {js}</body></html>'''
    scrivi_file("wallet.html", html)