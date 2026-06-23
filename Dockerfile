FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app /app
CMD ["uvicorn", "gateway.main:app", "--host", "0.0.0.0", "--port", "8000"]
