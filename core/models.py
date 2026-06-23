from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List, Optional

class Item(BaseModel):
    source: str  # "amazon" | "tiktok" | "trend"
    asin: Optional[str] = None
    product_id: Optional[str] = None
    title: str
    price: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    likes: Optional[int] = None
    views: Optional[int] = None
    tags: List[str] = []
    url: HttpUrl
    timestamp: datetime
    sales_rank: Optional[int] = None
    price_history: Optional[List[float]] = None
    review_sentiment_score: Optional[float] = None
