import os
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
    """Formatta il prezzo: se < 1 usa 6 decimali, altrimenti 2"""
    if price < 0.01:
        return f"${price:.6f}" 
    elif price < 1:
        return f"${price:.4f}"
    else:
        return f"${price:,.2f}"

def build_index(assets: List[Dict], news: List[Dict], calendar: List[Dict]):
    
    # --- 1. GRIGLIA ASSET ---
    grid_html = ""
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        
        # FIX NOME e PREZZO
        formatted_price = format_price(a['price'])
        
        grid_html += f'''
        <a href="chart_{a['id']}.html" class="card-link">
            <div class="card">
                <div class="card-head">
                    <span class="symbol">{a['symbol']}</span>
                    <span class="name" style="color:#888; font-size:0.8rem;">{a['name']}</span> 
                </div>
                <div class="price">{formatted_price}</div>
                <div class="change {color}">{sign}{a['change']}%</div>
                <div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{a['sig_col']}">{a['signal']}</strong></div>
            </div>
        </a>
        '''
    
    # --- 2. SEZIONE NEWS ---
    news_rows = ""
    for n in news:
        icon = "₿" if "Coin" in n['source'] else "🏛️"
        news_rows += f'''
        <tr style="border-bottom: 1px solid #333;">
            <td style="padding:10px; width:40px; text-align:center; font-size:1.2rem;">{icon}</td>
            <td style="padding:10px;">
                <a href="{n['link']}" target="_blank" style="font-weight:600; color:#eee; text-decoration:none; display:block; margin-bottom:4px; font-size:0.95rem;">
                    {n['title']}
                </a>
                <span style="font-size:0.75rem; color:#888;">{n['source']} • {n['published']}</span>
            </td>
            <td style="padding:10px; text-align:right;">
                <a href="{n['link']}" target="_blank" class="vip-btn" style="padding: 4px 12px; font-size: 0.7rem;">READ</a>
            </td>
        </tr>
        '''

    # --- 3. TABELLA MACRO ---
    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr style="border-bottom: 1px solid #333;"><td style="padding:10px;"><strong style="color:#fff">{ev["evento"]}</strong></td><td style="padding:10px;">{ev["impatto"]}</td><td style="padding:10px;">{ev["previsto"]}</td><td style="padding:10px; color:#888;">{ev["precedente"]}</td><td style="padding:10px;">{ev["data"]}</td></tr>'

    # --- ASSEMBLY HTML ---
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        
        <h2 class="section-title">GLOBAL MARKETS PULSE ({len(assets)} Live Assets) ⚡</h2>
        <div class="grid">{grid_html}</div>
        
        <div class="split-layout">
            <div class="panel">
                <h2 class="section-title">📰 BREAKING INSIDER NEWS</h2>
                <div class="table-wrapper">
                    <table style="width:100%; border-collapse: collapse;">
                        <tbody>{news_rows}</tbody>
                    </table>
                </div>
            </div>
            
            <div class="panel">
                <h2 class="section-title">📅 MACRO CALENDAR</h2>
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
    </body></html>'''
    scrivi_file("index.html", html)

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Analysis</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888; text-decoration:none;">&larr; BACK TO DASHBOARD</a>
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