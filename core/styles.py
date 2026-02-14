CSS_CORE = '''<style>
/* --- BASE & LAYOUT (ANTI-THEFT) --- */
:root { --bg: #0a0a0a; --card-bg: #111; --text: #eee; --accent: #2962FF; --green: #00C853; --red: #FF3D00; --gold: #FFD700; --stripe: #635bff; }
body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; -webkit-user-select: none; user-select: none; overflow-x: hidden; }
a { text-decoration: none; color: inherit; transition: 0.3s; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }
header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #222; margin-bottom: 30px; }
.logo { font-size: 1.5rem; font-weight: 900; letter-spacing: -1px; }
.logo span { color: var(--text); } 
.nav { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
.nav a { font-size: 0.85rem; color: #888; font-weight: 600; text-transform: uppercase; }
.nav a.active, .nav a:hover { color: #fff; }
.vip-btn { background: var(--accent); color: #fff; padding: 8px 16px; border-radius: 4px; font-weight: 700; font-size: 0.8rem; border:none; cursor:pointer;}
.vip-btn:hover { background: #1c44b2; }

/* --- GRID, CARDS & WATCHLIST --- */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 40px; }
.card-wrapper { position: relative; }
.star-icon { position: absolute; top: 15px; right: 15px; font-size: 1.5rem; color: #444; cursor: pointer; z-index: 10; transition: 0.3s; text-shadow: 0 0 5px rgba(0,0,0,0.5); }
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

/* --- SEZIONI E PANNELLI --- */
.section-title { font-size: 1.2rem; font-weight: 800; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; border-left: 4px solid var(--accent); padding-left: 10px; }
.split-layout { display: grid; grid-template-columns: 1fr; gap: 30px; }
@media(min-width: 768px) { .split-layout { grid-template-columns: 1fr 1fr; } }
.panel { background: var(--card-bg); border: 1px solid #222; border-radius: 8px; padding: 20px; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
td, th { padding: 12px; text-align: left; border-bottom: 1px solid #222; }
th { font-size: 0.7rem; text-transform: uppercase; color: #666; }

/* --- PULSANTI E ANIMAZIONI --- */
.btn-trade { background: linear-gradient(90deg, #00C853, #64DD17); color: #000; font-weight: 800; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 0.75rem; display: inline-block; box-shadow: 0 0 10px rgba(100, 221, 23, 0.4); transition: all 0.3s ease; animation: pulse 2s infinite; border:none; cursor:pointer;}
.btn-trade:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(100, 221, 23, 0.8); }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(100, 221, 23, 0); } 100% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0); } }
.flash-up { animation: flashGreen 1s; }
.flash-down { animation: flashRed 1s; }
@keyframes flashGreen { 0% { color: #00FF00; text-shadow:0 0 10px #00FF00; } 100% { color: inherit; } }
@keyframes flashRed { 0% { color: #FF0000; text-shadow:0 0 10px #FF0000; } 100% { color: inherit; } }

/* --- FOMO FEED POPUP --- */
.fomo-popup { position: fixed; bottom: -100px; left: 20px; background: rgba(17, 17, 17, 0.95); border: 1px solid var(--accent); border-left: 4px solid var(--accent); padding: 15px 20px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); z-index: 9999; transition: bottom 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55); display: flex; align-items: center; gap: 15px; font-size: 0.9rem; backdrop-filter: blur(5px); }
.fomo-popup.show { bottom: 20px; }
.fomo-icon { background: rgba(41, 98, 255, 0.2); padding: 10px; border-radius: 50%; display: flex; justify-content: center; align-items: center; }

/* --- GDPR COOKIE BANNER --- */
.cookie-banner { position: fixed; bottom: -150px; left: 50%; transform: translateX(-50%); width: 90%; max-width: 600px; background: #111; border: 1px solid #333; border-radius: 8px 8px 0 0; padding: 20px; z-index: 10000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 -10px 30px rgba(0,0,0,0.8); transition: bottom 0.5s ease; }
.cookie-banner.show { bottom: 0; }
.cookie-text { font-size: 0.8rem; color: #aaa; }
.cookie-btn { background: var(--green); color: #000; border: none; padding: 10px 20px; font-weight: bold; border-radius: 4px; cursor: pointer; }

/* --- PRICING & STRIPE CHECKOUT --- */
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

/* --- LEADERBOARD --- */
.rank-1 { color: var(--gold) !important; font-size: 1.5rem; font-weight: 900; text-shadow: 0 0 10px rgba(255,215,0,0.5); }
.rank-2 { color: #C0C0C0 !important; font-size: 1.2rem; font-weight: bold; }
.rank-3 { color: #CD7F32 !important; font-size: 1.1rem; font-weight: bold; }
.user-row { background: rgba(41, 98, 255, 0.1) !important; border-left: 4px solid var(--accent) !important; }

/* --- ALTRI COMPONENTI --- */
.modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 9999; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-content { background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333; width: 90%; max-width: 400px; text-align: center; position: relative; }
.close-modal { position: absolute; top: 15px; right: 20px; font-size: 1.5rem; cursor: pointer; color: #888; }
.modal-input { width: 80%; padding: 12px; margin: 15px 0; background: #000; border: 1px solid #333; color: #fff; border-radius: 4px; font-family: 'Inter', sans-serif;}
.fng-meter, .broker-card, .wallet-form, .academy-grid, .chat-interface, .hacker-terminal, .backtest-box, .legal-footer, .stats-bar { /* (Mantenuti dal layout precedente) */ }
</style>'''