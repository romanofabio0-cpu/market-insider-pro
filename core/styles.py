
"""
Modulo contenente lo stile CSS dell'applicazione.
"""

CSS_CORE = """
<style>
    :root { --bg: #050505; --card: #111; --border: #222; --accent: #2962FF; --text: #e0e0e0; --green: #00e676; --red: #ff1744; --yellow: #FFD700; }
    body { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 0; line-height: 1.6; }
    a { text-decoration: none; color: inherit; transition: 0.2s; }
    
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: var(--bg); }
    ::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
    
    header { background: rgba(10,10,10,0.95); border-bottom: 1px solid var(--border); padding: 15px 40px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; backdrop-filter: blur(10px); }
    .logo { font-size: 1.8rem; font-weight: 800; letter-spacing: -1px; color: #fff; }
    .logo span { color: var(--accent); }
    .nav { display: flex; gap: 25px; align-items: center; }
    .nav a { font-weight: 600; font-size: 0.9rem; color: #888; text-transform: uppercase; padding: 5px 10px; border-radius: 4px; }
    .nav a:hover, .nav a.active { color: #fff; background: rgba(255,255,255,0.05); }
    .vip-btn { background: linear-gradient(45deg, #FFD700, #FFA500); color: #000 !important; font-weight: bold; padding: 8px 20px !important; border-radius: 20px; box-shadow: 0 0 15px rgba(255, 215, 0, 0.3); animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.4); } 70% { box-shadow: 0 0 0 10px rgba(255, 215, 0, 0); } 100% { box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); } }

    .container { max-width: 1600px; margin: 0 auto; padding: 40px 20px; }
    h2.section-title { font-size: 1.5rem; border-left: 5px solid var(--accent); padding-left: 20px; margin: 50px 0 30px 0; color: #fff; display: flex; align-items: center; gap: 10px; }
    
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }
    .card-link { display: block; }
    .card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 20px; position: relative; transition: all 0.2s; }
    .card:hover { transform: translateY(-3px); border-color: var(--accent); z-index: 10; box-shadow: 0 5px 20px rgba(0,0,0,0.5); }
    .card-head { display: flex; justify-content: space-between; margin-bottom: 10px; }
    .symbol { font-weight: 800; color: #fff; font-size: 1.1rem; }
    .name { font-size: 0.8rem; color: #666; }
    .price { font-size: 1.4rem; font-weight: 700; color: #fff; }
    .change { font-weight: bold; font-size: 0.9rem; }
    .signal-box { margin-top: 15px; padding-top: 10px; border-top: 1px solid #222; font-size: 0.75rem; color: #888; display: flex; justify-content: space-between; }
    .green { color: var(--green); } .red { color: var(--red); } .grey { color: #888; }

    .split-layout { display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-top: 40px; }
    .table-wrapper { background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; height: fit-content; }
    table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    th { background: #151515; padding: 15px; text-align: left; color: #666; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; border-bottom: 1px solid var(--border); }
    td { padding: 12px 15px; border-bottom: 1px solid #222; color: #ccc; }
    tr:hover td { background: #1a1a1a; }
    .tag { padding: 3px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }
    .tag-buy { background: rgba(0, 230, 118, 0.1); color: var(--green); border: 1px solid rgba(0, 230, 118, 0.2); }
    .tag-sell { background: rgba(255, 23, 68, 0.1); color: var(--red); border: 1px solid rgba(255, 23, 68, 0.2); }
    .blur-row td { filter: blur(4px); user-select: none; opacity: 0.5; }
    .unlock-overlay { position: absolute; left: 50%; transform: translateX(-50%); background: #FFD700; color: #000; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.8rem; cursor: pointer; box-shadow: 0 0 10px rgba(0,0,0,0.5); }

    .academy-grid { display: grid; grid-template-columns: 300px 1fr; gap: 30px; }
    .sidebar { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; height: fit-content; }
    .module-title { color: var(--accent); font-weight: bold; margin-top: 25px; margin-bottom: 10px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid #222; padding-bottom: 5px; }
    .lesson-link { display: block; padding: 12px; border-radius: 6px; color: #888; margin-bottom: 5px; cursor: pointer; transition: 0.2s; font-size: 0.95rem; }
    .lesson-link:hover, .lesson-link.active { background: #222; color: #fff; padding-left: 18px; border-left: 3px solid var(--accent); }
    .lesson-content { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 50px; min-height: 600px; }
    .lesson-content h1 { color: #fff; font-size: 2rem; margin-top: 0; }
    .lesson-content h3 { color: var(--accent); margin-top: 30px; }
    .lesson-content p, .lesson-content li { font-size: 1.1rem; color: #ccc; margin-bottom: 15px; line-height: 1.8; }
    
    .chat-interface { max-width: 900px; margin: 0 auto; background: var(--card); border: 1px solid var(--border); border-radius: 12px; height: 75vh; display: flex; flex-direction: column; overflow: hidden; }
    .chat-history { flex: 1; padding: 30px; overflow-y: auto; display: flex; flex-direction: column; gap: 20px; }
    .msg { max-width: 75%; padding: 15px 20px; border-radius: 12px; font-size: 1rem; line-height: 1.5; }
    .msg-user { align-self: flex-end; background: var(--accent); color: white; border-bottom-right-radius: 2px; }
    .msg-ai { align-self: flex-start; background: #1f1f1f; color: #ddd; border-bottom-left-radius: 2px; border: 1px solid #333; }
    .chat-input-area { padding: 25px; background: #0f0f0f; border-top: 1px solid var(--border); display: flex; gap: 15px; }
    .chat-input { flex: 1; background: #1a1a1a; border: 1px solid #333; color: white; padding: 15px; border-radius: 8px; outline: none; font-size: 1rem; }
    .chat-btn { background: var(--accent); color: white; border: none; padding: 0 30px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.2s; }
    .chat-btn:hover { background: #1a4bd6; }

    footer { text-align: center; padding: 60px 20px; color: #666; font-size: 0.8rem; border-top: 1px solid var(--border); margin-top: 80px; background: #080808; }
    .legal-links a { color: #888; margin: 0 15px; }
</style>
/* --- NUOVI BOTTONI CTA --- */
.btn-trade {
    background: linear-gradient(90deg, #00C853, #64DD17);
    color: #000;
    font-weight: 800;
    padding: 6px 12px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.75rem;
    display: inline-block;
    box-shadow: 0 0 10px rgba(100, 221, 23, 0.4);
    transition: all 0.3s ease;
    animation: pulse 2s infinite;
}
.btn-trade:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(100, 221, 23, 0.8);
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0.7); }
    70% { box-shadow: 0 0 0 10px rgba(100, 221, 23, 0); }
    100% { box-shadow: 0 0 0 0 rgba(100, 221, 23, 0); }
}

/* Effetto Flash per aggiornamento prezzi */
.flash-up { animation: flashGreen 1s; }
.flash-down { animation: flashRed 1s; }

@keyframes flashGreen { 0% { color: #00FF00; text-shadow:0 0 10px #00FF00; } 100% { color: inherit; } }
@keyframes flashRed { 0% { color: #FF0000; text-shadow:0 0 10px #FF0000; } 100% { color: inherit; } }
"""
