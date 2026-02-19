from core.styles import CSS_CORE

def get_header(active_page: str) -> str:
    seo_tags = '''
    <meta name="description" content="Market Insider Pro - Advanced Algorithmic Trading Terminal. Live data, institutional signals, and AI analysis.">
    <meta property="og:title" content="Market Insider Pro - Premium Terminal">
    <meta property="og:description" content="Join the elite. Access real-time institutional order flows and AI-driven market analysis.">
    <meta property="og:image" content="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80">
    <meta property="og:url" content="https://marketinsiderpro.com">
    <meta name='impact-site-verification' value='82817dc6-e0b3-48b6-b7d7-f89b6dbd7a06'>
    '''
    anti_theft_script = '''<script>document.addEventListener('contextmenu', e => e.preventDefault()); document.onkeydown = function(e) { if(e.keyCode == 123 || (e.ctrlKey && e.shiftKey && (e.keyCode == 73 || e.keyCode == 67 || e.keyCode == 74)) || (e.ctrlKey && e.keyCode == 85)) return false; }</script>'''

    return f'''
    {CSS_CORE} 
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
            <a href="stories.html" class="{'active' if active_page=='stories' else ''}">📖 Stories</a>
            <a href="vip_lounge.html" class="{'active' if active_page=='vip' else ''}" style="color:#FFD700; text-shadow:0 0 5px rgba(255,215,0,0.5);">💎 VIP Area</a>
            <a href="brokers.html" class="{'active' if active_page=='brokers' else ''}">Brokers</a>
            <a href="tools.html" class="{'active' if active_page=='tools' else ''}">🛠️ Arsenal</a>
            <a href="referral.html" class="{'active' if active_page=='referral' else ''}" style="color:var(--gold);">🎁 Invite</a>
            
            <span id="user-greeting" style="color:#00C853; font-weight:bold; display:none; padding:8px 15px; border-radius:4px; background:#111; border:1px solid #333;"></span>
            <button id="login-btn" class="vip-btn" onclick="openLogin()" style="background:#333;">SIGN IN</button>
            <a href="pricing.html" class="vip-btn" style="background: linear-gradient(45deg, #FFD700, #F57F17); color:#000;">VIP PASS 👑</a>
        </nav>
    </header>
    '''

