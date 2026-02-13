import os
import json
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
        </a>
        '''
    
    # --- JAVASCRIPT REAL-TIME ENGINE ---
    api_ids = ",".join(js_mapping.keys())
    js_map_str = json.dumps(js_mapping)
    
    real_time_script = f'''
    <script>
    const idMap = {js_map_str}; 
    const apiIds = "{api_ids}";  
    
    async function updatePrices() {{
        try {{
            const cacheBuster = new Date().getTime();
            const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${{apiIds}}&vs_currencies=usd&include_24hr_change=true&_=${{cacheBuster}}`);
            if (!response.ok) throw new Error("API Limit");
            
            const data = await response.json();
            
            for (const [cgId, value] of Object.entries(data)) {{
                let htmlId = idMap[cgId]; 
                if (!htmlId) continue;

                let priceElem = document.getElementById(`price-${{htmlId}}`);
                let changeElem = document.getElementById(`change-${{htmlId}}`);
                
                if (priceElem) {{
                    let oldText = priceElem.innerText.replace('$', '').replace(',', '');
                    let oldPrice = parseFloat(oldText);
                    let newPrice = value.usd;
                    
                    if(newPrice !== oldPrice && !isNaN(oldPrice)) {{
                        let formatted = newPrice < 1 ? "$" + newPrice.toFixed(6) : "$" + newPrice.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
                        priceElem.innerText = formatted;
                        
                        let flashClass = newPrice > oldPrice ? 'flash-up' : 'flash-down';
                        priceElem.classList.remove('flash-up', 'flash-down');
                        void priceElem.offsetWidth; 
                        priceElem.classList.add(flashClass);
                    }} else if (isNaN(oldPrice)) {{
                        let formatted = newPrice < 1 ? "$" + newPrice.toFixed(6) : "$" + newPrice.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
                        priceElem.innerText = formatted;
                    }}
                }}
                
                if (changeElem) {{
                    let change = value.usd_24h_change.toFixed(2);
                    let sign = change >= 0 ? "+" : "";
                    changeElem.innerText = sign + change + "%";
                    changeElem.className = "change " + (change >= 0 ? "green" : "red");
                }}
            }}
        }} catch (e) {{
            console.log("Live Update Paused (Rate Limit):", e);
        }}
    }}
    setTimeout(updatePrices, 2000);
    setInterval(updatePrices, 6000);
    </script>
    '''

    news_rows = ""
    for n in news:
        icon = "🔥" if "Coin" in n['source'] else "🏛️"
        cta_text = "⚡ TRADE NOW" if "Coin" in n['source'] else "👁️ INSIDER VIEW"
        news_rows += f'''
        <tr style="border-bottom: 1px solid #333;">
            <td style="padding:15px 10px; width:40px; text-align:center; font-size:1.2rem;">{icon}</td>
            <td style="padding:15px 10px;">
                <a href="{n['link']}" target="_blank" style="font-weight:700; color:#fff; text-decoration:none; display:block; margin-bottom:5px; font-size:1rem; line-height:1.4;">{n['title']}</a>
                <span style="font-size:0.75rem; color:#888; text-transform:uppercase;">{n['source']} • {n['published']}</span>
            </td>
            <td style="padding:15px 10px; text-align:right;"><a href="{n['link']}" target="_blank" class="btn-trade">{cta_text}</a></td>
        </tr>'''

    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:10px;"><strong style="color:#fff">{ev["evento"]}</strong></td><td style="padding:10px;">{ev["impatto"]}</td><td style="padding:10px;">{ev["previsto"]}</td><td style="padding:10px; color:#888;">{ev["precedente"]}</td><td style="padding:10px;">{ev["data"]}</td></tr>'

    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 class="section-title" style="margin:0;">GLOBAL MARKETS PULSE ⚡</h2>
            <div style="font-size:0.8rem; color:#00C853; display:flex; align-items:center;">
                <span class="live-dot"></span> LIVE DATA (6s)
            </div>
            <style>.live-dot {{ height:8px; width:8px; background:#00C853; border-radius:50%; display:inline-block; margin-right:6px; animation: blink 1s infinite; }} @keyframes blink {{ 50% {{ opacity: 0; }} }}</style>
        </div>
        <div class="grid">{grid_html}</div>
        <div class="split-layout">
            <div class="panel"><h2 class="section-title">📰 MARKET MOVERS</h2><div class="table-wrapper"><table style="width:100%; border-collapse: collapse;"><tbody>{news_rows}</tbody></table></div></div>
            <div class="panel"><h2 class="section-title">📅 MACRO EVENTS</h2><div class="table-wrapper"><table style="width:100%; border-collapse: collapse;"><thead><tr style="text-align:left; color:#888; border-bottom:1px solid #444;"><th>EVENT</th><th>IMPACT</th><th>FCAST</th><th>PREV</th><th>DATE</th></tr></thead><tbody>{cal_rows}</tbody></table></div></div>
        </div>
    </div>
    {get_footer()}
    {real_time_script}
    </body></html>'''
    scrivi_file("index.html", html)

# =====================================================================
# 🔥 NUOVE FUNZIONI DELLA FASE 2: GRAFICI PRO, ACADEMY VIP E AI CHATBOT
# =====================================================================

def build_chart_pages(assets: List[Dict]):
    """Genera grafici TradingView con indicatori avanzati attivati di default"""
    for a in assets:
        # Aggiunti indicatori tecnici (studies): RSI, MACD e Medie Mobili
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "studies": ["RSI@tv-basicstudies", "MACD@tv-basicstudies", "MASimple@tv-basicstudies"], "container_id": "tv_{a["id"]}"}});</script></div>'
        
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Pro Chart</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888; text-decoration:none;">&larr; BACK TO TERMINAL</a>
            <h1 style="color:#fff; margin-bottom:20px;">{a['name']} <span style="color:var(--accent)">ADVANCED ALGORITHMIC CHART</span></h1>
            <div style="height:75vh; border:1px solid #333; border-radius:12px; overflow:hidden;">{widget}</div>
        </div>
        {get_footer()}</body></html>'''
        scrivi_file(f"chart_{a['id']}.html", html)

def build_academy():
    """Genera il modulo Academy con il Paywall per i contenuti VIP"""
    sidebar = ""
    for _, mod in ACADEMY_CONTENT.items():
        sidebar += f"<div class='module-title'>{mod['title']}</div>"
        for lez in mod['lessons']:
            # Aggiunge lucchetto alla sidebar se VIP
            lock = "🔒" if lez.get("vip", False) else "📄"
            sidebar += f'''<div onclick="window.location.href='academy_{lez['id']}.html'" class="lesson-link">{lock} {lez['title']}</div>'''
            
    for _, mod in ACADEMY_CONTENT.items():
        for lez in mod['lessons']:
            # Logica Paywall
            content_html = lez['html']
            if lez.get("vip", False):
                content_html = f'''
                <div style="filter: blur(6px); pointer-events: none; user-select: none;">
                    {lez['html']}
                    <p>Secret strategy steps...</p><p>Indicator settings...</p>
                </div>
                <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); text-align:center; background:#111; padding:40px; border:2px solid var(--accent); border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.8); z-index:10;">
                    <h2 style="color:#FFD700; font-size:1.8rem;">🔒 EXCLUSIVE VIP CONTENT</h2>
                    <p style="color:#ccc; margin-bottom:30px;">Unlock advanced trading strategies, live signals, and institutional indicators.</p>
                    <a href="#" class="btn-trade" style="font-size:1.2rem; padding:15px 30px;">GET VIP PASS NOW</a>
                </div>
                '''

            html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{lez['title']}</title>{CSS_CORE}</head><body>
            {get_header('academy')}
            <div class="container">
                <div class="academy-grid">
                    <div class="sidebar">{sidebar}</div>
                    <div class="lesson-content" style="position:relative;">
                        {content_html}
                        {"" if lez.get("vip", False) else '<hr style="border:0; border-top:1px solid #333; margin:50px 0;"><button class="vip-btn">MARK AS COMPLETED ✅</button>'}
                    </div>
                </div>
            </div>
            {get_footer()}</body></html>'''
            scrivi_file(f"academy_{lez['id']}.html", html)

def build_chat():
    """Genera l'IA locale che analizza il mercato algoritmicamente senza API a pagamento"""
    js = '''<script>
    async function getSmartResponse(query) {
        let q = query.toLowerCase();
        if(q.includes("btc") || q.includes("bitcoin")) {
            try {
                let res = await fetch("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true");
                let data = await res.json();
                let change = data.bitcoin.usd_24h_change;
                let trend = change > 0 ? "BULLISH 🟢" : "BEARISH 🔴";
                return `My analysis on Bitcoin: The current price is $${data.bitcoin.usd}. The 24h trend is ${trend} (${change.toFixed(2)}%). Institutional volume is currently supporting this momentum.`;
            } catch(e) { return "Bitcoin is currently facing high volatility. Wait for a clear support level."; }
        }
        else if(q.includes("buy") || q.includes("invest")) {
            return "Based on my algorithm, I recommend looking at assets with a strong 'BUY' signal on the dashboard. Ensure your risk management is strict (1% rule).";
        }
        else if(q.includes("gold") || q.includes("oil")) {
            return "Macro assets like Gold and Oil act as a hedge. Check the 'MACRO' section on the terminal for live RSI signals.";
        }
        else {
            let responses = ["Analyzing volume profile... Bullish divergence detected.", "Market sentiment is currently FEAR.", "Wait for a retest of the Moving Average before entering.", "Keep an eye on the upcoming Macro Economic events calendar."];
            return responses[Math.floor(Math.random()*responses.length)];
        }
    }

    async function send() {
        let i = document.getElementById('in'); let v = i.value; if(!v) return;
        let h = document.getElementById('hist');
        h.innerHTML += `<div class="msg msg-user">${v}</div>`; i.value = ''; h.scrollTop = h.scrollHeight;
        
        let typingId = "type-" + Date.now();
        h.innerHTML += `<div class="msg msg-ai" id="${typingId}">🤖 Analyzing market data...</div>`; h.scrollTop = h.scrollHeight;
        
        let responseText = await getSmartResponse(v);
        
        setTimeout(() => {
            document.getElementById(typingId).innerHTML = `🤖 ${responseText}`;
            h.scrollTop = h.scrollHeight;
        }, 1000); 
    }
    document.getElementById('in').addEventListener("keypress", e => { if(e.key === "Enter") send(); });
    </script>'''
    
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>AI Analyst</title>{CSS_CORE}</head><body>
    {get_header('chat')}
    <div class="container">
        <h2 class="section-title">AI MARKET ANALYST (Local Engine V2) 🤖</h2>
        <div class="chat-interface">
            <div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Welcome. I am connected to the real-time data engine. Ask me about Bitcoin, macro trends, or investment strategies.</div></div>
            <div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Ask 'What is the trend for Bitcoin?'..."><button class="chat-btn" onclick="send()">ANALYZE</button></div>
        </div>
    </div>
    {js} {get_footer()}
    </body></html>'''
    scrivi_file("chat.html", html)