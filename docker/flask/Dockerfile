FROM python:3.12-slim

WORKDIR /app

ENV FLASK_APP=app

# Build deps needed by cryptography (and other C-extension packages).
# Installed before pip, then cleaned up to keep the image small.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 755 /app

# Production default — dev compose.yml overrides this with flask run
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "run:app"]