def get_footer() -> str:
    return '''
    <div class="legal-footer container">
        <div class="stats-bar"><div class="stat-item"><div style="color:#00C853; font-size:0.8rem; font-weight:bold;">● LIVE TRADERS</div><div class="stat-value" id="live-users">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">Total Page Views</div><div class="stat-value" id="total-visits">---</div></div><div class="stat-item"><div style="color:#888; font-size:0.8rem; text-transform:uppercase;">System Status</div><div class="stat-value" style="color:#00C853;">100% SECURE</div></div></div>
        <div style="margin: 30px 0;"><a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Privacy Policy</a> | <a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Terms of Service</a> | <a href="legal.html" style="color:#888; margin: 0 10px; text-decoration:underline;">Risk Disclaimer</a></div>
        <p style="color:#888; text-transform:uppercase; letter-spacing:1px; margin-bottom:10px;"><b>STRICT LEGAL WARNING & RISK DISCLAIMER</b></p>
        <p style="text-align:justify; max-width:800px; margin: 0 auto 20px; line-height:1.4; font-size:0.75rem; color:#555;">Trading cryptocurrencies, stocks, and forex carries a high level of risk and may not be suitable for all investors. The high degree of leverage can work against you as well as for you. Before deciding to trade, you should carefully consider your investment objectives, level of experience, and risk appetite. Market Insider Pro is strictly an <b>educational platform</b>. The algorithms, signals, and charts provided do not constitute financial advice. You are solely responsible for your own capital. Past performance is not indicative of future results.</p>
        <p style="text-align:justify; max-width:800px; margin: 0 auto; line-height:1.4;">© 2026 Market Insider Pro. All Rights Reserved.</p>
    </div>
    <div class="fomo-popup" id="fomo-box"><div class="fomo-icon">⚡</div><div id="fomo-text">User99 just upgraded to VIP Pass.</div></div>
    <div class="cookie-banner" id="cookie-banner"><div class="cookie-text">We use cookies to secure your session and provide real-time institutional data. By continuing to use this site, you consent to our <a href="legal.html" style="color:var(--accent);">Privacy Policy</a>.</div><button class="cookie-btn" onclick="acceptCookies()">ACCEPT</button></div>

    <script>
    const originalFetch = window.fetch;
    window.fetch = async function() {
        if (typeof arguments[0] === 'string' && arguments[0].includes('coingecko')) {
            return new Response(JSON.stringify({}), { status: 200 }); 
        }
        return originalFetch.apply(this, arguments);
    };

    document.addEventListener("DOMContentLoaded", function() {
        let visits = localStorage.getItem("mip_total_visits"); if (!visits) visits = Math.floor(Math.random() * 5000) + 10000; localStorage.setItem("mip_total_visits", ++visits); let tv = document.getElementById("total-visits"); if(tv) tv.innerText = visits.toLocaleString();
        let baseUsers = Math.floor(Math.random() * 50) + 150; let lu = document.getElementById("live-users"); if(lu) lu.innerText = baseUsers;
        setInterval(() => { let f = Math.floor(Math.random() * 7) - 3; baseUsers += f; if(baseUsers < 100) baseUsers = 100; if(lu) lu.innerText = baseUsers; }, 5000);
        
        const fomoMsgs = ["🐋 Whale Alert: $4.2M moved to Binance", "🟢 User from Milan just went LONG on Bitcoin", "🔥 A user just unlocked the VIP Pass", "🚨 Algorithm detected high volatility on SOL", "💰 User from Rome secured +45% profit on NVDA"];
        setInterval(() => { let box = document.getElementById('fomo-box'); if(box) { document.getElementById('fomo-text').innerText = fomoMsgs[Math.floor(Math.random()*fomoMsgs.length)]; box.classList.add('show'); setTimeout(() => box.classList.remove('show'), 5000); } }, 15000);
        
        if(!localStorage.getItem('mip_cookies_accepted')) { setTimeout(()=> document.getElementById('cookie-banner').classList.add('show'), 2000); }
        
        async function updateLivePrices() {
            try {
                let res = await originalFetch('https://api.binance.com/api/v3/ticker/price');
                let data = await res.json();
                
                let priceMap = {};
                data.forEach(item => { priceMap[item.symbol] = item.price; });
                
                let targets = {
                    "btc": priceMap["BTCUSDT"], "eth": priceMap["ETHUSDT"], "sol": priceMap["SOLUSDT"],
                    "xrp": priceMap["XRPUSDT"], "ada": priceMap["ADAUSDT"], "doge": priceMap["DOGEUSDT"],
                    "pepe": priceMap["1000PEPEUSDT"] || priceMap["PEPEUSDT"],
                    "rndr": priceMap["RENDERUSDT"] || priceMap["RNDRUSDT"]
                };

                for (const [id, price] of Object.entries(targets)) {
                    if(price) {
                        let el = document.getElementById("price-" + id);
                        if(el) {
                            let p = parseFloat(price);
                            let decimals = p < 0.1 ? 6 : (p < 2 ? 4 : 2);
                            let formattedPrice = "$" + p.toLocaleString('en-US', {minimumFractionDigits: decimals, maximumFractionDigits: decimals});
                            
                            if(el.innerText !== formattedPrice) {
                                el.innerText = formattedPrice;
                                el.style.color = "#00C853";
                                setTimeout(() => el.style.color = "white", 500);
                            }
                        }
                    }
                }
            } catch (e) { }
        }
        
        if(document.body.innerText.includes('GLOBAL MARKETS PULSE')) {
            updateLivePrices();
            setInterval(updateLivePrices, 3000);
        }
    });
    function acceptCookies() { localStorage.setItem('mip_cookies_accepted', 'true'); document.getElementById('cookie-banner').classList.remove('show'); }
    </script>
    '''

