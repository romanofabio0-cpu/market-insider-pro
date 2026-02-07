import urllib.request
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from core.config import get_logger
from modules.analysis import analizza_segnale_tecnico

logger = get_logger("DataEngine")

def scarica_crypto_live() -> Dict[str, Any]:
    logger.info("📡 Connessione API CoinGecko...")
    ids = "bitcoin,ethereum,binancecoin,solana,ripple,cardano,staked-ether,avalanche-2,dogecoin,polkadot,tron,chainlink,matic-network,shiba-inu,litecoin,bitcoin-cash,uniswap,stellar,monero,ethereum-classic"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MarketInsiderBot/1.0'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        logger.warning(f"⚠️ Errore API: {e}")
        return {}

def genera_dataset_completo(db_live: Dict) -> List[Dict]:
    assets = []
    # Crypto
    crypto_map = {
        "bitcoin": "BTC", "ethereum": "ETH", "binancecoin": "BNB", "solana": "SOL", "ripple": "XRP",
        "cardano": "ADA", "dogecoin": "DOGE", "polkadot": "DOT", "tron": "TRX", "chainlink": "LINK",
        "matic-network": "MATIC", "shiba-inu": "SHIB", "litecoin": "LTC", "uniswap": "UNI", "stellar": "XLM"
    }
    for cid, symbol in crypto_map.items():
        data = db_live.get(cid, {})
        price = data.get('usd', 0)
        change = data.get('usd_24h_change', 0)
        sig_txt, sig_col = analizza_segnale_tecnico(change)
        assets.append({
            "id": symbol.lower(), "type": "CRYPTO", "name": cid.title(), "symbol": symbol,
            "price": price, "change": change, "tv": f"BINANCE:{symbol}USD", "signal": sig_txt, "sig_col": sig_col
        })

    # Stocks
    stocks = [
        ("NVDA", "NVIDIA", 148.50), ("TSLA", "Tesla", 325.10), ("AAPL", "Apple", 224.00), ("MSFT", "Microsoft", 418.00),
        ("AMZN", "Amazon", 198.00), ("GOOGL", "Google", 175.00), ("META", "Meta", 592.00), ("NFLX", "Netflix", 750.00),
        ("AMD", "AMD", 160.00), ("INTC", "Intel", 22.50), ("COIN", "Coinbase", 250.00), ("MSTR", "MicroStrategy", 380.00),
        ("PLTR", "Palantir", 45.00), ("HOOD", "Robinhood", 25.00), ("PYPL", "PayPal", 78.00), ("SQ", "Block", 80.00),
        ("UBER", "Uber", 75.00), ("ABNB", "Airbnb", 130.00), ("DIS", "Disney", 95.00), ("NKE", "Nike", 85.00),
        ("JPM", "JPMorgan", 210.00), ("BAC", "Bank of America", 38.00), ("GS", "Goldman Sachs", 510.00), ("V", "Visa", 280.00),
        ("MA", "Mastercard", 490.00), ("KO", "Coca-Cola", 68.00), ("PEP", "PepsiCo", 170.00), ("MCD", "McDonald's", 290.00),
        ("WMT", "Walmart", 70.00), ("TGT", "Target", 150.00)
    ]
    for s, n, p in stocks:
        var = round(random.uniform(-4.5, 4.5), 2)
        sig_txt, sig_col = analizza_segnale_tecnico(var)
        assets.append({"id": s.lower(), "type": "STOCK", "name": n, "symbol": s, "price": p, "change": var, "tv": f"NASDAQ:{s}", "signal": sig_txt, "sig_col": sig_col})
        
    return assets

def genera_smart_money() -> List[Dict]:
    names = ["Nancy Pelosi", "BlackRock", "Warren Buffet", "Elon Musk", "Mark Zuckerberg", "Jeff Bezos", "Cathie Wood", "Michael Burry", "Whale 0x7a...", "Whale 0x9b...", "Citadel LLC", "Bridgewater", "State Street", "Vanguard", "Senator Cruz", "Rep. Crenshaw"]
    actions = ["BUY 🟢", "SELL 🔴", "ACCUMULATE 🔵", "DUMP 🔻"]
    data = []
    for i in range(25):
        asset = random.choice(["NVDA", "TSLA", "BTC", "ETH", "AAPL", "MSFT", "PLTR", "COIN"])
        val = f"${random.randint(1, 50)}.{random.randint(1, 9)}M"
        data.append({"chi": names[i % len(names)], "asset": asset, "azione": random.choice(actions), "valore": val, "data": f"{random.randint(1, 12)}h ago"})
    return data

def genera_calendario_macro() -> List[Dict]:
    oggi = datetime.now()
    eventi = [
        {"evento": "CPI Inflation Data", "impatto": "ALTO 🔴", "previsto": "2.4%", "precedente": "2.5%"},
        {"evento": "FED Rate Decision", "impatto": "CRITICO 🔥", "previsto": "4.50%", "precedente": "4.75%"},
        {"evento": "Jobless Claims", "impatto": "MEDIO 🟡", "previsto": "220K", "precedente": "218K"},
        {"evento": "GDP Growth Rate", "impatto": "ALTO 🔴", "previsto": "2.1%", "precedente": "2.0%"},
        {"evento": "NFP Payrolls", "impatto": "CRITICO 🔥", "previsto": "150K", "precedente": "142K"}
    ]
    calendario = []
    for i, ev in enumerate(eventi):
        data_ev = (oggi + timedelta(days=i*3)).strftime("%d/%m")
        ev["data"] = data_ev
        calendario.append(ev)
    return calendario
