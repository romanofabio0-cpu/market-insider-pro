# vip_report_gen.py
import os
from datetime import datetime
# Importiamo le tue funzioni esistenti senza modificarle
from modules.data_engine import scarica_crypto_live, genera_dataset_completo
from core.config import OUTPUT_FOLDER, get_logger
from core.styles import CSS_CORE

logger = get_logger("VIP_Report")

def build_daily_vip_report():
    logger.info("Generazione Daily VIP Report in corso...")
    
    # Usiamo il tuo motore dati
    db_crypto = scarica_crypto_live()
    assets = genera_dataset_completo(db_crypto)
    
    oggi = datetime.now().strftime("%d %B %Y")
    
    # Filtriamo solo i segnali "STRONG"
    top_picks = [a for a in assets if "STRONG" in a['signal']]
    
    picks_html = ""
    for a in top_picks:
        picks_html += f"<li><strong>{a['symbol']}</strong>: {a['price']}$ -> Segnale AI: <span style='color:{a['sig_col']}'>{a['signal']}</span></li>"
        
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>VIP Briefing - {oggi}</title>
    {CSS_CORE}
    </head><body>
    <div class="container">
        <h1 style="color:#FFD700">👑 DAILY INSIDER BRIEFING</h1>
        <p style="color:#888">Data: {oggi} | Confidenziale</p>
        <hr style="border-color:#333">
        <h2>🔥 Top AI Picks di Oggi</h2>
        <ul>{picks_html if picks_html else "Nessun segnale forte rilevato oggi. Mantenere la liquidità."}</ul>
        <p style="margin-top:50px; font-size:0.8rem; color:#666;">Market Insider Pro - Solo per membri VIP.</p>
    </div>
    </body></html>"""
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        
    filepath = os.path.join(OUTPUT_FOLDER, "vip_daily_secret.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
    logger.info(f"✅ VIP Report generato: {filepath}")

if __name__ == "__main__":
    build_daily_vip_report()