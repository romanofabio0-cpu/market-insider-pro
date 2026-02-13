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
    # Dizionario per mappare ID_COINGECKO -> ID_HTML
    # Esempio: "bitcoin" -> "price-btc"
    js_mapping = {}
    
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        
        # ID HTML pulito (es: price-btc)
        elem_id = a['id'].replace(" ", "-")
        
        # Se è crypto, salviamo la mappatura per il JS
        if a['type'] == 'CRYPTO':
            # a['cg_id'] è "bitcoin", elem_id è "btc"
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
    
    # --- JAVASCRIPT REAL-TIME POTENZIATO ---
    # Creiamo la lista degli ID reali da chiedere all'API
    api_ids = ",".join(js_mapping.keys())
    # Passiamo la mappa al JS come oggetto JSON
    js_map_str = json.dumps(js_mapping)
    
    real_time_script = f'''
    <script>
    const idMap = {js_map_str}; // Mappa {{"bitcoin": "btc", "ethereum": "eth"}}
    const apiIds = "{api_ids}";  // Stringa "bitcoin,ethereum,..."
    
    async function updatePrices() {{
        console.log("⚡ Fetching live prices...");
        try {{
            // Aggiungiamo un timestamp per evitare che il browser usi la cache vecchia
            const cacheBuster = new Date().getTime();
            const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${{apiIds}}&vs_currencies=usd&include_24hr_change=true&_=${{cacheBuster}}`);
            
            if (!response.ok) throw new Error("API Limit");
            
            const data = await response.json();
            
            for (const [cgId, value] of Object.entries(data)) {{
                // Troviamo l'ID HTML corrispondente usando la mappa
                let htmlId = idMap[cgId]; 
                if (!htmlId) continue;

                let priceElem = document.getElementById(`price-${{htmlId}}`);
                let changeElem = document.getElementById(`change-${{htmlId}}`);
                
                if (priceElem) {{
                    // Puliamo il vecchio prezzo per fare il confronto
                    let oldText = priceElem.innerText.replace('$', '').replace(',', '');
                    let oldPrice = parseFloat(oldText);
                    let newPrice = value.usd;
                    
                    // Aggiorniamo SOLO se è cambiato
                    if(newPrice !== oldPrice && !isNaN(oldPrice)) {{
                        let formatted = newPrice < 1 ? "$" + newPrice.toFixed(6) : "$" + newPrice.toLocaleString('en-US', {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
                        priceElem.innerText = formatted;
                        
                        // FLASH EFFECT
                        let flashClass = newPrice > oldPrice ? 'flash-up' : 'flash-down';
                        priceElem.classList.remove('flash-up', 'flash-down');
                        void priceElem.offsetWidth; // Force reflow
                        priceElem.classList.add(flashClass);
                    }} else if (isNaN(oldPrice)) {{
                        // Se è il primo caricamento o c'era un errore
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
    
    // Avvia dopo 2 secondi
    setTimeout(updatePrices, 2000);
    // Aggiorna ogni 6 secondi (Massima velocità sicura)
    setInterval(updatePrices, 6000);
    </script>
    '''

    # --- RESTO DEL BUILDER (News, Calendar, etc.) ---
    # Costruzione News
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

    # Costruzione Calendar
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

# --- FUNZIONI ACCESSORIE INVARIATE (Ma necessarie per non rompere l'import) ---
def build_chart_pages(assets: List[Dict]):
    for a in assets:
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Analysis</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888; text-decoration:none;">&larr; BACK</a>
            <h1 style="color:#fff; margin-bottom:20px;">{a['name']} ({a['symbol']})</h1>
            <div style="height:75vh; border:1px solid #333; border-radius:12px; overflow:hidden;">{widget}</div>
        </div>
        {get_footer()}</body></html>'''
        scrivi_file(f"chart_{a['id']}.html", html)

def build_academy():
    # (Mantieni codice academy)
    pass 

def build_chat():
    # (Mantieni codice chat)
    pass