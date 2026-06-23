import asyncio
from typing import List
from .models import Item

async def fetch_tiktok(keyword: str) -> List[Item]:
    """Placeholder TikTok fetcher.
    Real implementation would call TikTok Shop API or use tiktok‑scraper.
    Returns empty list for now.
    """
    await asyncio.sleep(0)
    return []
