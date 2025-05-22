import feedparser
import json
import os
import locale



from datetime import datetime, timedelta

# Configuration de la locale pour le formatage des dates en français
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


CACHE_FILE = "rss_cache.json"
CACHE_DURATION_MINUTES = 10



def is_cache_valid():
    if not os.path.exists(CACHE_FILE):
        return False
    cache_mtime = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    return datetime.now() - cache_mtime < timedelta(minutes=CACHE_DURATION_MINUTES)

def get_articles():
    if is_cache_valid():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
FEEDS = [
    {"name": "GreenIT", "url": "https://www.greenit.fr/feed/"},
    {"name": "Novethic", "url": "https://www.novethic.fr/rss/rss.xml"},
    {"name": "Next INpact", "url": "https://www.nextinpact.com/rss"},
    {"name": "01net", "url": "https://www.01net.com/rss/"},
    {"name": "Les Numériques", "url": "https://www.lesnumeriques.com/rss"},
    {"name": "Symfony", "url": "https://symfony.com/blog/rss.xml"},
    {"name": "Code du Garage", "url": "https://code-garage.com/blog/rss"},
]

SOURCE_STYLE = {
    "GreenIT": {"color": "border-green-400", "icon": "🌱"},
    "Novethic": {"color": "border-blue-400", "icon": "📘"},
    "Next INpact": {"color": "border-indigo-400", "icon": "⚙️"},
    "01net": {"color": "border-red-400", "icon": "💻"},
    "Les Numériques": {"color": "border-yellow-400", "icon": "📷"},
    "Code du Garage": {"color": "border-gray-400 ", "icon": "🧰"},
    "Symfony": {"color": "border-purple-400", "icon": "🧩"},
}

def get_articles():
    articles = []
    for feed in FEEDS:
        parsed_feed = feedparser.parse(feed["url"])
        source_style = SOURCE_STYLE.get(feed["name"], {"color": "bg-gray-100", "icon": "📰"})
        print(f"--- {feed['name']} ---")
        print(f"Nombre d'articles récupérés : {len(parsed_feed.entries)}")
        for entry in parsed_feed.entries[:3]:  # Limite à 3 articles par flux
            
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "image": entry.image if hasattr(entry, 'image') else None,
                "summary": entry.summary,
                "published": entry.published if hasattr(entry, 'published') else entry.updated,
                "published_parsed": entry.published_parsed if hasattr(entry, 'published_parsed') else entry.updated_parsed,
                "published_str": datetime(*entry.published_parsed[:6]).strftime("%A %d %B %Y à %H:%M") if hasattr(entry, 'published_parsed') else datetime(*entry.updated_parsed[:6]).strftime("%A %d %B %Y à %H:%M"),
                "source": feed["name"],
                "color": source_style["color"],
                "icon": source_style["icon"]
            })
    
    # On trie les articles après avoir tous récupérés
    articles.sort(key=lambda x: x["published"], reverse=True)

    # Sauvegarde dans le cache
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False)

    return articles