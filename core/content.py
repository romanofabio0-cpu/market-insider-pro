def get_header(active_page: str) -> str:
    # Aggiunti Meta Tag SEO & Social Graph per Viralità
    seo_tags = '''
    <meta name="description" content="Market Insider Pro - Advanced Algorithmic Trading Terminal. Live data, institutional signals, and AI analysis.">
    <meta name="keywords" content="trading, crypto, stocks, signals, AI analyst, algorithmic trading">
    <meta property="og:title" content="Market Insider Pro - Premium Terminal">
    <meta property="og:description" content="Join the elite. Access real-time institutional order flows and AI-driven market analysis.">
    <meta property="og:image" content="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80">
    <meta property="og:type" content="website">
    '''
    
    # SCRIPT ANTI-FURTO (Blocca Tasto Destro, F12, Ctrl+Shift+I)
    anti_theft_script = '''
    <script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.onkeydown = function(e) {
        if(e.keyCode == 123) return false; // F12
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) return false; 
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) return false; 
        if(e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) return false; 
        if(e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) return false; 
    }
    </script>
    '''

    return f'''
    {seo_tags}
    {anti_theft_script}
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Terminal</a>
            <a href="signals.html" class="{'active' if active_page=='signals' else ''}">⚡ Signals</a>
            <a href="api_hub.html" class="{'active' if active_page=='api' else ''}">🤖 Auto-Trade</a>
            <a href="wallet.html" class="{'active' if active_page=='wallet' else ''}">Wallet</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="brokers.html" class="{'active' if active_page=='brokers' else ''}">Brokers</a>
            <span id="user-greeting" style="color:#00C853; font-weight:bold; display:none;"></span>
            <button id="login-btn" class="vip-btn" onclick="openLogin()" style="background:#333;">LOGIN</button>
            <button class="vip-btn" onclick="openWaitlist('VIP PASS')" style="background: linear-gradient(45deg, #FFD700, #F57F17); color:#000;">VIP PASS 👑</button>
        </nav>
    </header>
    '''

def get_footer() -> str:
    # Footer Legale e Contatore Visite
    return '''
    <div class="legal-footer container">
        <div class="stats-bar">
            <div class="stat-item">
                <div style="color:#00C853; font-size:0.8rem; font-weight:bold;">● LIVE TRADERS</div>
                <div class="stat-value" id="live-users">---</div>
            </div>
            <div class="stat-item">
                <div style="color:#888; font-size:0.8rem; text-transform:uppercase;">Total Page Views</div>
                <div class="stat-value" id="total-visits">---</div>
            </div>
            <div class="stat-item">
                <div style="color:#888; font-size:0.8rem; text-transform:uppercase;">System Status</div>
                <div class="stat-value" style="color:#00C853;">100% SECURE</div>
            </div>
        </div>
        
        <p style="color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;"><b>STRICT LEGAL WARNING & DISCLAIMER</b></p>
        <p style="text-align:justify; max-width:800px; margin: 0 auto; line-height:1.4;">
            © 2026 Market Insider Pro. All Rights Reserved.<br><br>
            <strong>INTELLECTUAL PROPERTY:</strong> The algorithms, design, code, and strategies contained within this platform are proprietary. Unauthorized reproduction, scraping, reverse engineering, or distribution is strictly prohibited and protected by international intellectual property laws. Violators will be prosecuted to the maximum extent of the law.<br><br>
            <strong>RISK DISCLAIMER:</strong> Trading cryptocurrencies, forex, and stocks involves significant risk and can result in the loss of your invested capital. The information, signals, and backtesting results provided on this platform are for educational purposes only and do NOT constitute financial advice. Past performance is not indicative of future results. Always conduct your own research.
        </p>
    </div>
    
    <script>
    // VISITOR COUNTER SCRIPT
    document.addEventListener("DOMContentLoaded", function() {
        // 1. Total Visits (Local Storage Increment)
        let visits = localStorage.getItem("mip_total_visits");
        if (!visits) { visits = Math.floor(Math.random() * 5000) + 10000; } // Base iniziale credibile
        visits = parseInt(visits) + 1;
        localStorage.setItem("mip_total_visits", visits);
        document.getElementById("total-visits").innerText = visits.toLocaleString();
        
        // 2. Live Users (Simulated Social Proof)
        let baseUsers = Math.floor(Math.random() * 50) + 150;
        document.getElementById("live-users").innerText = baseUsers;
        setInterval(() => {
            let fluctuation = Math.floor(Math.random() * 7) - 3; // -3 to +3
            baseUsers += fluctuation;
            if(baseUsers < 100) baseUsers = 100;
            document.getElementById("live-users").innerText = baseUsers;
        }, 5000);
    });
    </script>
    '''

