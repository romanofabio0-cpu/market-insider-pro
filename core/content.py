def get_header(active_page: str) -> str:
    seo_tags = '''
    <meta name="description" content="Market Insider Pro - Advanced Algorithmic Trading Terminal. Live data, institutional signals, and AI analysis.">
    <meta property="og:title" content="Market Insider Pro - Premium Terminal">
    <meta property="og:description" content="Join the elite. Access real-time institutional order flows and AI-driven market analysis.">
    <meta property="og:image" content="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80">
    '''
    anti_theft_script = '''<script>document.addEventListener('contextmenu', e => e.preventDefault()); document.onkeydown = function(e) { if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 67 || e.keyCode == 74)) || (e.ctrlKey && e.keyCode == 85)) return false; }</script>'''

    return f'''
    {seo_tags} {anti_theft_script}
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Terminal</a>
            <a href="signals.html" class="{'active' if active_page=='signals' else ''}">⚡ Signals</a>
            <a href="leaderboard.html" class="{'active' if active_page=='leaderboard' else ''}">🏆 Leaderboard</a>
            <a href="api_hub.html" class="{'active' if active_page=='api' else ''}">🤖 API Hub</a>
            <a href="wallet.html" class="{'active' if active_page=='wallet' else ''}">Wallet</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="brokers.html" class="{'active' if active_page=='brokers' else ''}">Brokers</a>
            <a href="referral.html" class="{'active' if active_page=='referral' else ''}" style="color:var(--gold);">🎁 Invite</a>
            <a href="pricing.html" class="{'active' if active_page=='pricing' else ''}" style="color:var(--accent);">💎 Pricing</a>
            
            <span id="user-greeting" style="color:#00C853; font-weight:bold; display:none;"></span>
            <button id="login-btn" class="vip-btn" onclick="openLogin()" style="background:#333;">LOGIN</button>
            <a href="pricing.html" class="vip-btn" style="background: linear-gradient(45deg, #FFD700, #F57F17); color:#000;">VIP PASS 👑</a>
        </nav>
    </header>
    '''

def get_footer() -> str:
    return '''
    <div class="legal-footer container">
        <div class="stats-bar"><div class="stat-item"><div style="color:#00C853; font-size:0.8rem; font-weight:bold;">● LIVE TRADERS</div><div class="stat-value" id="live-users">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">Total Page Views</div><div class="stat-value" id="total-visits">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">System Status</div><div class="stat-value" style="color:#00C853;">100% SECURE</div></div></div>
        <div style="margin: 30px 0;"><a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Privacy Policy</a> | <a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Terms of Service</a> | <a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Risk Disclaimer</a></div>
        <p style="color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;"><b>STRICT LEGAL WARNING</b></p>
        <p style="text-align:justify; max-width:800px; margin: 0 auto; line-height:1.4;">© 2026 Market Insider Pro. All Rights Reserved.<br><strong>INTELLECTUAL PROPERTY:</strong> Unauthorized reproduction, scraping, or distribution is strictly prohibited.<br><strong>RISK DISCLAIMER:</strong> Trading involves significant risk. The information provided is for educational purposes only and does NOT constitute financial advice.</p>
    </div>
    <div class="fomo-popup" id="fomo-box"><div class="fomo-icon">⚡</div><div id="fomo-text">User99 just upgraded to VIP Pass.</div></div>
    <div class="cookie-banner" id="cookie-banner"><div class="cookie-text">We use cookies to secure your session and provide real-time institutional data. By continuing to use this site, you consent to our <a href="legal.html" style="color:var(--accent);">Privacy Policy</a>.</div><button class="cookie-btn" onclick="acceptCookies()">ACCEPT</button></div>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        let visits = localStorage.getItem("mip_total_visits"); if (!visits) visits = Math.floor(Math.random() * 5000) + 10000; localStorage.setItem("mip_total_visits", ++visits); let tv = document.getElementById("total-visits"); if(tv) tv.innerText = visits.toLocaleString();
        let baseUsers = Math.floor(Math.random() * 50) + 150; let lu = document.getElementById("live-users"); if(lu) lu.innerText = baseUsers;
        setInterval(() => { let f = Math.floor(Math.random() * 7) - 3; baseUsers += f; if(baseUsers < 100) baseUsers = 100; if(lu) lu.innerText = baseUsers; }, 5000);
        
        const fomoMsgs = ["🐋 Whale Alert: $4.2M moved to Binance", "🟢 User from Milan just went LONG on Bitcoin", "🔥 A user just unlocked the VIP Pass", "🚨 Algorithm detected high volatility on SOL", "💰 User from Rome secured +45% profit on NVDA"];
        setInterval(() => { let box = document.getElementById('fomo-box'); if(box) { document.getElementById('fomo-text').innerText = fomoMsgs[Math.floor(Math.random()*fomoMsgs.length)]; box.classList.add('show'); setTimeout(() => box.classList.remove('show'), 5000); } }, 15000);
        
        if(!localStorage.getItem('mip_cookies_accepted')) { setTimeout(()=> document.getElementById('cookie-banner').classList.add('show'), 2000); }
        
        if ("Notification" in window && Notification.permission !== "denied" && !localStorage.getItem('mip_push_asked')) {
            setTimeout(() => { Notification.requestPermission().then(permission => { localStorage.setItem('mip_push_asked', 'true'); if (permission === "granted") { setTimeout(()=> new Notification("Market Insider Pro", {body: "⚡ Institutional Order Block filled on BTC. Check Terminal.", icon: "https://cdn-icons-png.flaticon.com/512/2950/2950063.png"}), 15000); } }); }, 5000);
        }
    });
    function acceptCookies() { localStorage.setItem('mip_cookies_accepted', 'true'); document.getElementById('cookie-banner').classList.remove('show'); }
    </script>
    '''

