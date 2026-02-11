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
ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: THE MINDSET 🧠",
        "lessons": [
            {
                "id": "lez1_1",
                "title": "1.1 Psychology of a Winner",
                "html": """
                <h1>Trading Psychology: The 80/20 Rule</h1>
                <p>Most beginners think trading is about charts. <strong>It is not.</strong></p>
                <p>Trading is 20% strategy and 80% psychology. If you cannot control your emotions (Fear & Greed), you will lose money even with the best strategy in the world.</p>
                <h3>The 3 Rules of Discipline:</h3>
                <ul>
                    <li><strong>Never revenge trade:</strong> If you lose, walk away.</li>
                    <li><strong>Stick to the plan:</strong> Determine your entry and exit BEFORE you click buy.</li>
                    <li><strong>Risk Management:</strong> Never risk more than 1-2% of your account on a single trade.</li>
                </ul>
                <div style="margin-top:40px; padding:20px; background:#1a1a1a; border-left:4px solid #FFD700; border-radius:4px;">
                    <h3>📚 Recommended Reading</h3>
                    <p>The bible of trading psychology is "Trading in the Zone" by Mark Douglas.</p>
                    <br>
                    <a href="https://www.amazon.com/Trading-Zone-Confidence-Discipline-Attitude/dp/0735201447" target="_blank" class="vip-btn" style="background: linear-gradient(45deg, #ff9900, #ffc107); color:black;">BUY ON AMAZON 🛒</a>
                </div>
                """
            },
            {
                "id": "lez1_2",
                "title": "1.2 Risk Management",
                "html": """
                <h1>Don't Lose Money</h1>
                <p>Your #1 job as a trader is not to make money, but to <strong>protect your capital</strong>.</p>
                <h3>The 1% Rule</h3>
                <p>If you have a $1,000 account, you should never lose more than $10 on a single trade. This ensures you can survive a losing streak.</p>
                """
            }
        ]
    },
    "mod2": {
        "title": "MODULE 2: TECHNICAL MASTERY 📈",
        "lessons": [
            {
                "id": "lez2_1",
                "title": "2.1 Japanese Candlesticks",
                "html": """
                <h1>Reading the Language of Price</h1>
                <p>Candlesticks tell you who is winning the war: Buyers (Bulls) or Sellers (Bears).</p>
                <ul>
                    <li><strong>Green Candle:</strong> Price closed higher than it opened (Bullish).</li>
                    <li><strong>Red Candle:</strong> Price closed lower than it opened (Bearish).</li>
                    <li><strong>Wick (Shadow):</strong> Shows rejection. A long wick on top means sellers pushed price down.</li>
                </ul>
                """
            },
            {
                "id": "lez2_2",
                "title": "2.2 Market Structure (HH/HL)",
                "html": """
                <h1>Trend is Your Friend</h1>
                <p>Identify the trend by looking at Highs and Lows.</p>
                <ul>
                    <li><strong>Uptrend:</strong> Higher Highs (HH) and Higher Lows (HL).</li>
                    <li><strong>Downtrend:</strong> Lower Highs (LH) and Lower Lows (LL).</li>
                </ul>
                <div style="margin-top:40px; padding:20px; background:#1a1a1a; border-left:4px solid #2962FF; border-radius:4px;">
                    <h3>🖥️ Best Hardware for Charting</h3>
                    <p>Don't trade on a phone. You need a clear view.</p>
                    <br>
                    <a href="https://www.amazon.com/s?k=ultrawide+monitor" target="_blank" class="vip-btn">VIEW MONITORS 🛒</a>
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
                "title": "3.1 Smart Money Concepts",
                "html": """
                <h1>Follow the Big Money</h1>
                <p>Institutional money (Banks, Hedge Funds) leaves footprints. They cannot hide their volume.</p>
                <p>In this module, we learn how to spot 'Order Blocks' and 'Fair Value Gaps' to trade alongside the whales, not against them.</p>
                <p><em>(Full video strategy coming soon for VIP members...)</em></p>
                """
            }
        ]
    }
}