MODALS_HTML = '''
<div class="modal-overlay" id="waitlist-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 id="modal-title" style="color:#FFD700; margin-top:0;">👑 VIP WAITLIST</h2><p id="modal-desc" style="color:#aaa; font-size:0.9rem;">Join the waitlist to get early access to institutional signals.</p><div id="waitlist-form"><input type="email" id="waitlist-email" class="modal-input" placeholder="Enter your best email..."><button class="btn-trade" style="width:85%; padding:12px;" onclick="submitWaitlist()">REQUEST ACCESS</button></div><div id="waitlist-success" style="display:none; color:#00C853; font-weight:bold; margin-top:20px;">✅ Request received! Keep an eye on your inbox.</div></div></div>
<div class="modal-overlay" id="login-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 style="margin-top:0;">Secure Login</h2><p style="color:#aaa; font-size:0.9rem;">Access your encrypted local workspace.</p><input type="text" id="login-name" class="modal-input" placeholder="Display name..."><button class="vip-btn" style="width:85%; padding:12px;" onclick="doLogin()">INITIALIZE TERMINAL</button></div></div>
<script>
    function openWaitlist(sourceText) { 
        if(sourceText === 'API') {
            document.getElementById('modal-title').innerText = '🤖 AUTO-TRADE BETA';
            document.getElementById('modal-desc').innerText = 'The API Auto-Execution engine is currently in Closed Beta for VIP members. Enter your email to join the waitlist.';
        } else {
            document.getElementById('modal-title').innerText = '👑 VIP PASS WAITLIST';
            document.getElementById('modal-desc').innerText = 'Join the waitlist to get early access to institutional signals and advanced courses.';
        }
        document.getElementById('waitlist-modal').style.display = 'flex'; 
    }
    function openLogin() { document.getElementById('login-modal').style.display = 'flex'; }
    function closeModals() { document.querySelectorAll('.modal-overlay').forEach(m => m.style.display = 'none'); }
    function submitWaitlist() { let e = document.getElementById('waitlist-email').value; if(e.includes('@')) { document.getElementById('waitlist-form').style.display = 'none'; document.getElementById('waitlist-success').style.display = 'block'; } else { alert("Please enter a valid email."); } }
    function doLogin() { let n = document.getElementById('login-name').value; if(n) { localStorage.setItem('mip_user', n); closeModals(); checkLogin(); } }
    function checkLogin() { let u = localStorage.getItem('mip_user'); if(u) { let g = document.getElementById('user-greeting'); let b = document.getElementById('login-btn'); if(g) { g.innerText = "👤 " + u; g.style.display = "inline"; } if(b) b.style.display = "none"; } }
    document.addEventListener("DOMContentLoaded", checkLogin);
</script>
'''

ACADEMY_CONTENT = {
    "mod1": {"title": "MODULE 1: THE MINDSET 🧠", "lessons": [{"id": "lez1_1", "title": "1.1 Psychology of a Winner", "vip": False, "html": "<h1>Trading Psychology</h1><p>Trading is 20% strategy and 80% psychology.</p>"}]},
    "mod3": {"title": "MODULE 3: WHALE TRACKING 🐳", "lessons": [{"id": "lez3_1", "title": "3.1 Institutional Strategy", "vip": True, "html": "<h1>The Whale Order Block</h1><p>Exact strategy used by institutional banks...</p>"}]}
}