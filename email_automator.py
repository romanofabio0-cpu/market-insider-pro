import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] EMAIL-ENGINE: %(message)s')

def genera_email_funnel():
    logging.info("Generazione Funnel Email di Benvenuto in corso...")
    
    email_1 = """OGGETTO: Benvenuto in Market Insider Pro 🚀
CORPO: Ciao! Hai fatto il primo passo verso il vantaggio statistico. 
Il 90% dei trader perde soldi perché non ha i dati giusti o si fa guidare dalle emozioni. 
Vai sulla nostra Dashboard e controlla i segnali AI aggiornati di oggi. Il mercato non aspetta."""
    
    email_2 = """OGGETTO: I segreti delle Balene 🐋
CORPO: Hai già visitato la nostra sezione 'Whale Tracker'? 
Seguire i soldi istituzionali è l'unico modo per anticipare i veri movimenti di mercato.
Scopri cosa stanno comprando i grandi fondi sbloccando la cronologia completa con il VIP PASS: [INSERISCI LINK STRIPE QUI]"""
    
    email_3 = """OGGETTO: Il tuo vantaggio sta per scadere ⏱️
CORPO: Non lasciare i tuoi futuri profitti sul tavolo. 
Sblocca i grafici PRO interattivi, chiedi analisi in tempo reale al nostro AI Analyst e ricevi i report giornalieri. 
Inizia la tua prova gratuita di 7 giorni a rischio zero e unisciti all'1% dei trader profittevoli."""
    
    # Crea la cartella se non esiste
    os.makedirs("emails_copy", exist_ok=True)
    filepath = os.path.join("emails_copy", "funnel_benvenuto.txt")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"--- EMAIL 1 (Giorno 0) ---\n{email_1}\n\n")
        f.write(f"--- EMAIL 2 (Giorno 2) ---\n{email_2}\n\n")
        f.write(f"--- EMAIL 3 (Giorno 4) ---\n{email_3}\n")
        
    logging.info(f"✅ Copy del funnel salvato con successo in: {filepath}")
    print("\n👉 Apri la cartella 'emails_copy', copia i testi e incollali nel tuo software di Email Marketing!")

if __name__ == "__main__":
    print("=========================================================")
    print("📥 MARKET INSIDER PRO - EMAIL FUNNEL GENERATOR           ")
    print("=========================================================")
    genera_email_funnel()