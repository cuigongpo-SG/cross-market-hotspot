from fastapi import FastAPI
import asyncio
from core.pipeline import pipeline

app = FastAPI()

@app.post("/analyze")
async def analyze(keywords: list[str]):
    markdown = await pipeline(keywords)
    return {"markdown": markdown}
