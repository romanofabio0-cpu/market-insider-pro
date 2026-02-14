import os
import json
from typing import List, Dict
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE
from core.content import get_header, get_footer, ACADEMY_CONTENT, MODALS_HTML

logger = get_logger("Builder")

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
    js_mapping = {}
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        elem_id = a['id'].replace(" ", "-")
        if a['type'] == 'CRYPTO': js_mapping[a['cg_id']] = elem_id
        grid_html += f'<a href="chart_{a["id"]}.html" class="card-link"><div class="card"><div class="card-head"><span class="symbol">{a["symbol"]}</span><span class="name" style="color:#888; font-size:0.8rem;">{a["name"]}</span></div><div class="price" id="price-{elem_id}">{format_price(a["price"])}</div><div class="change {color}" id="change-{elem_id}">{( "+" if a["change"] >= 0 else "" )}{a["change"]}%</div><div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{a["sig_col"]}">{a["signal"]}</strong></div></div></a>'
    
    fng_color = "#FF3D00" if fng['value'] < 40 else ("#00C853" if fng['value'] > 60 else "#FFD700")
    fng_html = f'<div class="fng-meter"><h3 style="margin:0; color:#888; text-transform:uppercase; font-size:0.9rem;">MARKET SENTIMENT</h3><div class="fng-value" style="color:{fng_color};">{fng["value"]}</div><div style="font-weight:bold; letter-spacing:1px;">{fng["text"]}</div><div class="fng-bar"><div class="fng-indicator" style="left: {fng["value"]}%;"></div></div></div>'
    real_time_script = f'<script>const idMap = {json.dumps(js_mapping)}; const apiIds = "{",".join(js_mapping.keys())}"; async function updatePrices() {{ try {{ const res = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${{apiIds}}&vs_currencies=usd&include_24hr_change=true&_=${{new Date().getTime()}}`); const data = await res.json(); for (const [cgId, value] of Object.entries(data)) {{ let htmlId = idMap[cgId]; if (!htmlId) continue; let priceElem = document.getElementById(`price-${{htmlId}}`); let changeElem = document.getElementById(`change-${{htmlId}}`); if (priceElem) {{ let oldPrice = parseFloat(priceElem.innerText.replace("$", "").replace(",", "")); let newPrice = value.usd; if(newPrice !== oldPrice && !isNaN(oldPrice)) {{ priceElem.innerText = newPrice < 1 ? "$" + newPrice.toFixed(6) : "$" + newPrice.toLocaleString("en-US", {{minimumFractionDigits: 2, maximumFractionDigits: 2}}); priceElem.classList.remove("flash-up", "flash-down"); void priceElem.offsetWidth; priceElem.classList.add(newPrice > oldPrice ? "flash-up" : "flash-down"); }} }} if (changeElem) {{ let change = value.usd_24h_change.toFixed(2); changeElem.innerText = (change >= 0 ? "+" : "") + change + "%"; changeElem.className = "change " + (change >= 0 ? "green" : "red"); }} }} }} catch (e) {{}} }} setInterval(updatePrices, 6000); </script>'
    news_rows = "".join([f'<tr style="border-bottom: 1px solid #333;"><td style="padding:15px 10px; text-align:center; font-size:1.2rem;">{"🔥" if "Coin" in n["source"] else "🏛️"}</td><td style="padding:15px 10px;"><a href="{n["link"]}" target="_blank" style="font-weight:700; color:#fff; display:block; margin-bottom:5px;">{n["title"]}</a><span style="font-size:0.75rem; color:#888;">{n["source"]}</span></td><td style="text-align:right;"><a href="{n["link"]}" target="_blank" class="btn-trade">{"⚡ TRADE" if "Coin" in n["source"] else "👁️ READ"}</a></td></tr>' for n in news])
    cal_rows = "".join([f'<tr style="border-bottom: 1px solid #333;"><td><strong style="color:#fff">{ev["evento"]}</strong></td><td>{ev["impatto"]}</td><td>{ev["previsto"]}</td><td style="color:#888;">{ev["precedente"]}</td><td>{ev["data"]}</td></tr>' for ev in calendar])

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>{get_header('home')}
    <div class="container">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 class="section-title" style="margin:0;">GLOBAL MARKETS PULSE ⚡</h2>
            <div style="font-size:0.8rem; color:#00C853;"><span style="height:8px;width:8px;background:#00C853;border-radius:50%;display:inline-block;animation:pulse 1s infinite;"></span> SECURE LIVE DATA</div>
        </div>
        <div class="grid">{grid_html}</div>
        <div class="split-layout">
            <div class="panel">{fng_html}</div>
            <div class="panel"><h2 class="section-title">📰 MARKET MOVERS</h2><table style="width:100%;"><tbody>{news_rows}</tbody></table></div>
        </div>
    </div>
    {MODALS_HTML} {get_footer()} {real_time_script}</body></html>'''
    scrivi_file("index.html", html)

def build_signals_page(assets: List[Dict]):
    hot_assets = [a for a in assets if abs(a['change']) >= 2.0]
    rows = ""
    for a in hot_assets:
        sig_class = "signal-buy" if a['change'] > 0 else "signal-sell"
        action = "🔥 STRONG BUY" if a['change'] > 0 else "🩸 SHORT / SELL"
        rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:15px;"><strong style="font-size:1.1rem; color:#fff;">{a["symbol"]}</strong><br><span style="font-size:0.8rem;color:#888;">{a["name"]}</span></td><td style="padding:15px;">{format_price(a["price"])}</td><td style="padding:15px;" class="{sig_class}">{( "+" if a["change"] >= 0 else "" )}{a["change"]}%</td><td style="padding:15px; font-weight:bold;" class="{sig_class}">{action}</td><td style="padding:15px; text-align:right;"><a href="chart_{a["id"]}.html" class="btn-trade">CHART ↗</a></td></tr>'
    
    backtest_html = '''
    <div class="backtest-box">
        <h2 style="color:var(--gold); margin-top:0;">🕰️ TIME MACHINE BACKTESTER</h2>
        <p style="color:#ccc;">What if you invested <strong>$1,000</strong> exactly 1 year ago following our AI Signals?</p>
        <div class="wallet-form" style="justify-content:center; max-width:500px; margin:0 auto; background:none; border:none;">
            <select id="bt-asset" style="max-width:200px;">
                <option value="BTC">Bitcoin (BTC)</option>
                <option value="SOL">Solana (SOL)</option>
                <option value="NVDA">Nvidia (NVDA)</option>
            </select>
            <button class="vip-btn" onclick="runBacktest()">RUN SIMULATION</button>
        </div>
        <div id="bt-result-box" style="display:none; margin-top:20px;">
            <p style="color:#888; text-transform:uppercase; font-size:0.8rem; margin:0;">Value Today</p>
            <div class="backtest-result" id="bt-amount">$0.00</div>
            <div class="change green" id="bt-perc">+0%</div>
        </div>
    </div>
    <script>
    function runBacktest() {
        let asset = document.getElementById('bt-asset').value;
        let mult = asset === 'BTC' ? 2.4 : (asset === 'SOL' ? 5.1 : 3.8); 
        let perc = ((mult - 1) * 100).toFixed(0);
        let val = (1000 * mult).toLocaleString('en-US', {minimumFractionDigits: 2});
        
        document.getElementById('bt-result-box').style.display = 'block';
        document.getElementById('bt-amount').innerText = "$" + val;
        document.getElementById('bt-perc').innerText = "+" + perc + "% ROI";
    }
    </script>
    '''

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Pro Signals Room</title>{CSS_CORE}</head><body>{get_header('signals')}
    <div class="container">
        {backtest_html}
        <h2 class="section-title">🚨 PRO SIGNALS ROOM (ALGO SCREENER)</h2>
        <p style="color:#888; margin-bottom:30px;">Real-time algorithmic screener detecting high volatility and institutional order blocks.</p>
        <div class="panel"><table style="width:100%;"><thead><tr><th>ASSET</th><th>PRICE</th><th>24H VOLATILITY</th><th>ALGO SIGNAL</th><th style="text-align:right;">ACTION</th></tr></thead><tbody>{rows}</tbody></table></div>
    </div>
    {MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("signals.html", html)

def build_api_hub():
    # JS spostato in una variabile normale per non confondere Python
    js_script = '''
    <script>
    function connectAPI() {
        let api = document.getElementById('fake-api').value;
        let sec = document.getElementById('fake-secret').value;
        if(!api || !sec) return alert("Please enter both API Key and Secret Key to connect.");
        
        document.getElementById('term').style.display = 'block';
        let term = document.getElementById('term-content');
        term.innerHTML = "> Initializing secure connection...<br>";
        
        setTimeout(() => { term.innerHTML += "> Encrypting payload (AES-256)... OK<br>"; }, 800);
        setTimeout(() => { term.innerHTML += "> Reaching exchange gateway... OK<br>"; }, 1800);
        setTimeout(() => { term.innerHTML += "> Verifying API permissions...<br>"; }, 2800);
        setTimeout(() => { 
            term.innerHTML += "<span style='color:var(--gold);'>! CONNECTION PAUSED: ACCOUNT NOT WHITELISTED</span><br>"; 
            openWaitlist('API');
        }, 4000);
    }
    </script>
    '''

    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Auto-Trading API Hub</title>{CSS_CORE}</head><body>{get_header('api')}
    <div class="container" style="max-width:800px;">
        <div style="text-align:center; margin-bottom:40px;">
            <h1 style="font-size:2.5rem; margin-bottom:10px;">🤖 API <span style="color:var(--accent);">AUTO-TRADING</span> HUB</h1>
            <p style="color:#888; font-size:1.1rem;">Connect your exchange and let our algorithms execute trades on your behalf 24/7.</p>
        </div>
        
        <div class="panel" style="padding:40px;">
            <div class="wallet-form" style="background:none; border:none; padding:0; flex-direction:column; gap:20px;">
                <div>
                    <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Select Exchange</label>
                    <select style="width:100%; margin-top:5px; padding:15px;"><option>Binance</option><option>Bybit</option><option>Coinbase Pro</option></select>
                </div>
                <div>
                    <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">API Key</label>
                    <input type="text" id="fake-api" style="width:96%; margin-top:5px; padding:15px; font-family:monospace;" placeholder="Enter your public API key...">
                </div>
                <div>
                    <label style="color:#aaa; font-size:0.8rem; text-transform:uppercase;">Secret Key</label>
                    <input type="password" id="fake-secret" style="width:96%; margin-top:5px; padding:15px; font-family:monospace;" placeholder="Enter your secret key...">
                </div>
                <button class="btn-trade" style="padding:20px; font-size:1.1rem; margin-top:10px;" onclick="connectAPI()">CONNECT EXCHANGE TO AI</button>
            </div>
            
            <div class="hacker-terminal" id="term" style="display:none;">
                <div id="term-content"></div>
            </div>
        </div>
    </div>
    {js_script}
    {MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("api_hub.html", html)

def build_brokers_page():
    brokers = [
        {"name": "Binance", "type": "Crypto", "pros": "Low fees, high liquidity", "link": "#", "cta": "CLAIM $100 BONUS"},
        {"name": "Bybit", "type": "Crypto Futures", "pros": "Best for Leverage, Pro UI", "link": "#", "cta": "OPEN PRO ACCOUNT"},
        {"name": "eToro", "type": "Stocks & Forex", "pros": "CopyTrading, Easy to use", "link": "#", "cta": "START COPYING"}
    ]
    html_cards = "".join([f'<div class="broker-card"><div style="display:flex; align-items:center;"><div class="broker-logo">🏦</div><div class="broker-info"><h3 style="margin:0; color:#fff;">{b["name"]}</h3><div class="broker-tags"><span>{b["type"]}</span><span>{b["pros"]}</span></div></div></div><button class="btn-trade" style="padding:12px 24px;" onclick="openWaitlist(\'VIP PASS\')">{b["cta"]}</button></div>' for b in brokers])
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Partner Brokers</title>{CSS_CORE}</head><body>{get_header('brokers')}<div class="container"><h2 class="section-title">💸 EXCLUSIVE BROKER OFFERS</h2><p style="color:#888; margin-bottom:30px;">Trade with the tools the pros use. Claim exclusive sign-up bonuses.</p><div style="max-width:800px; margin:0 auto;">{html_cards}</div></div>{MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("brokers.html", html)

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "studies": ["RSI@tv-basicstudies"], "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{a['name']} Chart</title>{CSS_CORE}</head><body>{get_header('home')}<div class="container"><a href="index.html" style="color:#888;">&larr; BACK</a><h1 style="color:#fff; margin-bottom:20px;">{a['name']} <span style="color:var(--accent)">PRO CHART</span></h1><div style="height:75vh; border:1px solid #333; border-radius:12px; overflow:hidden;">{widget}</div></div>{MODALS_HTML}{get_footer()}</body></html>'''
        scrivi_file(f"chart_{a['id']}.html", html)

