FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir playwright && \
    playwright install --with-deps chromium

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
# Ensure node and tiktok-scraper are available (already installed globally on host)
ENV PATH="/home/ubuntu/.hermes/profiles/telegram-bot/node/bin:$PATH"
CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
