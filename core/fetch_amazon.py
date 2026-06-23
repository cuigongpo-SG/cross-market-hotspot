import asyncio, json, os
from datetime import datetime
from typing import List
from .models import Item
from hermes_tools import terminal

async def _run_playwright_amazon(keyword: str) -> List[Item]:
    """Runs a short Playwright script to scrape Amazon search results for the given keyword.
    Returns a list of Item objects (max 5)."""
    # Inline Python script executed via `python - <<'PY'`
    script = f"""
import json, asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f'https://www.amazon.com/s?k={keyword}')
        await page.wait_for_selector('div.s-main-slot')
        results = []
        items = await page.query_selector_all('div.s-main-slot div[data-component-type="s-search-result"]')
        for item in items[:5]:
            title_el = await item.query_selector('h2 a span')
            title = await title_el.inner_text() if title_el else ''
            url_el = await item.query_selector('h2 a')
            url = await url_el.get_attribute('href') if url_el else ''
            price_whole_el = await item.query_selector('span.a-price-whole')
            price_whole = await price_whole_el.inner_text() if price_whole_el else ''
            price_frac_el = await item.query_selector('span.a-price-fraction')
            price_frac = await price_frac_el.inner_text() if price_frac_el else ''
            price = f"{price_whole}{price_frac}" if price_whole else ''
            rating_el = await item.query_selector('i span.a-icon-alt')
            rating = await rating_el.inner_text() if rating_el else ''
            reviews_el = await item.query_selector('span[aria-label$="ratings"]')
            reviews = await reviews_el.get_attribute('aria-label') if reviews_el else ''
            results.append({
                'title': title,
                'url': 'https://www.amazon.com' + url if url else '',
                'price': price,
                'rating': rating,
                'reviews': reviews,
            })
        print(json.dumps(results))
        await browser.close()
asyncio.run(main())
"""
    # Execute the script via terminal tool
    res = terminal(command=f"python - <<'PY'\n{script}\nPY", timeout=180)
    if res["exit_code"] != 0:
        return []
    try:
        data = json.loads(res["output"].strip())
    except Exception:
        return []
    items: List[Item] = []
    for entry in data:
        items.append(Item(
            source="amazon",
            title=entry.get("title", ""),
            url=entry.get("url", ""),
            price=entry.get("price"),
            rating=float(entry.get("rating", "0").split()[0]) if entry.get("rating") else None,
            review_count=int(''.join(filter(str.isdigit, entry.get("reviews", "0")))) if entry.get("reviews") else None,
            timestamp=datetime.utcnow()
        ))
    return items

async def fetch_amazon(keyword: str) -> List[Item]:
    """Public Amazon scraper using Playwright. Returns up to 5 items per keyword."""
    return await _run_playwright_amazon(keyword)
