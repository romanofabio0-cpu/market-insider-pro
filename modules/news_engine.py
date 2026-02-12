import feedparser
from typing import List, Dict
from core.config import get_logger
from datetime import datetime

logger = get_logger("NewsEngine")

def scarica_news() -> List[Dict]:
    """Scarica le ultime notizie da fonti finanziarie affidabili"""
    logger.info("📰 Scaricando Flash News...")
    
    # Fonti RSS (Affidabili e Veloci)
    feeds = [
        # Crypto
        "https://cointelegraph.com/rss",
        # Stocks / Macro
        "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664" 
    ]
    
    news_items = []
    
    try:
        for url in feeds:
            feed = feedparser.parse(url)
            for entry in feed.entries[:4]: # Prendiamo le prime 4 per ogni fonte
                # Pulizia data (se presente)
                data_pub = entry.published if 'published' in entry else "Just now"
                
                news_items.append({
                    "title": entry.title,
                    "link": entry.link,
                    "source": feed.feed.title if 'title' in feed.feed else "Market News",
                    "published": data_pub[:16] # Taglia la data per non farla lunghissima
                })
    except Exception as e:
        logger.error(f"⚠️ Errore News: {e}")
        # News di backup in caso di errore
        return [{"title": "Market Data update running...", "link": "#", "source": "System", "published": "Now"}]

    # Mescoliamo le news per non avere solo crypto in cima? 
    # Meglio lasciarle ordinate o alternate. Per ora lista semplice.
    return news_items[:8] # Ritorniamo le 8 più recenti totali