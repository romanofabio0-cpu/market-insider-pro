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
    ids = "bitcoin,ethereum,binancecoin,solana,ripple,cardano,dogecoin,polkadot,tron,chainlink,matic-network,shiba-inu,litecoin,uniswap,stellar,render-token,fetch-ai,singularitynet"
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
    """Scarica i prezzi reali da Yahoo Finance"""
    logger.info("📈 Scaricando dati Azionari Live...")
    # Lista delle azioni da monitorare
    tickers = ["NVDA", "TSLA", "AAPL", "MSFT", "AMZN", "GOOGL", "META", "AMD", "COIN", "MSTR", "PLTR", "HOOD", "PYPL", "UBER", "DIS"]
    dati_azioni = []
    
    try:
        # Scarica dati in blocco (più veloce)
        data = yf.download(tickers, period="2d", group_by='ticker', progress=False)
        
        for symbol in tickers:
            try:
                # Prende la chiusura di oggi (o ultimo prezzo) e quella di ieri
                hist = data[symbol]
                if len(hist) >= 2:
                    price = float(hist['Close'].iloc[-1])
                    prev_close = float(hist['Close'].iloc[-2])
                    change = ((price - prev_close) / prev_close) * 100
                    
                    sig_txt, sig_col = analizza_segnale_tecnico(change)
                    
                    dati_azioni.append({
                        "id": symbol.lower(),
                        "type": "STOCK",
                        "name": symbol, # Yahoo finance usa il ticker come nome breve
                        "symbol": symbol,
                        "price": round(price, 2),
                        "change": round(change, 2),
                        "tv": f"NASDAQ:{symbol}", # Per TradingView
                        "signal": sig_txt,
                        "sig_col": sig_col
                    })
            except Exception as e:
                logger.warning(f"Saltata {symbol}: {e}")
                continue
                
    except Exception as e:
        logger.error(f"⚠️ Errore Yahoo Finance: {e}")
    
    return dati_azioni

def genera_dataset_completo(db_crypto: Dict) -> List[Dict]:
    assets = []
    
    # 1. Elabora Crypto Reali
    crypto_map = {
        "bitcoin": "BTC", "ethereum": "ETH", "binancecoin": "BNB", "solana": "SOL", "ripple": "XRP",
        "cardano": "ADA", "dogecoin": "DOGE", "polkadot": "DOT", "tron": "TRX", "chainlink": "LINK",
        "matic-network": "MATIC", "shiba-inu": "SHIB", "litecoin": "LTC", "uniswap": "UNI", "stellar": "XLM",
        "ai16z": "AI16Z", "render-token": "RNDR", "fetch-ai": "FET", "singularitynet": "AGIX"
    }
    
    for cid, symbol in crypto_map.items():
        if cid in db_crypto:
            data = db_crypto[cid]
            price = data.get('usd', 0)
            change = data.get('usd_24h_change', 0)
            
            sig_txt, sig_col = analizza_segnale_tecnico(change)
            
            assets.append({
                "id": symbol.lower(),
                "type": "CRYPTO",
                "name": cid.title().replace("-", " "),
                "symbol": symbol,
                "price": price,
                "change": round(change, 2),
                "tv": f"BINANCE:{symbol}USD",
                "signal": sig_txt,
                "sig_col": sig_col
            })

    # 2. Aggiunge Azioni Reali
    stock_assets = scarica_azioni_live()
    assets.extend(stock_assets)
    
    # Ordina per performance (i migliori in alto)
    assets.sort(key=lambda x: x['change'], reverse=True)
    
    return assets

def genera_smart_money() -> List[Dict]:
    # (Per ora lasciamo questo simulato, nel prossimo step lo collegheremo alle news)
    names = ["Nancy Pelosi", "BlackRock", "Warren Buffet", "Elon Musk", "Ark Invest", "Michael Burry"]
    actions = ["BUY 🟢", "SELL 🔴", "ACCUMULATE 🔵"]
    assets_list = ["NVDA", "TSLA", "BTC", "ETH", "COIN", "MSTR"]
    data = []
    for i in range(15):
        data.append({
            "chi": random.choice(names),
            "asset": random.choice(assets_list),
            "azione": random.choice(actions),
            "valore": f"${random.randint(1, 50)}M",
            "data": f"{random.randint(1, 12)}h ago"
        })
    return data

def genera_calendario_macro() -> List[Dict]:
    # Placeholder per calendario reale (prossimo step)
    oggi = datetime.now()
    eventi = [
        {"evento": "CPI Inflation", "impatto": "ALTO 🔴", "previsto": "2.4%", "precedente": "2.5%"},
        {"evento": "FED Rate Decision", "impatto": "CRITICO 🔥", "previsto": "4.50%", "precedente": "4.75%"},
        {"evento": "NFP Payrolls", "impatto": "CRITICO 🔥", "previsto": "150K", "precedente": "142K"}
    ]
    calendario = []
    for i, ev in enumerate(eventi):
        data_ev = (oggi + timedelta(days=i*5)).strftime("%d/%m")
        ev["data"] = data_ev
        calendario.append(ev)
    return calendario