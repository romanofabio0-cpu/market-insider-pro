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
            <a href="api_hub.html" class="{'active' if active_page=='api' else ''}">🤖 Auto-Trade</a>
            <a href="wallet.html" class="{'active' if active_page=='wallet' else ''}">Wallet</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="brokers.html" class="{'active' if active_page=='brokers' else ''}">Brokers</a>
            <a href="referral.html" class="{'active' if active_page=='referral' else ''}" style="color:var(--gold);">🎁 Invite & Earn</a>
            <span id="user-greeting" style="color:#00C853; font-weight:bold; display:none;"></span>
            <button id="login-btn" class="vip-btn" onclick="openLogin()" style="background:#333;">LOGIN</button>
            <button class="vip-btn" onclick="openWaitlist('VIP PASS')" style="background: linear-gradient(45deg, #FFD700, #F57F17); color:#000;">VIP PASS 👑</button>
        </nav>
    </header>
    '''

def get_footer() -> str:
    # FOMO FEED ENGINE INIETTATO QUI
    return '''
    <div class="legal-footer container">
        <div class="stats-bar"><div class="stat-item"><div style="color:#00C853; font-size:0.8rem; font-weight:bold;">● LIVE TRADERS</div><div class="stat-value" id="live-users">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">Total Page Views</div><div class="stat-value" id="total-visits">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">System Status</div><div class="stat-value" style="color:#00C853;">100% SECURE</div></div></div>
        <p style="color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;"><b>STRICT LEGAL WARNING & DISCLAIMER</b></p>
        <p style="text-align:justify; max-width:800px; margin: 0 auto; line-height:1.4;">© 2026 Market Insider Pro. All Rights Reserved.<br><strong>INTELLECTUAL PROPERTY:</strong> Unauthorized reproduction, scraping, or distribution is strictly prohibited.<br><strong>RISK DISCLAIMER:</strong> Trading involves significant risk. The information provided is for educational purposes only and does NOT constitute financial advice.</p>
    </div>
    
    <div class="fomo-popup" id="fomo-box">
        <div class="fomo-icon">⚡</div>
        <div id="fomo-text">User99 just upgraded to VIP Pass.</div>
    </div>
    
    <script>
    // VISITOR COUNTER
    document.addEventListener("DOMContentLoaded", function() {
        let visits = localStorage.getItem("mip_total_visits");
        if (!visits) visits = Math.floor(Math.random() * 5000) + 10000; 
        localStorage.setItem("mip_total_visits", ++visits);
        document.getElementById("total-visits").innerText = visits.toLocaleString();
        let baseUsers = Math.floor(Math.random() * 50) + 150;
        document.getElementById("live-users").innerText = baseUsers;
        setInterval(() => { let f = Math.floor(Math.random() * 7) - 3; baseUsers += f; if(baseUsers < 100) baseUsers = 100; document.getElementById("live-users").innerText = baseUsers; }, 5000);
        
        // FOMO ENGINE
        const fomoMsgs = [
            "🐋 Whale Alert: $4.2M moved to Binance", 
            "🟢 User from Milan just went LONG on Bitcoin", 
            "🔥 A user just unlocked the VIP Pass", 
            "🚨 Algorithm detected high volatility on SOL", 
            "💰 User from Rome secured +45% profit on NVDA",
            "⚡ Institutional order block filled on ETH"
        ];
        setInterval(() => {
            let box = document.getElementById('fomo-box');
            document.getElementById('fomo-text').innerText = fomoMsgs[Math.floor(Math.random()*fomoMsgs.length)];
            box.classList.add('show');
            setTimeout(() => box.classList.remove('show'), 5000);
        }, 15000); // Mostra un pop-up ogni 15 secondi
    });
    </script>
    '''

MODALS_HTML = '''
<div class="modal-overlay" id="waitlist-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 id="modal-title" style="color:#FFD700; margin-top:0;">👑 VIP WAITLIST</h2><p id="modal-desc" style="color:#aaa; font-size:0.9rem;">Join the waitlist to get early access to institutional signals.</p><div id="waitlist-form"><input type="email" id="waitlist-email" class="modal-input" placeholder="Enter your best email..."><button class="btn-trade" style="width:85%; padding:12px;" onclick="submitWaitlist()">REQUEST ACCESS</button></div><div id="waitlist-success" style="display:none; color:#00C853; font-weight:bold; margin-top:20px;">✅ Request received! Keep an eye on your inbox.</div></div></div>
<div class="modal-overlay" id="login-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 style="margin-top:0;">Secure Login</h2><p style="color:#aaa; font-size:0.9rem;">Access your encrypted local workspace.</p><input type="text" id="login-name" class="modal-input" placeholder="Display name..."><button class="vip-btn" style="width:85%; padding:12px;" onclick="doLogin()">INITIALIZE TERMINAL</button></div></div>
<script>
    function openWaitlist(sourceText) { 
        if(sourceText === 'API') { document.getElementById('modal-title').innerText = '🤖 AUTO-TRADE BETA'; document.getElementById('modal-desc').innerText = 'The API Auto-Execution engine is currently in Closed Beta for VIP members. Enter your email to join the waitlist.'; } 
        else { document.getElementById('modal-title').innerText = '👑 VIP PASS WAITLIST'; document.getElementById('modal-desc').innerText = 'Join the waitlist to get early access to institutional signals and advanced courses.'; }
        document.getElementById('waitlist-modal').style.display = 'flex'; 
    }
    function openLogin() { document.getElementById('login-modal').style.display = 'flex'; }
    function closeModals() { document.querySelectorAll('.modal-overlay').forEach(m => m.style.display = 'none'); }
    function submitWaitlist() { let e = document.getElementById('waitlist-email').value; if(e.includes('@')) { document.getElementById('waitlist-form').style.display = 'none'; document.getElementById('waitlist-success').style.display = 'block'; } else { alert("Please enter a valid email."); } }
    function doLogin() { let n = document.getElementById('login-name').value; if(n) { localStorage.setItem('mip_user', n); closeModals(); checkLogin(); location.reload(); } }
    function checkLogin() { let u = localStorage.getItem('mip_user'); if(u) { let g = document.getElementById('user-greeting'); let b = document.getElementById('login-btn'); if(g) { g.innerText = "👤 " + u; g.style.display = "inline"; } if(b) b.style.display = "none"; } }
    document.addEventListener("DOMContentLoaded", checkLogin);
</script>
'''

ACADEMY_CONTENT = {
    "mod1": {"title": "MODULE 1: THE MINDSET 🧠", "lessons": [{"id": "lez1_1", "title": "1.1 Psychology of a Winner", "vip": False, "html": "<h1>Trading Psychology</h1><p>Trading is 20% strategy and 80% psychology.</p>"}]},
    "mod3": {"title": "MODULE 3: WHALE TRACKING 🐳", "lessons": [{"id": "lez3_1", "title": "3.1 Institutional Strategy", "vip": True, "html": "<h1>The Whale Order Block</h1><p>Exact strategy used by institutional banks...</p>"}]}
}