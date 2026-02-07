from typing import Tuple

def analizza_segnale_tecnico(change_24h: float) -> Tuple[str, str]:
    '''
    Simula un algoritmo di analisi tecnica basato sulla volatilità.
    '''
    rsi_simulato = 50 + (change_24h * 2.5)
    
    if rsi_simulato > 75: return "STRONG BUY 🚀", "green"
    if rsi_simulato > 60: return "BUY 🟢", "green"
    if rsi_simulato < 25: return "STRONG SELL 🩸", "red"
    if rsi_simulato < 40: return "SELL 🔴", "red"
    return "NEUTRAL ⚪", "grey"
