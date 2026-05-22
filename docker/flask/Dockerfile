FROM python:3.12-slim

WORKDIR /app

ENV FLASK_APP=app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 755 /app

# Production default — dev compose.yml overrides this with flask run
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "run:app"]
