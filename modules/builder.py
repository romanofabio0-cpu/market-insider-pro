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
        with open(path, "wb") as f:
            f.write(contenuto.encode('utf-8'))
        logger.info(f"💾 Generato: {nome_file}")
    except IOError as e:
        logger.error(f"❌ Errore scrittura {nome_file}: {e}")

def format_price(price):
    if price < 0.01: return f"${price:.6f}"
    elif price < 1: return f"${price:.4f}"
    else: return f"${price:,.2f}"

def build_index(assets: List[Dict], news: List[Dict], calendar: List[Dict]):
    grid_html = ""
    js_mapping = {}
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        elem_id = a['id'].replace(" ", "-")
        if a['type'] == 'CRYPTO':
            js_mapping[a['cg_id']] = elem_id
        
        grid_html += f'''
        <a href="chart_{a['id']}.html" class="card-link">
            <div class="card">
                <div class="card-head">
                    <span class="symbol">{a['symbol']}</span>
                    <span class="name" style="color:#888; font-size:0.8rem;">{a['name']}</span> 
                </div>
                <div class="price" id="price-{elem_id}">{format_price(a['price'])}</div>
                <div class="change {color}" id="change-{elem_id}">{sign}{a['change']}%</div>
                <div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{a['sig_col']}">{a['signal']}</strong></div>
            </div>
        </a>'''
    
    api_ids = ",".join(js_mapping.keys())
    js_map_str = json.dumps(js_mapping)
    real_time_script = f'''
    <script>
    const idMap = {js_map_str}; 
    const apiIds = "{api_ids}";  
    async function updatePrices() {{
        try {{
            const res = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${{apiIds}}&vs_currencies=usd&include_24hr_change=true&_=${{new Date().getTime()}}`);
            const data = await res.json();
            for (const [cgId, value] of Object.entries(data)) {{
                let htmlId = idMap[cgId]; if (!htmlId) continue;
                let priceElem = document.getElementById(`price-${{htmlId}}`);
                let changeElem = document.getElementById(`change-${{htmlId}}`);
                if (priceElem) {{
                    let oldPrice = parseFloat(priceElem.innerText.replace('$', '').replace(',', ''));
                    let newPrice = value.usd;
                    if(newPrice !== oldPrice && !isNaN(oldPrice)) {{
                        priceElem.innerText = newPrice < 1 ? "$" + newPrice.toFixed(6) : "$" + newPrice.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
                        let flashClass = newPrice > oldPrice ? 'flash-up' : 'flash-down';
                        priceElem.classList.remove('flash-up', 'flash-down');
                        void priceElem.offsetWidth; 
                        priceElem.classList.add(flashClass);
                    }}
                }}
                if (changeElem) {{
                    let change = value.usd_24h_change.toFixed(2);
                    changeElem.innerText = (change >= 0 ? "+" : "") + change + "%";
                    changeElem.className = "change " + (change >= 0 ? "green" : "red");
                }}
            }}
        }} catch (e) {{}}
    }}
    setInterval(updatePrices, 6000);
    </script>'''

    news_rows = ""
    for n in news:
        icon = "🔥" if "Coin" in n['source'] else "🏛️"
        cta_text = "⚡ TRADE NOW" if "Coin" in n['source'] else "👁️ INSIDER VIEW"
        news_rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:15px 10px; width:40px; text-align:center; font-size:1.2rem;">{icon}</td><td style="padding:15px 10px;"><a href="{n["link"]}" target="_blank" style="font-weight:700; color:#fff; text-decoration:none; display:block; margin-bottom:5px; font-size:1rem;">{n["title"]}</a><span style="font-size:0.75rem; color:#888;">{n["source"]} • {n["published"]}</span></td><td style="padding:15px 10px; text-align:right;"><a href="{n["link"]}" target="_blank" class="btn-trade">{cta_text}</a></td></tr>'
    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:10px;"><strong style="color:#fff">{ev["evento"]}</strong></td><td style="padding:10px;">{ev["impatto"]}</td><td style="padding:10px;">{ev["previsto"]}</td><td style="padding:10px; color:#888;">{ev["precedente"]}</td><td style="padding:10px;">{ev["data"]}</td></tr>'

    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 class="section-title" style="margin:0;">GLOBAL MARKETS PULSE ⚡</h2>
            <div style="font-size:0.8rem; color:#00C853;"><span class="live-dot"></span> LIVE DATA (6s)</div>
            <style>.live-dot {{ height:8px; width:8px; background:#00C853; border-radius:50%; display:inline-block; margin-right:6px; animation: blink 1s infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}</style>
        </div>
        <div class="grid">{grid_html}</div>
        <div class="split-layout">
            <div class="panel"><h2 class="section-title">📰 MARKET MOVERS</h2><table style="width:100%;"><tbody>{news_rows}</tbody></table></div>
            <div class="panel"><h2 class="section-title">📅 MACRO EVENTS</h2><table style="width:100%;"><thead><tr><th>EVENT</th><th>IMPACT</th><th>FCAST</th><th>PREV</th><th>DATE</th></tr></thead><tbody>{cal_rows}</tbody></table></div>
        </div>
    </div>
    {MODALS_HTML} {get_footer()} {real_time_script}
    </body></html>'''
    scrivi_file("index.html", html)

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "studies": ["RSI@tv-basicstudies", "MACD@tv-basicstudies"], "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Chart</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container"><a href="index.html" style="color:#888;">&larr; BACK</a><h1 style="color:#fff; margin-bottom:20px;">{a['name']} <span style="color:var(--accent)">PRO CHART</span></h1><div style="height:75vh; border:1px solid #333; border-radius:12px; overflow:hidden;">{widget}</div></div>
        {MODALS_HTML} {get_footer()}</body></html>'''
        scrivi_file(f"chart_{a['id']}.html", html)

def build_academy():
    sidebar = ""
    for _, mod in ACADEMY_CONTENT.items():
        sidebar += f"<div class='module-title'>{mod['title']}</div>"
        for lez in mod['lessons']:
            lock = "🔒" if lez.get("vip", False) else "📄"
            sidebar += f'''<div onclick="window.location.href='academy_{lez['id']}.html'" class="lesson-link">{lock} {lez['title']}</div>'''
            
    for _, mod in ACADEMY_CONTENT.items():
        for lez in mod['lessons']:
            content_html = lez['html']
            if lez.get("vip", False):
                content_html = f'''<div style="filter: blur(6px); pointer-events: none; user-select: none;">{lez['html']}<p>Secret strategy steps...</p></div>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--accent); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.8); z-index:10;">
                    <h2 style="color:#FFD700;">🔒 EXCLUSIVE VIP CONTENT</h2><p style="color:#ccc; margin-bottom:30px;">Unlock advanced trading strategies.</p>
                    <button class="btn-trade" style="font-size:1.2rem; padding:15px 30px;" onclick="openWaitlist()">GET VIP PASS NOW</button>
                </div>'''
            html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{lez['title']}</title>{CSS_CORE}</head><body>
            {get_header('academy')}
            <div class="container"><div class="academy-grid"><div class="sidebar">{sidebar}</div><div class="lesson-content" style="position:relative;">{content_html}</div></div></div>
            {MODALS_HTML} {get_footer()}</body></html>'''
            scrivi_file(f"academy_{lez['id']}.html", html)

def build_chat():
    js = '''<script>
    async function send() {
        let i = document.getElementById('in'); let v = i.value; if(!v) return;
        let h = document.getElementById('hist');
        h.innerHTML += `<div class="msg msg-user">${v}</div>`; i.value = ''; h.scrollTop = h.scrollHeight;
        let typeId = "t-"+Date.now(); h.innerHTML += `<div class="msg msg-ai" id="${typeId}">🤖 Analyzing...</div>`; h.scrollTop = h.scrollHeight;
        setTimeout(() => { document.getElementById(typeId).innerHTML = `🤖 Market sentiment is neutral. Wait for volume confirmation.`; h.scrollTop = h.scrollHeight; }, 1000); 
    }
    document.getElementById('in').addEventListener("keypress", e => { if(e.key === "Enter") send(); });
    </script>'''
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>AI Analyst</title>{CSS_CORE}</head><body>
    {get_header('chat')}
    <div class="container"><h2 class="section-title">AI MARKET ANALYST 🤖</h2><div class="chat-interface"><div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Welcome. Ask me about trends.</div></div><div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Type here..."><button class="chat-btn" onclick="send()">ANALYZE</button></div></div></div>
    {js} {MODALS_HTML} {get_footer()}</body></html>'''
    scrivi_file("chat.html", html)

def build_wallet():
    """Genera la pagina Portfolio Tracker che usa LocalStorage e API live"""
    js = '''<script>
    const WALLET_KEY = "mip_wallet_assets";
    
    // Lista monete supportate per questo MVP (CoinGecko IDs)
    const supportedAssets = {
        "bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "ripple": "XRP", "cardano": "ADA"
    };

    function loadWallet() {
        let saved = localStorage.getItem(WALLET_KEY);
        let assets = saved ? JSON.parse(saved) : {};
        renderWalletTable(assets);
        fetchLiveWorth(assets);
    }

    function addAsset() {
        let id = document.getElementById("asset-select").value;
        let amount = parseFloat(document.getElementById("asset-amount").value);
        if(!id || isNaN(amount) || amount <= 0) return alert("Enter a valid amount.");
        
        let saved = localStorage.getItem(WALLET_KEY);
        let assets = saved ? JSON.parse(saved) : {};
        
        assets[id] = (assets[id] || 0) + amount;
        localStorage.setItem(WALLET_KEY, JSON.stringify(assets));
        
        document.getElementById("asset-amount").value = "";
        loadWallet();
    }

    function removeAsset(id) {
        let saved = localStorage.getItem(WALLET_KEY);
        if(!saved) return;
        let assets = JSON.parse(saved);
        delete assets[id];
        localStorage.setItem(WALLET_KEY, JSON.stringify(assets));
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
            let symbol = supportedAssets[id];
            tbody.innerHTML += `<tr>
                <td><strong>${symbol}</strong></td>
                <td>${amount}</td>
                <td id="val-${id}">Loading...</td>
                <td style="text-align:right;"><button onclick="removeAsset('${id}')" style="background:#FF3D00; color:#fff; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;">X</button></td>
            </tr>`;
        }
    }

    async function fetchLiveWorth(assets) {
        let ids = Object.keys(assets).join(",");
        if(!ids) { document.getElementById("total-net-worth").innerText = "$0.00"; return; }
        
        try {
            let res = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${ids}&vs_currencies=usd`);
            let data = await res.json();
            
            let total = 0;
            for (const [id, amount] of Object.entries(assets)) {
                if(data[id]) {
                    let price = data[id].usd;
                    let value = price * amount;
                    total += value;
                    document.getElementById(`val-${id}`).innerText = "$" + value.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
                }
            }
            document.getElementById("total-net-worth").innerText = "$" + total.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2});
        } catch(e) { console.log("Error fetching wallet prices"); }
    }

    document.addEventListener("DOMContentLoaded", loadWallet);
    // Auto-update every 10 seconds
    setInterval(loadWallet, 10000);
    </script>'''

    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>My Wallet - Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('wallet')}
    <div class="container">
        <h2 class="section-title">MY PORTFOLIO TRACKER 💼</h2>
        <p style="color:#888; margin-top:-10px; margin-bottom:30px;">Track your crypto net worth in real-time. Data is securely saved only on your local device.</p>
        
        <div style="text-align:center; padding: 40px; background:#111; border-radius:12px; border:1px solid #333; margin-bottom:30px;">
            <div style="color:#888; font-size:1.2rem; text-transform:uppercase; letter-spacing:2px;">Total Net Worth</div>
            <div class="wallet-total" id="total-net-worth">$0.00</div>
            <div style="font-size:0.8rem; color:#00C853;">Live tracking active ⚡</div>
        </div>

        <div class="wallet-form">
            <select id="asset-select">
                <option value="bitcoin">Bitcoin (BTC)</option>
                <option value="ethereum">Ethereum (ETH)</option>
                <option value="solana">Solana (SOL)</option>
                <option value="ripple">Ripple (XRP)</option>
                <option value="cardano">Cardano (ADA)</option>
            </select>
            <input type="number" id="asset-amount" placeholder="Amount (e.g. 0.5)" step="0.0001">
            <button class="vip-btn" onclick="addAsset()">+ ADD ASSET</button>
        </div>

        <div class="panel">
            <table>
                <thead><tr><th>ASSET</th><th>AMOUNT</th><th>FIAT VALUE (USD)</th><th style="text-align:right;">ACTION</th></tr></thead>
                <tbody id="wallet-body">
                    </tbody>
            </table>
        </div>
    </div>
    {MODALS_HTML} {get_footer()} {js}
    </body></html>'''
    scrivi_file("wallet.html", html)