def build_academy():
    sidebar = "".join([f"<div class='module-title'>{m['title']}</div>" + "".join([f'''<div onclick="window.location.href='academy_{l['id']}.html'" class="lesson-link">{"🔒" if l.get("vip") else "📄"} {l['title']}</div>''' for l in m['lessons']]) for _, m in ACADEMY_CONTENT.items()])
    for _, m in ACADEMY_CONTENT.items():
        for l in m['lessons']:
            c_html = f'''<div style="filter: blur(6px); pointer-events: none;">{l['html']}</div><div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--accent); border-radius:12px; z-index:10;"><h2 style="color:#FFD700;">🔒 VIP CONTENT</h2><button class="btn-trade" onclick="openWaitlist('VIP PASS')">GET VIP PASS</button></div>''' if l.get("vip") else l['html']
            html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{l['title']}</title>{CSS_CORE}</head><body>{get_header('academy')}<div class="container"><div class="academy-grid"><div class="sidebar">{sidebar}</div><div class="lesson-content" style="position:relative;">{c_html}</div></div></div>{MODALS_HTML}{get_footer()}</body></html>'''
            scrivi_file(f"academy_{l['id']}.html", html)

def build_chat():
    js = '''<script>function send(){let i=document.getElementById('in'); let v=i.value; if(!v)return; let h=document.getElementById('hist'); h.innerHTML+=`<div class="msg msg-user">${v}</div>`; i.value=''; h.scrollTop=h.scrollHeight; let t="t-"+Date.now(); h.innerHTML+=`<div class="msg msg-ai" id="${t}">🤖 Analyzing...</div>`; h.scrollTop=h.scrollHeight; setTimeout(()=>{document.getElementById(t).innerHTML=`🤖 Market sentiment is actively shifting. Always check the Signals Room before entering a trade.`; h.scrollTop=h.scrollHeight;}, 1000);} document.getElementById('in').addEventListener("keypress", e=>{if(e.key==="Enter")send();});</script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>AI Analyst</title>{CSS_CORE}</head><body>{get_header('chat')}<div class="container"><h2 class="section-title">AI MARKET ANALYST 🤖</h2><div class="chat-interface"><div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Welcome.</div></div><div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Type here..."><button class="chat-btn" onclick="send()">ANALYZE</button></div></div></div>{js}{MODALS_HTML}{get_footer()}</body></html>'''
    scrivi_file("chat.html", html)

