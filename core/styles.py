CSS_CORE = '''<style>
/* --- BASE & LAYOUT --- */
:root { --bg: #0a0a0a; --card-bg: #111; --text: #eee; --accent: #2962FF; --green: #00C853; --red: #FF3D00; }
body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; }
a { text-decoration: none; color: inherit; transition: 0.3s; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }
header { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; border-bottom: 1px solid #222; margin-bottom: 30px; }
.logo { font-size: 1.5rem; font-weight: 900; letter-spacing: -1px; }
.logo span { color: var(--text); } 
.nav { display: flex; align-items: center; gap: 20px; }
.nav a { font-size: 0.9rem; color: #888; font-weight: 500; }
.nav a.active, .nav a:hover { color: #fff; }
.vip-btn { background: var(--accent); color: #fff; padding: 8px 16px; border-radius: 4px; font-weight: 700; font-size: 0.8rem; border:none; cursor:pointer;}
.vip-btn:hover { background: #1c44b2; }

/* --- GRID & CARDS --- */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 40px; }
.card { background: var(--card-bg); border: 1px solid #222; padding: 20px; border-radius: 8px; transition: transform 0.2s; position: relative; overflow: hidden; }
.card:hover { transform: translateY(-5px); border-color: #333; }
.card-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.symbol { font-weight: 800; font-size: 1.1rem; }
.price { font-size: 1.8rem; font-weight: 700; margin: 10px 0; letter-spacing: -1px; }
.change { font-size: 0.9rem; font-weight: 600; }
.change.green { color: var(--green); }
.change.red { color: var(--red); }
.signal-box { margin-top: 15px; padding-top: 15px; border-top: 1px solid #222; display: flex; justify-content: space-between; font-size: 0.75rem; color: #666; }

/* --- INTELLIGENCE SECTION --- */
.section-title { font-size: 1.2rem; font-weight: 800; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; border-left: 4px solid var(--accent); padding-left: 10px; }
.split-layout { display: grid; grid-template-columns: 1fr; gap: 30px; }
@media(min-width: 768px) { .split-layout { grid-template-columns: 1fr 1fr; } }
.panel { background: var(--card-bg); border: 1px solid #222; border-radius: 8px; padding: 20px; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
td, th { padding: 12px; text-align: left; border-bottom: 1px solid #222; }
th { font-size: 0.7rem; text-transform: uppercase; color: #666; }

/* --- CTA BUTTONS --- */
.btn-trade { background: linear-gradient(90deg, #00C853, #64DD17); color: #000; font-weight: 800; padding: 6px 12px; border-radius: 4px; text-decoration: none; font-size: 0.75rem; display: inline-block; box-shadow: 0 0 10px rgba(100, 221, 23, 0.4); transition: all 0.3s ease; animation: pulse 2s infinite; border:none; cursor:pointer;}
.btn-trade:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(100, 221, 23, 0.8); }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(100, 221, 23, 0); } 100% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0); } }

/* --- FLASH EFFECT --- */
.flash-up { animation: flashGreen 1s; }
.flash-down { animation: flashRed 1s; }
@keyframes flashGreen { 0% { color: #00FF00; text-shadow:0 0 10px #00FF00; } 100% { color: inherit; } }
@keyframes flashRed { 0% { color: #FF0000; text-shadow:0 0 10px #FF0000; } 100% { color: inherit; } }

/* --- ACADEMY & CHAT --- */
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

/* --- MODALS (LOGIN & WAITLIST) --- */
.modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 999; justify-content: center; align-items: center; backdrop-filter: blur(5px); }
.modal-content { background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333; width: 90%; max-width: 400px; text-align: center; position: relative; }
.close-modal { position: absolute; top: 15px; right: 20px; font-size: 1.5rem; cursor: pointer; color: #888; }
.close-modal:hover { color: #fff; }
.modal-input { width: 80%; padding: 12px; margin: 15px 0; background: #000; border: 1px solid #333; color: #fff; border-radius: 4px; }

/* --- WALLET DASHBOARD --- */
.wallet-total { font-size: 3rem; font-weight: 900; color: var(--green); text-shadow: 0 0 20px rgba(0,200,83,0.3); margin: 10px 0 30px; }
.wallet-form { display: flex; gap: 10px; margin-bottom: 30px; background: #111; padding: 20px; border-radius: 8px; border: 1px solid #222;}
.wallet-form select, .wallet-form input { padding: 10px; background: #000; border: 1px solid #333; color: #fff; border-radius: 4px; flex: 1; }
</style>'''