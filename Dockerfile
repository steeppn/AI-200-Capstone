FROM python:3.11-slim

WORKDIR /app

COPY scripts/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY config.py .
COPY llm_config.yaml .
COPY main.py .
COPY classes/ ./classes/
COPY api/ ./api/
COPY models/ ./models/

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