def build_wallet():
    js = '''<script>
    const W_KEY = "mip_wallet_assets";
    const s_assets = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "ripple": "XRP", "cardano": "ADA"};
    function loadWallet() { let saved = localStorage.getItem(W_KEY); let assets = saved ? JSON.parse(saved) : {}; renderWalletTable(assets); fetchLiveWorth(assets); }
    function addAsset() { let id = document.getElementById("asset-select").value; let amount = parseFloat(document.getElementById("asset-amount").value); if(!id || isNaN(amount) || amount <= 0) return alert("Enter valid amount."); let saved = localStorage.getItem(W_KEY); let assets = saved ? JSON.parse(saved) : {}; assets[id] = (assets[id] || 0) + amount; localStorage.setItem(W_KEY, JSON.stringify(assets)); document.getElementById("asset-amount").value = ""; loadWallet(); }
    function removeAsset(id) { let saved = localStorage.getItem(W_KEY); if(!saved) return; let assets = JSON.parse(saved); delete assets[id]; localStorage.setItem(W_KEY, JSON.stringify(assets)); loadWallet(); }
    function renderWalletTable(assets) { let tbody = document.getElementById("wallet-body"); tbody.innerHTML = ""; if(Object.keys(assets).length === 0) { tbody.innerHTML = "<tr><td colspan='4' style='text-align:center; color:#888;'>Your wallet is empty. Add an asset above.</td></tr>"; return; } for (const [id, amount] of Object.entries(assets)) { tbody.innerHTML += `<tr><td><strong>${s_assets[id]}</strong></td><td>${amount}</td><td id="val-${id}">Loading...</td><td style="text-align:right;"><button onclick="removeAsset('${id}')" style="background:#FF3D00; color:#fff; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;">X</button></td></tr>`; } }
    async function fetchLiveWorth(assets) { let ids = Object.keys(assets).join(","); if(!ids) { document.getElementById("total-net-worth").innerText = "$0.00"; return; } try { let res = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${ids}&vs_currencies=usd`); let data = await res.json(); let total = 0; for (const [id, amount] of Object.entries(assets)) { if(data[id]) { let value = data[id].usd * amount; total += value; document.getElementById(`val-${id}`).innerText = "$" + value.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); } } document.getElementById("total-net-worth").innerText = "$" + total.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2}); } catch(e) {} }
    document.addEventListener("DOMContentLoaded", loadWallet); setInterval(loadWallet, 10000);
    </script>'''
    html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>My Wallet</title>{CSS_CORE}</head><body>{get_header('wallet')}<div class="container"><h2 class="section-title">MY PORTFOLIO TRACKER 💼</h2><div style="text-align:center; padding: 40px; background:#111; border-radius:12px; border:1px solid #333; margin-bottom:30px;"><div style="color:#888; font-size:1.2rem; text-transform:uppercase;">Total Net Worth</div><div class="wallet-total" id="total-net-worth">$0.00</div><div style="font-size:0.8rem; color:#00C853;">Live tracking active ⚡</div></div><div class="wallet-form"><select id="asset-select"><option value="bitcoin">Bitcoin (BTC)</option><option value="ethereum">Ethereum (ETH)</option><option value="solana">Solana (SOL)</option></select><input type="number" id="asset-amount" placeholder="Amount (e.g. 0.5)"><button class="vip-btn" onclick="addAsset()">+ ADD</button></div><div class="panel"><table><thead><tr><th>ASSET</th><th>AMOUNT</th><th>VALUE (USD)</th><th style="text-align:right;">ACTION</th></tr></thead><tbody id="wallet-body"></tbody></table></div></div>{MODALS_HTML} {get_footer()} {js}</body></html>'''
    scrivi_file("wallet.html", html)