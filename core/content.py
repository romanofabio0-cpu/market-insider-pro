def get_header(active_page: str) -> str:
    return f'''
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Dashboard</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="chat.html" class="{'active' if active_page=='chat' else ''}">AI Analyst</a>
            <a href="#" class="vip-btn">VIP PASS 👑</a>
        </nav>
    </header>
    '''

def get_footer() -> str:
    return '''
    <footer>
        <div class="legal-links">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Risk Disclaimer</a>
        </div>
        <p style="margin-top:20px; font-size:0.75rem; color:#555;">
            &copy; 2026 Market Insider Pro. Not financial advice.<br>
            *This site contains affiliate links. We may earn a commission at no extra cost to you.
        </p>
    </footer>
    '''

# --- CONTENUTI CORSO & AFFILIAZIONI ---
# Sostituisci la variabile ACADEMY_CONTENT nel tuo core/content.py con questa:

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: THE MINDSET 🧠",
        "lessons": [
            {
                "id": "lez1_1",
                "title": "1.1 Psychology of a Winner",
                "vip": False, # Lezione gratuita
                "html": """
                <h1>Trading Psychology</h1>
                <p>Trading is 20% strategy and 80% psychology...</p>
                <div style="margin-top:20px; padding:20px; background:#1a1a1a; border-left:4px solid #FFD700;">
                    <h3>📚 Recommended Reading</h3>
                    <a href="https://www.amazon.com/Trading-Zone-Confidence-Discipline-Attitude/dp/0735201447" target="_blank" class="vip-btn" style="background: linear-gradient(45deg, #ff9900, #ffc107); color:black;">BUY ON AMAZON 🛒</a>
                </div>
                """
            }
        ]
    },
    "mod3": {
        "title": "MODULE 3: WHALE TRACKING 🐳",
        "lessons": [
            {
                "id": "lez3_1",
                "title": "3.1 Smart Money Secret Strategy",
                "vip": True, # 🔥 LEZIONE A PAGAMENTO
                "html": """
                <h1>The Whale Order Block</h1>
                <p>Here is the exact strategy used by institutional banks...</p>
                """
            }
        ]
    }
}