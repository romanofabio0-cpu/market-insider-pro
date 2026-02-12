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

# 🔥 MODIFICA QUI: Aggiunto parametro 'news'
def build_index(assets: List[Dict], news: List[Dict], calendar: List[Dict]):
    
    # --- 1. GRIGLIA ASSET (Come prima) ---
    grid_html = ""
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        grid_html += f'''
        <a href="chart_{a['id']}.html" class="card-link">
            <div class="card">
                <div class="card-head"><span class="symbol">{a['symbol']}</span><span class="name">{a['type']}</span></div>
                <div class="price">${a['price']:,}</div>
                <div class="change {color}">{sign}{a['change']}%</div>
                <div class="signal-box"><span>AI SIGNAL:</span><strong style="color:{a['sig_col']}">{a['signal']}</strong></div>
            </div>
        </a>
        '''
    
    # --- 🔥🔥 NUOVO: GENERAZIONE RIGHE NEWS ---
    news_rows = ""
    for n in news:
        # Icona diversa se è crypto o finanza classica
        icon = "₿" if "Coin" in n['source'] else "🏛️"
        
        # Creiamo la riga della tabella
        news_rows += f'''
        <tr>
            <td style="width:50px; text-align:center; font-size:1.2rem;">{icon}</td>
            <td>
                <a href="{n['link']}" target="_blank" style="font-weight:bold; color:#fff; display:block; margin-bottom:4px; text-decoration:none;">
                    {n['title']}
                </a>
                <span style="font-size:0.75rem; color:#888;">{n['source']} • {n['published']}</span>
            </td>
            <td style="text-align:right;">
                <a href="{n['link']}" target="_blank" class="vip-btn" style="padding: 5px 10px; font-size: 0.7rem;">READ ↗</a>
            </td>
        </tr>
        '''

    # --- 3. TABELLA MACRO (Come prima) ---
    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr><td><strong style="color:#fff">{ev["evento"]}</strong></td><td>{ev["impatto"]}</td><td>{ev["previsto"]}</td><td>{ev["precedente"]}</td><td>{ev["data"]}</td></tr>'

    # --- ASSEMBLY FINALE HTML ---
    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        
        <h2 class="section-title">GLOBAL MARKETS PULSE ({len(assets)} Live Assets) ⚡</h2>
        <div class="grid">{grid_html}</div>
        
        <div class="split-layout" style="display:grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 40px;">
            
            <div>
                <h2 class="section-title">📰 BREAKING INSIDER NEWS</h2>
                <div class="table-wrapper">
                    <table style="width:100%; border-collapse: collapse;">
                        <tbody>{news_rows}</tbody>
                    </table>
                </div>
            </div>
            
            <div>
                <h2 class="section-title">📅 MACRO CALENDAR</h2>
                <div class="table-wrapper">
                    <table style="width:100%; border-collapse: collapse;">
                        <thead>
                            <tr style="text-align:left; color:#888;">
                                <th>EVENT</th><th>IMPACT</th><th>FCAST</th><th>PREV</th><th>DATE</th>
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

# --- LE ALTRE FUNZIONI (Chart, Academy, Chat) RIMANGONO UGUALI ---
# Le rimetto qui per comodità, così copiando tutto il file non perdi pezzi.

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        # TradingView Widget
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
    # Genera Sidebar
    for _, mod in ACADEMY_CONTENT.items():
        sidebar += f"<div class='module-title'>{mod['title']}</div>"
        for lez in mod['lessons']:
            sidebar += f'''<div onclick="window.location.href='academy_{lez['id']}.html'" class="lesson-link">📄 {lez['title']}</div>'''
    
    # Genera Pagine Lezioni
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
            <div class="chat-history" id="hist"><div class="msg msg-ai">🤖 Hello! I am your Market Analyst. Ask me about trends.</div></div>
            <div class="chat-input-area"><input type="text" class="chat-input" id="in" placeholder="Ask analysis (e.g., 'Is BTC bullish?')..."><button class="chat-btn" onclick="send()">ANALYZE</button></div>
        </div>
    </div>
    {js} {get_footer()}
    </body></html>'''
    scrivi_file("chat.html", html)