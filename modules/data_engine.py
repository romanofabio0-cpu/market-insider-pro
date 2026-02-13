import json
import requests
import yfinance as yf
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from core.config import get_logger
from modules.analysis import analizza_segnale_tecnico

logger = get_logger("DataEngine")

def scarica_crypto_live() -> Dict[str, Any]:
    """Scarica i prezzi reali da CoinGecko API"""
    logger.info("📡 Scaricando dati Crypto Live...")
    # Lista ID corretti per CoinGecko
    ids = "bitcoin,ethereum,binancecoin,solana,ripple,cardano,dogecoin,polkadot,tron,chainlink,matic-network,shiba-inu,litecoin,uniswap,stellar,render-token,fetch-ai,singularitynet,pepe"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"⚠️ Errore API Crypto: {response.status_code}")
            return {}
    except Exception as e:
        logger.error(f"⚠️ Eccezione API Crypto: {e}")
        return {}

def scarica_azioni_live() -> List[Dict]:
    """Scarica prezzi Azionari, Commodities e Forex da Yahoo Finance"""
    logger.info("📈 Scaricando dati Multi-Asset Live...")
    
    # Abbiamo aggiunto Oro (GC=F), Petrolio (CL=F) e EUR/USD (EURUSD=X)
    tickers_map = {
        "NVDA": "Nvidia", "TSLA": "Tesla", "AAPL": "Apple", "MSFT": "Microsoft", 
        "COIN": "Coinbase", "MSTR": "MicroStrategy",
        "GC=F": "Gold", "CL=F": "Crude Oil", "EURUSD=X": "EUR/USD"
    }
    tickers_list = list(tickers_map.keys())
    dati_azioni = []
    
    try:
        data = yf.download(tickers_list, period="2d", group_by='ticker', progress=False)
        
        for symbol in tickers_list:
            try:
                import pandas as pd
                ticker_data = data
                if isinstance(data.columns, pd.MultiIndex):
                    try:
                        ticker_data = data[symbol]
                    except KeyError:
                        continue
                
                hist = ticker_data
                if len(hist) >= 2:
                    price = float(hist['Close'].iloc[-1])
                    prev_close = float(hist['Close'].iloc[-2])
                    change = ((price - prev_close) / prev_close) * 100
                    
                    sig_txt, sig_col = analizza_segnale_tecnico(change)
                    
                    # Usa il nome bello dalla mappa
                    display_name = tickers_map[symbol]
                    # ID pulito per l'HTML (senza = o X)
                    clean_id = symbol.replace("=", "").replace("X", "").lower()
                    
                    # TradingView symbol formatting
                    tv_symbol = f"NASDAQ:{symbol}"
                    if symbol == "GC=F": tv_symbol = "COMEX:GC1!"
                    elif symbol == "CL=F": tv_symbol = "NYMEX:CL1!"
                    elif symbol == "EURUSD=X": tv_symbol = "FX:EURUSD"
                    
                    dati_azioni.append({
                        "id": clean_id,
                        "cg_id": "stock", 
                        "type": "MACRO" if "=" in symbol else "STOCK",
                        "name": display_name, 
                        "symbol": symbol.replace("=F", "").replace("=X", ""),
                        "price": round(price, 4) if "USD" in symbol else round(price, 2),
                        "change": round(change, 2),
                        "tv": tv_symbol,
                        "signal": sig_txt,
                        "sig_col": sig_col
                    })
            except Exception as e:
                continue
    except Exception as e:
        logger.error(f"⚠️ Errore Yahoo Finance: {e}")
    
    return dati_azioni

def genera_dataset_completo(db_crypto: Dict) -> List[Dict]:
    assets = []
    
    # Mappa: ID CoinGecko -> Simbolo Display
    crypto_map = {
        "bitcoin": "BTC", "ethereum": "ETH", "binancecoin": "BNB", "solana": "SOL", "ripple": "XRP",
        "cardano": "ADA", "dogecoin": "DOGE", "polkadot": "DOT", "tron": "TRX", "chainlink": "LINK",
        "matic-network": "MATIC", "shiba-inu": "SHIB", "litecoin": "LTC", "uniswap": "UNI", "stellar": "XLM",
        "render-token": "RNDR", "fetch-ai": "FET", "singularitynet": "AGIX", "pepe": "PEPE"
    }
    
    for cid, symbol in crypto_map.items():
        if cid in db_crypto:
            data = db_crypto[cid]
            price = data.get('usd', 0)
            change = data.get('usd_24h_change', 0)
            
            sig_txt, sig_col = analizza_segnale_tecnico(change)
            
            assets.append({
                "id": symbol.lower(), # ID interno (es: btc)
                "cg_id": cid,         # ID CoinGecko VERO (es: bitcoin) -> FONDAMENTALE PER IL REAL TIME
                "type": "CRYPTO",
                "name": cid.title().replace("-", " "),
                "symbol": symbol,
                "price": price,
                "change": round(change, 2),
                "tv": f"BINANCE:{symbol}USD",
                "signal": sig_txt,
                "sig_col": sig_col
            })

    # Aggiungi azioni
    import pandas as pd # Assicura import pandas se serve per yfinance check
    stock_assets = scarica_azioni_live()
    assets.extend(stock_assets)
    
    assets.sort(key=lambda x: x['change'], reverse=True)
    return assets

# --- FUNZIONI ACCESSORIE (News, Macro, Smart Money) ---
# Le teniamo semplici per non allungare troppo il codice qui, usa quelle standard
def genera_smart_money() -> List[Dict]:
    return [] # Placeholder per brevità, tanto non le stiamo usando ora

def genera_calendario_macro() -> List[Dict]:
    oggi = datetime.now()
    eventi = [
        {"evento": "CPI Inflation", "impatto": "ALTO 🔴", "previsto": "2.4%", "precedente": "2.5%"},
        {"evento": "FED Rate Decision", "impatto": "CRITICO 🔥", "previsto": "4.50%", "precedente": "4.75%"}
    ]
    calendario = []
    for i, ev in enumerate(eventi):
        ev["data"] = (oggi + timedelta(days=i*5)).strftime("%d/%m")
        calendario.append(ev)
    return calendario