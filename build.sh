#!/bin/bash

echo "FROM python:3.9-slim" > Dockerfile
echo "WORKDIR /app" >> Dockerfile
echo "COPY requirements.txt ." >> Dockerfile
echo "RUN pip install --no-cache-dir -r requirements.txt" >> Dockerfile
echo "COPY app.py ." >> Dockerfile
echo "CMD [\"python\", \"app.py\"]" >> Dockerfile

# Construir la imagen Docker
docker build -t nasa-app .

docker stop samplerunning 2>/dev/null || true
docker rm samplerunning 2>/dev/null || true

docker run --name samplerunning -e API_KEY_PROYECTO=$API_KEY_PROYECTO nasa-app
