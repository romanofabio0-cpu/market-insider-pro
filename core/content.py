def get_header(active_page: str) -> str:
    return f'''
    <header>
        <div class="logo">MARKET<span>INSIDER</span> PRO</div>
        <nav class="nav">
            <a href="index.html" class="{'active' if active_page=='home' else ''}">Terminal</a>
            <a href="academy_lez1_1.html" class="{'active' if active_page=='academy' else ''}">Academy</a>
            <a href="wallet.html" class="{'active' if active_page=='wallet' else ''}">My Wallet</a>
            <a href="chat.html" class="{'active' if active_page=='chat' else ''}">AI Analyst</a>
            <span id="user-greeting" style="color:#00C853; font-weight:bold; display:none;"></span>
            <button id="login-btn" class="vip-btn" onclick="openLogin()" style="background:#333;">LOGIN</button>
            <button class="vip-btn" onclick="openWaitlist()" style="background: linear-gradient(45deg, #FFD700, #F57F17); color:#000;">VIP PASS 👑</button>
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

# --- MODALI GLOBALI (Verranno iniettati in ogni pagina) ---
MODALS_HTML = '''
<div class="modal-overlay" id="waitlist-modal">
    <div class="modal-content">
        <span class="close-modal" onclick="closeModals()">&times;</span>
        <h2 style="color:#FFD700; margin-top:0;">👑 VIP WAITLIST</h2>
        <p style="color:#aaa; font-size:0.9rem;">The VIP Section is currently invite-only. Join the waitlist to get early access to institutional signals and advanced courses.</p>
        <div id="waitlist-form">
            <input type="email" id="waitlist-email" class="modal-input" placeholder="Enter your email address...">
            <button class="btn-trade" style="width:85%; padding:12px;" onclick="submitWaitlist()">JOIN WAITLIST</button>
        </div>
        <div id="waitlist-success" style="display:none; color:#00C853; font-weight:bold; margin-top:20px;">
            ✅ You are on the list! Keep an eye on your inbox.
        </div>
    </div>
</div>

<div class="modal-overlay" id="login-modal">
    <div class="modal-content">
        <span class="close-modal" onclick="closeModals()">&times;</span>
        <h2 style="margin-top:0;">Welcome Back</h2>
        <p style="color:#aaa; font-size:0.9rem;">Create your local profile to track your portfolio.</p>
        <input type="text" id="login-name" class="modal-input" placeholder="Enter your display name...">
        <button class="vip-btn" style="width:85%; padding:12px;" onclick="doLogin()">ACCESS TERMINAL</button>
    </div>
</div>

<script>
    function openWaitlist() { document.getElementById('waitlist-modal').style.display = 'flex'; }
    function openLogin() { document.getElementById('login-modal').style.display = 'flex'; }
    function closeModals() { document.querySelectorAll('.modal-overlay').forEach(m => m.style.display = 'none'); }
    
    function submitWaitlist() {
        let email = document.getElementById('waitlist-email').value;
        if(email.includes('@')) {
            document.getElementById('waitlist-form').style.display = 'none';
            document.getElementById('waitlist-success').style.display = 'block';
        } else { alert("Please enter a valid email."); }
    }

    function doLogin() {
        let name = document.getElementById('login-name').value;
        if(name) {
            localStorage.setItem('mip_user', name);
            closeModals();
            checkLogin();
        }
    }

    function checkLogin() {
        let user = localStorage.getItem('mip_user');
        if(user) {
            let greeting = document.getElementById('user-greeting');
            let loginBtn = document.getElementById('login-btn');
            if(greeting) { greeting.innerText = "👤 " + user; greeting.style.display = "inline"; }
            if(loginBtn) loginBtn.style.display = "none";
        }
    }
    
    // Check login on page load
    document.addEventListener("DOMContentLoaded", checkLogin);
</script>
'''

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: THE MINDSET 🧠",
        "lessons": [
            {
                "id": "lez1_1",
                "title": "1.1 Psychology of a Winner",
                "vip": False,
                "html": """
                <h1>Trading Psychology: The 80/20 Rule</h1>
                <p>Most beginners think trading is about charts. <strong>It is not.</strong></p>
                <p>Trading is 20% strategy and 80% psychology. If you cannot control your emotions (Fear & Greed), you will lose money even with the best strategy in the world.</p>
                <div style="margin-top:40px; padding:20px; background:#1a1a1a; border-left:4px solid #FFD700; border-radius:4px;">
                    <h3>📚 Recommended Reading</h3>
                    <p>The bible of trading psychology is "Trading in the Zone" by Mark Douglas.</p>
                    <br>
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
                "title": "3.1 Smart Money Strategy",
                "vip": True,
                "html": """
                <h1>The Whale Order Block</h1>
                <p>Here is the exact strategy used by institutional banks to manipulate retail liquidity...</p>
                """
            }
        ]
    }
}