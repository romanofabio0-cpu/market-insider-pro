
def get_header(active_page: str) -> str:
    return f'''
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Dashboard</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="chat.html" class="{'active' if active_page=='chat' else ''}">AI Analyst</a>
            <a href="#" class="vip-btn">GET VIP PASS 👑</a>
        </nav>
    </header>
    '''

def get_footer() -> str:
    return '''
    <footer>
        <div class="legal-links"><a href="#">Privacy Policy</a><a href="#">Terms of Service</a><a href="#">Risk Disclaimer</a></div>
        <p style="margin-top:20px;">&copy; 2026 Market Insider Pro. All trading involves risk. Past performance is not indicative of future results.</p>
    </footer>
    '''

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: FOUNDATIONS",
        "lessons": [
            {"id": "lez1_1", "title": "1.1 The Trading Mindset", "html": "<h1>The Trading Mindset</h1><p>Success in trading is 20% strategy and 80% psychology.</p>"},
            {"id": "lez1_2", "title": "1.2 Understanding Candles", "html": "<h1>Japanese Candlesticks</h1><p>Candlesticks tell the story of the battle between buyers and sellers.</p>"}
        ]
    },
    "mod2": {
        "title": "MODULE 2: TECHNICAL ANALYSIS",
        "lessons": [
            {"id": "lez2_1", "title": "2.1 Support & Resistance", "html": "<h1>Support & Resistance</h1><p>Invisible floors and ceilings of the market.</p>"},
            {"id": "lez2_2", "title": "2.2 RSI & MACD", "html": "<h1>Indicators</h1><p>RSI measures momentum.</p>"}
        ]
    },
    "mod3": {
        "title": "MODULE 3: PRO STRATEGIES",
        "lessons": [
            {"id": "lez3_1", "title": "3.1 Smart Money Concepts", "html": "<h1>Follow the Whales</h1><p>Institutional money leaves footprints.</p>"}
        ]
    }
}
