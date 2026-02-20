# Voice Obfuscation API

This API accepts customer call recordings and applies transformations
that preserve speech clarity while reducing the risk of voice cloning
or speaker embedding reuse.

## Features

- Upload WAV or MP3
- Output processed WAV
- File size validation
- Duration validation
- Structured logging
- Docker ready

## Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload

## Docker

docker build -t voice-api .
docker run -p 8000:8000 voice-api

## Endpoints

GET /health
POST /obfuscate (form-data: file)
