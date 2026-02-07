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

def build_index(assets: List[Dict], smart_money: List[Dict], calendar: List[Dict]):
    # Grid
    grid_html = ""
    for a in assets:
        color = "green" if a['change'] >= 0 else "red"
        sign = "+" if a['change'] >= 0 else ""
        # Usiamo triple quote single f''' per gestire le virgolette doppie dell'HTML
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
    
    # Tables
    sm_rows = ""
    for i, row in enumerate(smart_money):
        is_vip = i > 6
        blur = "blur-row" if is_vip else ""
        act_cls = "tag-buy" if "BUY" in row['azione'] or "ACC" in row['azione'] else "tag-sell"
        sm_rows += f'<tr class="{blur}"><td><strong style="color:#fff">{row["chi"]}</strong></td><td>{row["asset"]}</td><td><span class="tag {act_cls}">{row["azione"]}</span></td><td>{row["valore"]}</td><td>{row["data"]}</td></tr>'
        if i == 7: sm_rows += '<tr><td colspan="5" style="position:relative; padding:0;"><div class="unlock-overlay">🔒 UPGRADE TO VIP TO SEE FULL HISTORY</div></td></tr>'

    cal_rows = ""
    for ev in calendar:
        cal_rows += f'<tr><td><strong style="color:#fff">{ev["evento"]}</strong></td><td>{ev["impatto"]}</td><td>{ev["previsto"]}</td><td>{ev["precedente"]}</td><td>{ev["data"]}</td></tr>'

    html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Market Insider Pro</title>{CSS_CORE}</head><body>
    {get_header('home')}
    <div class="container">
        <h2 class="section-title">GLOBAL MARKETS PULSE ({len(assets)} Live Assets) ⚡</h2>
        <div class="grid">{grid_html}</div>
        <div class="split-layout">
            <div><h2 class="section-title">🕵️‍♂️ INSIDER & WHALE TRACKER</h2><div class="table-wrapper"><table><thead><tr><th>ENTITY</th><th>ASSET</th><th>ACTION</th><th>SIZE</th><th>TIME</th></tr></thead><tbody>{sm_rows}</tbody></table></div></div>
            <div><h2 class="section-title">📅 MACRO CALENDAR</h2><div class="table-wrapper"><table><thead><tr><th>EVENT</th><th>IMPACT</th><th>FCAST</th><th>PREV</th><th>DATE</th></tr></thead><tbody>{cal_rows}</tbody></table></div></div>
        </div>
    </div>
    {get_footer()}
    </body></html>'''
    scrivi_file("index.html", html)

def build_chart_pages(assets: List[Dict]):
    for a in assets:
        # Qui usiamo single quotes esterne e doppie interne per l'HTML
        widget = f'<div class="tradingview-widget-container" style="height:100%;width:100%"><div id="tv_{a["id"]}" style="height:100%;width:100%"></div><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script><script type="text/javascript">new TradingView.widget({{"autosize": true, "symbol": "{a["tv"]}", "interval": "D", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": true, "container_id": "tv_{a["id"]}"}});</script></div>'
        html = f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{a['name']} Analysis</title>{CSS_CORE}</head><body>
        {get_header('home')}
        <div class="container">
            <a href="index.html" style="color:#888;">&larr; DASHBOARD</a>
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
            # FIX CRUCIALE: Usiamo f'''...''' triplo per permettere le virgolette miste nell'HTML generato
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
                        <button class="vip-btn">MARK COMPLETE</button>
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