MODALS_HTML = '''
<div class="stripe-overlay" id="stripe-modal"><div class="stripe-modal"><span class="close-modal" onclick="closeModals()" style="z-index:10; top:10px; right:15px; color:#333;">&times;</span><div class="stripe-header"><h3 style="margin:0; color:#333;">Market Insider Pro VIP</h3><p style="margin:5px 0 0; color:#666; font-size:0.9rem;" id="stripe-price-desc">Subscribe for $49.00/month</p></div><div class="stripe-body"><label style="font-size:0.8rem; color:#666; display:block; margin-bottom:5px;">Email</label><input type="email" class="stripe-input" placeholder="you@example.com"><label style="font-size:0.8rem; color:#666; display:block; margin-bottom:5px;">Card Information</label><input type="text" class="stripe-input" placeholder="💳 4242  4242  4242  4242" style="margin-bottom:0; border-radius: 6px 6px 0 0;"><div style="display:flex;"><input type="text" class="stripe-input" placeholder="MM / YY" style="border-radius: 0 0 0 6px; border-top:none; border-right:none; width:50%;"><input type="text" class="stripe-input" placeholder="CVC" style="border-radius: 0 0 6px 0; border-top:none; width:50%;"></div><label style="font-size:0.8rem; color:#666; display:block; margin:15px 0 5px;">Name on card</label><input type="text" class="stripe-input" placeholder="John Doe"><button class="stripe-btn" id="stripe-pay-btn" onclick="processPayment()">Subscribe</button><div class="stripe-footer">🔒 Powered by <b>Stripe</b></div></div></div></div>
<div class="modal-overlay" id="waitlist-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 id="modal-title" style="color:#FFD700; margin-top:0;">🤖 AUTO-TRADE BETA</h2><p id="modal-desc" style="color:#aaa; font-size:0.9rem;">The API Auto-Execution engine is currently in Closed Beta. Enter your email to join the waitlist.</p><div id="waitlist-form"><input type="email" id="waitlist-email" class="modal-input" placeholder="Enter your best email..."><button class="btn-trade" style="width:85%; padding:12px;" onclick="submitWaitlist()">REQUEST ACCESS</button></div><div id="waitlist-success" style="display:none; color:#00C853; font-weight:bold; margin-top:20px;">✅ Request received! Keep an eye on your inbox.</div></div></div>
<div class="modal-overlay" id="login-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 style="margin-top:0;">Secure Login</h2><p style="color:#aaa; font-size:0.9rem;">Access your encrypted local workspace.</p><input type="text" id="login-name" class="modal-input" placeholder="Display name..."><button class="vip-btn" style="width:85%; padding:12px;" onclick="doLogin()">INITIALIZE TERMINAL</button></div></div>
<script>
    function openStripe(plan, price) { document.getElementById('stripe-price-desc').innerText = `Subscribe for $${price}`; document.getElementById('stripe-modal').style.display = 'flex'; }
    function processPayment() { let btn = document.getElementById('stripe-pay-btn'); btn.innerText = "Processing..."; btn.style.opacity = "0.7"; setTimeout(() => { btn.innerText = "Payment Successful! ✅"; btn.style.background = "#00C853"; setTimeout(()=>{closeModals(); alert("Welcome to VIP! (This is a Sandbox Demo)");}, 1500); }, 2000); }
    function openWaitlist(sourceText) { document.getElementById('waitlist-modal').style.display = 'flex'; }
    function openLogin() { document.getElementById('login-modal').style.display = 'flex'; }
    function closeModals() { document.querySelectorAll('.modal-overlay, .stripe-overlay').forEach(m => m.style.display = 'none'); }
    function submitWaitlist() { let e = document.getElementById('waitlist-email').value; if(e.includes('@')) { document.getElementById('waitlist-form').style.display = 'none'; document.getElementById('waitlist-success').style.display = 'block'; } else { alert("Please enter a valid email."); } }
    function doLogin() { let n = document.getElementById('login-name').value; if(n) { localStorage.setItem('mip_user', n); closeModals(); checkLogin(); location.reload(); } }
    function checkLogin() { let u = localStorage.getItem('mip_user'); if(u) { let g = document.getElementById('user-greeting'); let b = document.getElementById('login-btn'); if(g) { g.innerText = "👤 " + u; g.style.display = "inline"; } if(b) b.style.display = "none"; } }
    document.addEventListener("DOMContentLoaded", checkLogin);
</script>
'''

# 🔥 INSERISCI QUI IL TUO VERO LINK AFFILIATO AMAZON
AMAZON_AFFILIATE_LINK = "https://www.amazon.it/dp/B00000000?tag=IL_TUO_TAG_AFFILIATO-21"

ACADEMY_CONTENT = {
    "mod1": {"title": "MODULE 1: THE MINDSET 🧠", "lessons": [{"id": "lez1_1", "title": "1.1 Psychology of a Winner", "vip": False, "html": f"<h1>Trading Psychology</h1><p>Trading is 20% strategy and 80% psychology.</p><div style='margin-top:20px; padding:20px; background:#1a1a1a; border-left:4px solid #FFD700;'><h3>📚 Recommended Book</h3><a href='{AMAZON_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background: linear-gradient(45deg, #ff9900, #ffc107); color:black;'>BUY ON AMAZON 🛒</a></div>"}]},
    "mod3": {"title": "MODULE 3: WHALE TRACKING 🐳", "lessons": [{"id": "lez3_1", "title": "3.1 Institutional Strategy", "vip": True, "html": "<h1>The Whale Order Block</h1><p>Exact strategy used by institutional banks...</p>"}]}
}