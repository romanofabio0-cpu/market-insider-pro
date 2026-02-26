CSS_CORE = '''<style>
/* --- BASE & LAYOUT (ANTI-THEFT) --- */
:root { --bg: #0a0a0a; --card-bg: #111; --text: #eee; --accent: #2962FF; --green: #00C853; --red: #FF3D00; --gold: #FFD700; --stripe: #635bff; }
body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; -webkit-user-select: none; user-select: none; overflow-x: hidden; }
a { text-decoration: none; color: inherit; transition: 0.3s; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }

/* FIX GRAFICO: Header con padding laterale e Sticky Glass Effect */
header { 
    display: flex; justify-content: space-between; align-items: center; 
    padding: 20px 5%; /* Spazio laterale di sicurezza */
    border-bottom: 1px solid #222; margin-bottom: 30px; 
    flex-wrap: wrap; gap: 15px; 
    position: sticky; top: 0; z-index: 1000; 
    background: rgba(10, 10, 10, 0.85); backdrop-filter: blur(12px); 
}

.logo { font-size: 1.5rem; font-weight: 900; letter-spacing: -1px; }
.logo span { color: var(--text); } 
.nav { display: flex; align-items: center; gap: 15px; flex-wrap: wrap; }
.nav a { font-size: 0.8rem; color: #888; font-weight: 600; text-transform: uppercase; }
.nav a.active, .nav a:hover { color: #fff; }
.vip-btn { background: var(--accent); color: #fff; padding: 8px 16px; border-radius: 4px; font-weight: 700; font-size: 0.8rem; border:none; cursor:pointer;}
.vip-btn:hover { background: #1c44b2; }

/* Grid, Cards, Watchlist, FOMO, Cookies */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 40px; }
.card-wrapper { position: relative; }
.star-icon { position: absolute; top: 15px; right: 15px; font-size: 1.5rem; color: #444; cursor: pointer; z-index: 10; transition: 0.3s; }
.star-icon:hover { transform: scale(1.2); }
.star-icon.active { color: var(--gold); text-shadow: 0 0 10px rgba(255,215,0,0.5); }
.card { background: var(--card-bg); border: 1px solid #222; padding: 20px; border-radius: 8px; transition: transform 0.2s; position: relative; overflow: hidden; height: 100%; box-sizing: border-box;}
.card:hover { transform: translateY(-5px); border-color: #333; }
.card-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-right: 25px;}
.symbol { font-weight: 800; font-size: 1.1rem; }
.price { font-size: 1.8rem; font-weight: 700; margin: 10px 0; letter-spacing: -1px; }
.change { font-size: 0.9rem; font-weight: 600; }
.change.green { color: var(--green); }
.change.red { color: var(--red); }
.signal-box { margin-top: 15px; padding-top: 15px; border-top: 1px solid #222; display: flex; justify-content: space-between; font-size: 0.75rem; color: #666; }
.section-title { font-size: 1.2rem; font-weight: 800; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; border-left: 4px solid var(--accent); padding-left: 10px; }
.split-layout { display: grid; grid-template-columns: 1fr; gap: 30px; }
@media(min-width: 768px) { .split-layout { grid-template-columns: 1fr 1fr; } }
.panel { background: var(--card-bg); border: 1px solid #222; border-radius: 8px; padding: 20px; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
td, th { padding: 12px; text-align: left; border-bottom: 1px solid #222; }
th { font-size: 0.7rem; text-transform: uppercase; color: #666; }
.btn-trade { background: linear-gradient(90deg, #00C853, #64DD17); color: #000; font-weight: 800; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 0.75rem; display: inline-block; box-shadow: 0 0 10px rgba(100, 221, 23, 0.4); transition: all 0.3s ease; animation: pulse 2s infinite; border:none; cursor:pointer;}
.btn-trade:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(100, 221, 23, 0.8); }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(100, 221, 23, 0); } 100% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0); } }
.flash-up { animation: flashGreen 1s; }
.flash-down { animation: flashRed 1s; }
@keyframes flashGreen { 0% { color: #00FF00; text-shadow:0 0 10px #00FF00; } 100% { color: inherit; } }
@keyframes flashRed { 0% { color: #FF0000; text-shadow:0 0 10px #FF0000; } 100% { color: inherit; } }
.fomo-popup { position: fixed; bottom: -100px; left: 20px; background: rgba(17, 17, 17, 0.95); border: 1px solid var(--accent); border-left: 4px solid var(--accent); padding: 15px 20px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); z-index: 9999; transition: bottom 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55); display: flex; align-items: center; gap: 15px; font-size: 0.9rem; backdrop-filter: blur(5px); }
.fomo-popup.show { bottom: 20px; }
.fomo-icon { background: rgba(41, 98, 255, 0.2); padding: 10px; border-radius: 50%; display: flex; justify-content: center; align-items: center; }
.cookie-banner { position: fixed; bottom: -150px; left: 50%; transform: translateX(-50%); width: 90%; max-width: 600px; background: #111; border: 1px solid #333; border-radius: 8px 8px 0 0; padding: 20px; z-index: 10000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 -10px 30px rgba(0,0,0,0.8); transition: bottom 0.5s ease; }
.cookie-banner.show { bottom: 0; }
.cookie-text { font-size: 0.8rem; color: #aaa; }
.cookie-btn { background: var(--green); color: #000; border: none; padding: 10px 20px; font-weight: bold; border-radius: 4px; cursor: pointer; }

/* --- MODALS & NEW SOCIAL LOGIN BUTTONS --- */
.modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 9999; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-content { background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333; width: 90%; max-width: 400px; text-align: center; position: relative; }
.close-modal { position: absolute; top: 15px; right: 20px; font-size: 1.5rem; cursor: pointer; color: #888; }
.modal-input { width: 100%; padding: 12px; margin: 15px 0; background: #000; border: 1px solid #333; color: #fff; border-radius: 4px; font-family: 'Inter', sans-serif; box-sizing: border-box;}

/* Bottoni Login Avanzati */
.auth-btn { width: 100%; padding: 12px; border-radius: 6px; font-weight: 600; font-size: 0.9rem; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px; border: none; transition: 0.2s; }
.btn-google { background: #fff; color: #333; border: 1px solid #ddd; }
.btn-google:hover { background: #f1f1f1; }
.btn-web3 { background: #F6851B; color: #fff; }
.btn-web3:hover { background: #e27615; }
.auth-divider { display: flex; align-items: center; text-align: center; margin: 20px 0; color: #666; font-size: 0.8rem; }
.auth-divider::before, .auth-divider::after { content: ''; flex: 1; border-bottom: 1px solid #333; }
.auth-divider:not(:empty)::before { margin-right: .25em; }
.auth-divider:not(:empty)::after { margin-left: .25em; }

/* Referral, Pricing, Stripe, Leaderboard */
.ref-box { background: linear-gradient(135deg, #111, #1a1a1a); border: 1px solid var(--accent); border-radius: 12px; padding: 40px; text-align: center; box-shadow: 0 10px 30px rgba(41, 98, 255, 0.1); margin-bottom: 40px; }
.ref-link-container { display: flex; justify-content: center; margin: 30px 0; }
.ref-link { background: #000; padding: 15px 20px; border: 1px solid #333; border-radius: 8px 0 0 8px; color: var(--gold); font-family: monospace; font-size: 1.1rem; width: 60%; max-width: 400px; }
.ref-copy { background: var(--accent); color: #fff; border: none; padding: 15px 25px; border-radius: 0 8px 8px 0; font-weight: bold; cursor: pointer; transition: 0.3s; }
.ref-copy:hover { background: #1c44b2; }
.progress-container { width: 100%; max-width: 500px; margin: 0 auto; background: #000; border-radius: 10px; border: 1px solid #333; overflow: hidden; height: 20px;}
.progress-bar { height: 100%; background: linear-gradient(90deg, #FFD700, #F57F17); width: 33%; transition: width 1s; }
.pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px; }
.pricing-card { background: #111; border: 1px solid #333; border-radius: 12px; padding: 40px 30px; text-align: center; position: relative; overflow: hidden; }
.pricing-card.pro { border-color: var(--gold); box-shadow: 0 10px 40px rgba(255,215,0,0.1); transform: scale(1.05); }
.pricing-card.pro::before { content: "MOST POPULAR"; position: absolute; top: 15px; right: -35px; background: var(--gold); color: #000; font-size: 0.7rem; font-weight: bold; padding: 5px 40px; transform: rotate(45deg); }
.price-tag { font-size: 3.5rem; font-weight: 900; margin: 20px 0; color: #fff; }
.price-tag span { font-size: 1rem; color: #666; font-weight: normal; }
.plan-feature { padding: 10px 0; border-bottom: 1px solid #222; font-size: 0.9rem; color: #aaa; text-align: left; }
.plan-feature::before { content: "✓ "; color: var(--green); font-weight: bold; }
.stripe-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 10000; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.stripe-modal { background: #fff; color: #333; padding: 0; border-radius: 12px; width: 90%; max-width: 400px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); overflow: hidden; position: relative; }
.stripe-header { background: #f7f9fc; padding: 20px; border-bottom: 1px solid #e6ebf1; text-align: center; }
.stripe-body { padding: 30px; }
.stripe-input { width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #e6ebf1; border-radius: 6px; box-sizing: border-box; font-family: 'Inter', sans-serif; }
.stripe-btn { width: 100%; background: var(--stripe); color: #fff; padding: 15px; border: none; border-radius: 6px; font-weight: bold; font-size: 1rem; cursor: pointer; transition: 0.3s; }
.stripe-btn:hover { background: #5449d9; }
.stripe-footer { font-size: 0.7rem; color: #aab7c4; text-align: center; margin-top: 15px; display: flex; justify-content: center; align-items: center; gap: 5px; }
.rank-1 { color: var(--gold) !important; font-size: 1.5rem; font-weight: 900; text-shadow: 0 0 10px rgba(255,215,0,0.5); }
.rank-2 { color: #C0C0C0 !important; font-size: 1.2rem; font-weight: bold; }
.rank-3 { color: #CD7F32 !important; font-size: 1.1rem; font-weight: bold; }
.user-row { background: rgba(41, 98, 255, 0.1) !important; border-left: 4px solid var(--accent) !important; }
.fng-meter { background: #000; border: 1px solid #333; border-radius: 8px; padding: 20px; text-align: center; }
.fng-value { font-size: 3rem; font-weight: 900; margin: 10px 0; }
.fng-bar { height: 10px; width: 100%; background: linear-gradient(90deg, #FF3D00, #FFD700, #00C853); border-radius: 5px; margin-top: 10px; position: relative; }
.fng-indicator { height: 20px; width: 4px; background: #fff; position: absolute; top: -5px; transition: 1s; box-shadow: 0 0 5px #fff; }
.broker-card { display: flex; align-items: center; justify-content: space-between; background: #111; border: 1px solid #333; padding: 20px; border-radius: 8px; margin-bottom: 15px; }
.broker-logo { font-size: 2rem; font-weight: 900; margin-right: 20px; }
.broker-info { flex: 1; }
.broker-tags span { background: #222; color: #aaa; padding: 4px 8px; border-radius: 4px; font-size: 0.7rem; margin-right: 5px; }
.signal-buy { color: var(--green); font-weight: bold; }
.signal-sell { color: var(--red); font-weight: bold; }
.wallet-total { font-size: 3rem; font-weight: 900; color: var(--green); text-shadow: 0 0 20px rgba(0,200,83,0.3); margin: 10px 0 30px; }
.wallet-form { display: flex; gap: 10px; margin-bottom: 30px; background: #111; padding: 20px; border-radius: 8px; border: 1px solid #222;}
.wallet-form select, .wallet-form input { padding: 10px; background: #000; border: 1px solid #333; color: #fff; border-radius: 4px; flex: 1; }
.academy-grid { display: grid; grid-template-columns: 250px 1fr; gap: 30px; }
.sidebar { border-right: 1px solid #222; padding-right: 20px; }
.module-title { font-weight: 800; color: #666; font-size: 0.8rem; margin: 20px 0 10px; text-transform: uppercase; }
.lesson-link { padding: 8px; cursor: pointer; border-radius: 4px; color: #aaa; font-size: 0.9rem; }
.lesson-link:hover { background: #1a1a1a; color: #fff; }
.chat-interface { height: 600px; display: flex; flex-direction: column; background: #111; border: 1px solid #333; border-radius: 8px; }
.chat-history { flex: 1; padding: 20px; overflow-y: auto; }
.msg { padding: 10px 15px; border-radius: 8px; margin-bottom: 10px; max-width: 80%; font-size: 0.9rem; }
.msg-ai { background: #1a1a1a; color: #ccc; border-left: 3px solid var(--accent); }
.msg-user { background: var(--accent); color: #fff; align-self: flex-end; margin-left: auto; }
.chat-input-area { padding: 20px; border-top: 1px solid #333; display: flex; gap: 10px; }
.chat-input { flex: 1; background: #000; border: 1px solid #333; color: #fff; padding: 10px; border-radius: 4px; }
.chat-btn { background: #fff; color: #000; border: none; padding: 0 20px; font-weight: 800; cursor: pointer; }
.hacker-terminal { background: #000; border: 1px solid #333; border-radius: 8px; padding: 20px; font-family: 'Courier New', Courier, monospace; color: #00C853; height: 150px; overflow-y: hidden; margin-top: 20px; box-shadow: inset 0 0 10px #000; }
.backtest-box { background: linear-gradient(135deg, #111, #1a1a1a); border: 1px solid var(--gold); border-radius: 8px; padding: 30px; text-align: center; margin-bottom:40px; box-shadow: 0 10px 30px rgba(255, 215, 0, 0.1); }
.backtest-result { font-size: 2.5rem; font-weight: 900; color: var(--gold); margin: 20px 0; }
.legal-footer { border-top: 1px solid #333; padding: 40px 0 20px; margin-top: 50px; text-align: center; font-size: 0.75rem; color: #555; }
.stats-bar { display: flex; justify-content: center; gap: 20px; margin-bottom: 20px; padding: 15px; background: #111; border-radius: 8px; border: 1px solid #222; flex-wrap: wrap;}
.stat-item { text-align: center; }
.stat-value { font-size: 1.5rem; font-weight: bold; color: #fff; }
</style>'''
# --- STILE DASHBOARD ISTITUZIONALE MIP ---
MIP_DASHBOARD_CSS = """
:root {
    --bg-dark: #0f172a; --bg-card: #1e293b; --text-main: #f8fafc; 
    --text-muted: #94a3b8; --gold: #d4af37; --sidebar-width: 250px;
}
body {
    margin: 0; font-family: 'Inter', system-ui, sans-serif; 
    background-color: #0b1120; color: var(--text-main);
    display: flex; height: 100vh; overflow: hidden;
}
/* SIDEBAR */
.sidebar {
    width: var(--sidebar-width); background-color: var(--bg-dark); 
    border-right: 1px solid #334155; display: flex; flex-direction: column; z-index: 10;
}
.sidebar-logo {
    padding: 20px; display: flex; align-items: center; gap: 15px; 
    font-weight: 800; font-size: 1.2rem; border-bottom: 1px solid #334155; color: var(--gold);
}
.sidebar-logo img { width: 45px; height: 45px; border-radius: 50%; border: 2px solid var(--gold); }
.nav-item {
    padding: 15px 20px; color: var(--text-muted); text-decoration: none; 
    font-weight: 500; border-left: 3px solid transparent; transition: all 0.2s ease;
}
.nav-item:hover { 
    background-color: #1e293b; color: white; border-left: 3px solid var(--gold); 
}
/* MAIN CONTENT */
.main-wrapper { flex: 1; overflow-y: auto; display: flex; flex-direction: column; }
.top-header {
    height: 70px; background-color: var(--bg-dark); border-bottom: 1px solid #334155;
    display: flex; align-items: center; justify-content: flex-end; padding: 0 30px;
}
.vip-btn {
    background: linear-gradient(135deg, var(--gold), #b88a00); color: #000; 
    padding: 10px 20px; border-radius: 6px; font-weight: bold; 
    text-decoration: none; box-shadow: 0 2px 10px rgba(212, 175, 55, 0.3);
}
.hero-banner {
    margin: 20px 30px; height: 220px; border-radius: 12px; overflow: hidden;
    background: linear-gradient(rgba(15,23,42,0.6), rgba(15,23,42,0.6)), url('banner_mip.jpg');
    background-size: cover; background-position: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
}
.hero-banner h1 { margin: 0; font-size: 2.8rem; color: white; letter-spacing: 1px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
.hero-banner p { color: var(--gold); font-size: 1.2rem; font-weight: 500; margin-top: 10px; }
.dashboard-content { padding: 0 30px 30px 30px; }

/* MOBILE RESPONSIVE */
@media (max-width: 768px) {
    body { flex-direction: column; overflow: auto; }
    .sidebar { width: 100%; height: auto; flex-direction: row; flex-wrap: wrap; justify-content: space-between; padding: 10px; }
    .sidebar-logo { padding: 10px; border-bottom: none; font-size: 1rem; }
    .nav-item { padding: 10px; font-size: 0.9rem; }
    .hero-banner { height: 160px; margin: 15px; }
    .hero-banner h1 { font-size: 1.8rem; }
    .dashboard-content { padding: 15px; }
}
"""
MIP_DASHBOARD_CSS = """
:root {
    --bg-dark: #0f172a; --bg-card: #1e293b; --text-main: #f8fafc; 
    --text-muted: #94a3b8; --gold: #d4af37; --sidebar-width: 250px;
}
body {
    margin: 0; font-family: 'Inter', system-ui, sans-serif; 
    background-color: #0b1120; color: var(--text-main);
    display: flex; height: 100vh; overflow: hidden;
}
.sidebar {
    width: var(--sidebar-width); background-color: var(--bg-dark); 
    border-right: 1px solid #334155; display: flex; flex-direction: column; z-index: 10;
}
.sidebar-logo {
    padding: 20px; display: flex; align-items: center; gap: 15px; 
    font-weight: 800; font-size: 1.2rem; border-bottom: 1px solid #334155; color: var(--gold);
}
.sidebar-logo img { width: 45px; height: 45px; border-radius: 50%; border: 2px solid var(--gold); }
.nav-item {
    padding: 15px 20px; color: var(--text-muted); text-decoration: none; 
    font-weight: 500; border-left: 3px solid transparent; transition: all 0.2s ease;
}
.nav-item:hover { 
    background-color: #1e293b; color: white; border-left: 3px solid var(--gold); 
}
.main-wrapper { flex: 1; overflow-y: auto; display: flex; flex-direction: column; }
.top-header {
    height: 70px; background-color: var(--bg-dark); border-bottom: 1px solid #334155;
    display: flex; align-items: center; justify-content: flex-end; padding: 0 30px;
}
.vip-btn {
    background: linear-gradient(135deg, var(--gold), #b88a00); color: #000; 
    padding: 10px 20px; border-radius: 6px; font-weight: bold; 
    text-decoration: none; box-shadow: 0 2px 10px rgba(212, 175, 55, 0.3);
}
.hero-banner {
    margin: 20px 30px; height: 220px; border-radius: 12px; overflow: hidden;
    background: linear-gradient(rgba(15,23,42,0.6), rgba(15,23,42,0.6)), url('banner_mip.jpg');
    background-size: cover; background-position: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;
}
.hero-banner h1 { margin: 0; font-size: 2.8rem; color: white; letter-spacing: 1px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
.hero-banner p { color: var(--gold); font-size: 1.2rem; font-weight: 500; margin-top: 10px; }
.dashboard-content { padding: 0 30px 30px 30px; }

@media (max-width: 768px) {
    body { flex-direction: column; overflow: auto; }
    .sidebar { width: 100%; height: auto; flex-direction: row; flex-wrap: wrap; justify-content: space-between; padding: 10px; }
    .sidebar-logo { padding: 10px; border-bottom: none; font-size: 1rem; }
    .nav-item { padding: 10px; font-size: 0.9rem; }
    .hero-banner { height: 160px; margin: 15px; }
    .hero-banner h1 { font-size: 1.8rem; }
    .dashboard-content { padding: 15px; }
}
"""