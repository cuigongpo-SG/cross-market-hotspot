import asyncio
from typing import List
from .models import Item

async def fetch_amazon(keyword: str) -> List[Item]:
    """Placeholder Amazon fetcher.
    Real implementation would call Keepa/Helium10 API or Playwright scraper.
    Returns empty list for now.
    """
    await asyncio.sleep(0)  # simulate async
    return []
