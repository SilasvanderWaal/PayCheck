#!/usr/bin/env bash
# deploy.sh — pull latest, rebuild, run migrations
# Usage: bash scripts/deploy.sh
set -euo pipefail

COMPOSE="sudo docker compose -f docker-compose.prod.yml"

echo "==> Pulling latest code..."
git pull origin main

echo "==> Building and starting containers..."
$COMPOSE up --build -d

echo "==> Waiting for DB to be healthy..."
$COMPOSE exec -T db bash -c "until mysqladmin ping -h localhost --silent; do sleep 2; done"

echo "==> Running DB migrations..."
$COMPOSE exec -T web flask db upgrade

echo "==> Deploy complete."
$COMPOSE ps