MODALS_HTML = '''
<div class="modal-overlay" id="waitlist-modal"><div class="modal-content"><span class="close-modal" onclick="closeModals()">&times;</span><h2 id="modal-title" style="color:#FFD700; margin-top:0;">🤖 AUTO-TRADE BETA</h2><p id="modal-desc" style="color:#aaa; font-size:0.9rem;">The API Auto-Execution engine is currently in Closed Beta. Enter your email to join the waitlist.</p><div id="waitlist-form"><input type="email" id="waitlist-email" class="modal-input" placeholder="name@company.com"><button class="btn-trade" style="width:100%; padding:12px;" onclick="window.submitFirebaseWaitlist()">REQUEST ACCESS</button></div><div id="waitlist-success" style="display:none; color:#00C853; font-weight:bold; margin-top:20px;">✅ Valid Request Received! Check your inbox.</div></div></div>

<div class="modal-overlay" id="login-modal">
    <div class="modal-content">
        <span class="close-modal" onclick="closeModals()">&times;</span>
        <h2 style="margin-top:0;">Sign In</h2>
        <p style="color:#aaa; font-size:0.9rem; margin-bottom:25px;">Access your institutional workspace.</p>
        
        <button class="auth-btn btn-web3" onclick="loginWeb3()">
            <svg width="20" height="20" viewBox="0 0 32 32" fill="none"><path d="M31.066 12.355c-0.126-0.347-0.428-0.597-0.793-0.658l-8.665-1.428-3.419-7.971c-0.155-0.362-0.505-0.599-0.899-0.599s-0.744 0.237-0.899 0.599l-3.419 7.971-8.665 1.428c-0.365 0.061-0.667 0.311-0.793 0.658s-0.038 0.748 0.231 1.002l6.471 6.115-1.848 8.423c-0.075 0.342 0.054 0.702 0.336 0.906s0.669 0.222 0.984 0.052l7.533-4.062 7.533 4.062c0.141 0.076 0.297 0.113 0.452 0.113 0.183 0 0.365-0.055 0.531-0.165 0.282-0.204 0.411-0.564 0.336-0.906l-1.848-8.423 6.471-6.115c0.269-0.254 0.357-0.655 0.231-1.002z" fill="#fff"/></svg>
            Connect Web3 Wallet
        </button>
        
        <button class="auth-btn btn-google" onclick="window.triggerGoogleLogin()">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>
            Continue with Google
        </button>
        
        <div class="auth-divider">or use email</div>
        
        <input type="email" id="login-email" class="modal-input" placeholder="name@company.com">
        <button class="vip-btn" style="width:100%; padding:12px; margin-top:5px;" onclick="loginEmail()">SIGN IN</button>
    </div>
</div>

<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
  import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

  const firebaseConfig = {
    apiKey: "AIzaSyDKYdyh3y-SWCPSciwvVkmnpAoom8fTFM4",
    authDomain: "market-insider-pro.firebaseapp.com",
    projectId: "market-insider-pro",
    storageBucket: "market-insider-pro.firebasestorage.app",
    messagingSenderId: "1019243929111",
    appId: "1:1019243929111:web:99815e309d933d0b2f8652",
    measurementId: "G-431ECSCM9B"
  };

  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  const provider = new GoogleAuthProvider();
  const db = getFirestore(app);

  window.triggerGoogleLogin = function() {
      signInWithPopup(auth, provider).then((result) => {
          let displayName = result.user.displayName || result.user.email.split('@')[0];
          localStorage.setItem('mip_user', displayName);
          closeModals(); checkLogin(); location.reload();
      }).catch((error) => { alert("Errore Login Google: " + error.message); });
  };

  window.submitFirebaseWaitlist = async function() {
      let e = document.getElementById('waitlist-email').value; 
      const re = /^(([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/;
      
      if(re.test(String(e).toLowerCase())) { 
          let btn = document.querySelector('#waitlist-form .btn-trade');
          btn.innerText = "SAVING... ⏳"; btn.style.opacity = "0.7";
          try {
              await addDoc(collection(db, "waitlist_emails"), { email: e, timestamp: serverTimestamp(), source: "Market Insider Pro" });
              document.getElementById('waitlist-form').style.display = 'none'; 
              document.getElementById('waitlist-success').style.display = 'block'; 
          } catch (error) {
              alert("Server Error: Impossibile salvare l'email (" + error.message + ")");
              btn.innerText = "REQUEST ACCESS"; btn.style.opacity = "1";
          }
      } else { alert("Security Error: Please enter a valid email address format."); } 
  };
</script>

<script>
    function validateEmail(email) { const re = /^(([^<>()\\[\\]\\\\.,;:\\s@"]+(\\.[^<>()\\[\\]\\\\.,;:\\s@"]+)*)|(".+"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/; return re.test(String(email).toLowerCase()); }
    function loginEmail() { let e = document.getElementById('login-email').value; if(validateEmail(e)) { localStorage.setItem('mip_user', e.split('@')[0]); closeModals(); checkLogin(); location.reload(); } else { alert("Login Failed: Invalid email."); } }
    async function loginWeb3() { if (typeof window.ethereum !== 'undefined') { try { const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' }); localStorage.setItem('mip_user', accounts[0].substring(0,6) + '...' + accounts[0].substring(accounts[0].length-4)); closeModals(); checkLogin(); location.reload(); } catch (error) { alert("Connection refused."); } } else { alert("Please install MetaMask."); } }
    
    function openWaitlist() { document.getElementById('waitlist-modal').style.display = 'flex'; }
    function openLogin() { document.getElementById('login-modal').style.display = 'flex'; }
    function closeModals() { document.querySelectorAll('.modal-overlay').forEach(m => m.style.display = 'none'); }
    
    function checkLogin() { 
        let u = localStorage.getItem('mip_user'); 
        let isVip = localStorage.getItem('mip_vip_status') === 'active';
        if(u) { 
            let g = document.getElementById('user-greeting'); 
            let b = document.getElementById('login-btn'); 
            if(g) { 
                let badge = isVip ? ' <span style="background:var(--gold); color:#000; padding:2px 6px; border-radius:4px; font-size:0.75rem; font-weight:900; margin-left:8px;">VIP</span>' : '';
                g.innerHTML = (u.startsWith('0x') ? '🦊 ' : '👤 ') + u + badge; 
                g.style.display = "inline"; 
            } 
            if(b) b.style.display = "none"; 
        } 
    }
    document.addEventListener("DOMContentLoaded", checkLogin);
</script>
'''

