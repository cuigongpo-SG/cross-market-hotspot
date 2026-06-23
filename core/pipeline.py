import asyncio
from typing import List
from .models import Item
from .fetch_amazon import fetch_amazon
from .fetch_tiktok import fetch_tiktok
from .fetch_trends import fetch_trends
from .llm_service import call_llm
from .report_service import render_markdown

async def pipeline(keywords: List[str]):
    """Orchestrates data collection, LLM analysis and markdown rendering.
    Returns the final markdown string.
    """
    # 1️⃣ 并行抓取 Amazon 与 TikTok（每个关键词分别抓取）
    async def collect_source(src_func, kw):
        return await src_func(kw)

    amazon_tasks = [collect_source(fetch_amazon, kw) for kw in keywords]
    tiktok_tasks = [collect_source(fetch_tiktok, kw) for kw in keywords]
    amazon_items = await asyncio.gather(*amazon_tasks)
    tiktok_items = await asyncio.gather(*tiktok_tasks)
    # flatten
    items = [i for sub in amazon_items + tiktok_items for i in sub]

    # 2️⃣（可选）抓取 Google Trends
    trend_items = await fetch_trends(keywords)
    items.extend(trend_items)

    # 3️⃣ LLM 分析
    llm_input = {"items": [item.dict() for item in items]}
    llm_result = call_llm(llm_input)

    # 4️⃣ 渲染 markdown 报告
    markdown = render_markdown(llm_result)
    return markdown
