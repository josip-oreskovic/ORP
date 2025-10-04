# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]