# === CABINA DI REGIA AFFILIAZIONI (RENDITE PASSIVE) ===
AMAZON_LINK_BOOK = "https://www.amazon.it/s?k=trading+in+the+zone+libro&tag=mip081-21"
AMAZON_LINK_MONITOR = "https://www.amazon.it/s?k=monitor+lg+34+pollici+ultrawide&tag=mip081-21"
AMAZON_LINK_LEDGER = "https://www.amazon.it/s?k=ledger+nano+x+wallet&tag=mip081-21"
BINANCE_AFFILIATE_LINK = "https://accounts.binance.com/register?ref=1218170181"
BYBIT_AFFILIATE_LINK = "https://www.bybit.eu/invite?ref=PXANQ70"

ACADEMY_CONTENT = {
    "mod1": {
        "title": "MODULE 1: THE MINDSET 🧠", 
        "lessons": [
            {
                "id": "lez1_1", 
                "title": "1.1 The 1% Psychology", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">The 1% Psychology</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Welcome to Market Insider Pro. Before touching any algorithm or chart, you must understand a brutal truth: <b>90% of retail traders lose money</b>. Why? Because they trade with emotion, FOMO (Fear Of Missing Out), and panic.</p>
                <h3 style="color:#fff; margin-top:30px;">The Institutional Edge</h3>
                <p style="color:#888; line-height:1.6;">Institutions do not feel fear. They use algorithms to execute trades based on pure data, volume, and statistical probability. To win, you must rewire your brain to think like a machine.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FFD700; border-radius:8px;'>
                    <h3 style="color:#FFD700; margin-top:0;">📚 Required Reading</h3>
                    <p style="color:#ccc;">We highly recommend starting your journey by reading "Trading in the Zone" by Mark Douglas. It will completely destroy your emotional biases.</p>
                    <a href='{AMAZON_LINK_BOOK}' target='_blank' class='vip-btn' style='background: linear-gradient(45deg, #ff9900, #ffc107); color:black; text-decoration:none; display:inline-block; margin-top:10px;'>BUY ON AMAZON 🛒</a>
                </div>
                '''
            }
        ]
    },
    "mod2": {
        "title": "MODULE 2: TECHNICAL MASTERY 📈", 
        "lessons": [
            {
                "id": "lez2_1", 
                "title": "2.1 Naked Charting", 
                "vip": False, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">Naked Charting & Liquidity</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">Throw away your complex indicators. Retail traders crowd their screens with RSI, MACD, and Bollinger Bands. Smart money only looks at two things: <b>Price Action</b> and <b>Volume</b>.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FCD535; border-radius:8px;'>
                    <h3 style="color:#FCD535; margin-top:0;">🖥️ The Pro Setup</h3>
                    <p style="color:#ccc;">You cannot trade order blocks on a laptop screen. An Ultrawide Monitor is mandatory to see the full market structure without scrolling.</p>
                    <a href='{AMAZON_LINK_MONITOR}' target='_blank' class='vip-btn' style='background:#f5f5f5; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>GET THE LG 34" ULTRAWIDE 🛒</a>
                </div>
                <div style='margin-top:20px; padding:30px; background:#1a1a1a; border-left:4px solid #FCD535; border-radius:8px;'>
                    <h3 style="color:#FCD535; margin-top:0;">🏦 The Right Exchange</h3>
                    <p style="color:#ccc;">To trade our volume strategies, you need an exchange with the highest global liquidity and zero-slippage execution. We exclusively use Binance.</p>
                    <a href='{BINANCE_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background:#FCD535; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>CLAIM $100 BINANCE BONUS</a>
                </div>
                '''
            }
        ]
    },
    "mod3": {
        "title": "MODULE 3: WHALE TRACKING 🐳", 
        "lessons": [
            {
                "id": "lez3_1", 
                "title": "3.1 Order Block Secrets", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">Finding The Whale Order Blocks</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">This is the exact strategy used by institutional banks. We track large wallet movements and front-run the retail liquidity.</p>
                <p style="color:#888; line-height:1.6;">Order Blocks (OBs) are specific areas on a chart where central banks or large institutions have accumulated or distributed massive quantities of an asset. They leave a footprint.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #00C853; border-radius:8px;'>
                    <h3 style="color:#00C853; margin-top:0;">🔐 Securing Whale Profits</h3>
                    <p style="color:#ccc;">When you track whales, you make whale money. NEVER keep large capital on an exchange. Store your long-term holdings offline securely.</p>
                    <a href='{AMAZON_LINK_LEDGER}' target='_blank' class='vip-btn' style='background:#00C853; color:black; text-decoration:none; display:inline-block; margin-top:10px;'>BUY LEDGER NANO X 🛒</a>
                </div>
                '''
            }
        ]
    },
    "mod4": {
        "title": "MODULE 4: ALGO & BOTS 🤖", 
        "lessons": [
            {
                "id": "lez4_1", 
                "title": "4.1 Setup Auto-Trading", 
                "vip": True, 
                "html": f'''
                <h1 style="color:#fff; font-size:2.5rem; margin-bottom:10px;">Connecting the AI</h1>
                <p style="color:#aaa; font-size:1.1rem; line-height:1.6;">You now have the knowledge. It's time to automate it. Our API Hub allows you to connect your exchange via secure API keys and let our algorithm execute Order Block strategies 24/7.</p>
                <div style='margin-top:40px; padding:30px; background:#1a1a1a; border-left:4px solid #FF9900; border-radius:8px;'>
                    <h3 style="color:#FF9900; margin-top:0;">⚡ Mandatory Requirement</h3>
                    <p style="color:#ccc;">Our high-frequency bots require extremely low API latency. We strongly advise setting up a dedicated Bybit Pro account for algorithm execution.</p>
                    <a href='{BYBIT_AFFILIATE_LINK}' target='_blank' class='vip-btn' style='background:#17181E; border:1px solid #FF9900; color:#FF9900; text-decoration:none; display:inline-block; margin-top:10px;'>OPEN BYBIT PRO ACCOUNT</a>
                </div>
                '''
            }
        ]
    }
}