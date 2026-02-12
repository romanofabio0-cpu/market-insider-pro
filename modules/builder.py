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
    
    # --- 1. COSTRUIAMO LA GRIGLIA CON ID PER JAVASCRIPT ---
    grid_html = ""
    asset_ids_js = [] # Lista per dire al JS cosa monitorare
    
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        
        # ID univoci per l'aggiornamento real-time (es: price-bitcoin, change-bitcoin)
        # Nota: Funzionerà live solo per le crypto supportate dall'API pubblica
        elem_id = a['id'].replace(" ", "-")
        if a['type'] == 'CRYPTO':
            asset_ids_js.append(a['id']) 
        
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
    
    # --- 2. JAVASCRIPT REAL-TIME ENGINE ---
    # Convertiamo la lista di ID python in una stringa JS
    js_ids_string = ",".join(asset_ids_js)
    
    real_time_script = f'''
    <script>
    async function updatePrices() {{
        // Aggiorna solo Crypto per ora (API Gratuita Pubblica)
        const ids = "{js_ids_string}";
        try {{
            const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${{ids}}&vs_currencies=usd&include_24hr_change=true`);
            const data = await response.json();
            
            for (const [key, value] of Object.entries(data)) {{
                // Aggiorna Prezzo
                let priceElem = document.getElementById(`price-${{key}}`);
                let oldPrice = parseFloat(priceElem.innerText.replace('$', '').replace(',', ''));
                let newPrice = value.usd;
                
                if (priceElem) {{
                    // Formattazione
                    let formatted = newPrice < 1 ? "$" + newPrice.toFixed(4) : "$" + newPrice.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
                    priceElem.innerText = formatted;
                    
                    // Effetto Flash
                    if(newPrice > oldPrice) {{ priceElem.classList.add('flash-up'); setTimeout(()=>priceElem.classList.remove('flash-up'), 1000); }}
                    else if(newPrice < oldPrice) {{ priceElem.classList.add('flash-down'); setTimeout(()=>priceElem.classList.remove('flash-down'), 1000); }}
                }}
                
                // Aggiorna Percentuale
                let changeElem = document.getElementById(`change-${{key}}`);
                if (changeElem) {{
                    let change = value.usd_24h_change.toFixed(2);
                    let sign = change >= 0 ? "+" : "";
                    changeElem.innerText = sign + change + "%";
                    
                    // Colori
                    changeElem.className = "change"; // Reset
                    changeElem.classList.add(change >= 0 ? "green" : "red");
                }}
            }}
            console.log("⚡ Prices updated live!");
        }} catch (e) {{
            console.log("Skipping update (Rate limit or error):", e);
        }}
    }}
    
    // Avvia aggiornamento ogni 20 secondi
    setInterval(updatePrices, 20000);
    </script>
    '''

    # --- 3. NEWS CON NUOVE CTA AGGRESSIVE ---
    news_rows = ""
    for n in news:
        icon = "🔥" if "Coin" in n['source'] else "🏛️"
        # CTA Randomizzata per varietà
        cta_text = "⚡ TRADE NOW" if "Coin" in n['source'] else "👁️ INSIDER VIEW"
        
        news_rows += f'''
        <tr style="border-bottom: 1px solid #333;">
            <td style="padding:15px 10px; width:40px; text-align:center; font-size:1.2rem;">{icon}</td>
            <td style="padding:15px 10px;">
                <a href="{n['link']}" target="_blank" style="font-weight:700; color:#fff; text-decoration:none; display:block; margin-bottom:5px; font-size:1rem; line-height:1.4;">
                    {n['title']}
                </a>
                <span style="font-size:0.75rem; color:#888; text-transform:uppercase; letter-spacing:1px;">{n['source']} • {n['published']}</span>
            </td>
            <td style="padding:15px 10px; text-align:right; vertical-align:middle;">
                <a href="{n['link']}" target="_blank" class="btn-trade">{cta_text}</a>
            </td>
        </tr>
        '''

    # --- 4. CALENDARIO ---
    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:10px;"><strong style="color:#fff">{ev["evento"]}</strong></td><td style="padding:10px;">{ev["impatto"]}</td><td style="padding:10px;">{ev["previsto"]}</td><td style="padding:10px; color:#888;">{ev["precedente"]}</td><td style="padding:10px;">{ev["data"]}</td></tr>'

    # --- ASSEMBLY HTML ---
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
            <h2 class="section-title" style="margin:0;">GLOBAL MARKETS PULSE ⚡</h2>
            <div style="font-size:0.8rem; color:#00C853;">● LIVE DATA ACTIVE</div>
        </div>
        
        <div class="grid">{grid_html}</div>
        
        <div class="split-layout">
            <div class="panel">
                <h2 class="section-title">📰 MARKET MOVERS INTELLIGENCE</h2>
                <div class="table-wrapper">
                    <table style="width:100%; border-collapse: collapse;"><tbody>{news_rows}</tbody></table>
                </div>
            </div>
            
            <div class="panel">
                <h2 class="section-title">📅 MACRO ECONOMIC EVENTS</h2>
                <div class="table-wrapper">
                    <table style="width:100%; border-collapse: collapse;">
                        <thead>
                            <tr style="text-align:left; color:#888; border-bottom:1px solid #444;">
                                <th style="padding:10px;">EVENT</th><th style="padding:10px;">IMPACT</th><th style="padding:10px;">FCAST</th><th style="padding:10px;">PREV</th><th style="padding:10px;">DATE</th>
                            </tr>
                        </thead>
                        <tbody>{cal_rows}</tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    {get_footer()}
    {real_time_script} </body></html>'''
    scrivi_file("index.html", html)

# --- FUNZIONI INVARIATE (Chart, Academy, Chat) ---
# Copia qui le funzioni build_chart_pages, build_academy, build_chat 
# dal file precedente o lasciale se non hai cancellato tutto.
# IMPORTANTE: Se copi-incolli, assicurati che build_chart_pages, ecc. siano presenti sotto!
def build_chart_pages(assets: List[Dict]):
    for a in assets:
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Analysis</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888; text-decoration:none;">&larr; DASHBOARD</a>
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
                        <button class="vip-btn">MARK AS COMPLETED ✅</button>
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