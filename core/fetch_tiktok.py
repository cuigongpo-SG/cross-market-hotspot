import asyncio, json, os
from typing import List
from .models import Item
from hermes_tools import terminal

async def _run_tiktok_scraper(hashtag: str) -> List[Item]:
    """Run `tiktok-scraper` for the given hashtag and parse JSON output.
    Returns a list of Item objects (only a subset of fields filled)."""
    cmd = f"tiktok-scraper hashtag {hashtag} -l 20 -j"  # -l limit, -j json output
    result = terminal(command=cmd, timeout=120)
    if result["exit_code"] != 0:
        # scraper failed – return empty list and log error
        return []
    try:
        data = json.loads(result["output"].strip())
    except Exception:
        return []
    items: List[Item] = []
    for vid in data.get("videos", []):
        # Try to extract product link from description if any
        title = vid.get("title", "")
        url = vid.get("url", "")
        likes = vid.get("stats", {}).get("diggCount")
        views = vid.get("stats", {}).get("playCount")
        # Simple heuristic: if description contains "http" treat it as product URL
        product_url = ""
        for token in title.split():
            if token.startswith("http"):
                product_url = token
                break
        items.append(Item(
            source="tiktok",
            title=title,
            url=product_url or url,
            likes=likes,
            views=views,
            tags=[hashtag],
            timestamp=datetime.utcnow()
        ))
    return items

async def fetch_tiktok(keyword: str) -> List[Item]:
    """Public fallback scraper for TikTok.
    Tries to search by hashtag derived from the keyword (e.g., "kitchen" -> "#kitchen").
    If `TIKTOK_SID_TT` env var is present, we could call the private API, but here we rely on the public scraper.
    """
    # Use the keyword directly as hashtag (strip spaces, lower case)
    hashtag = keyword.replace(" ", "").lower()
    return await _run_tiktok_scraper(hashtag)
