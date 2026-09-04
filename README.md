# Voice Obfuscation API

A FastAPI service that transforms customer call recordings to preserve speech intelligibility while reducing the risk of voice cloning or speaker-embedding reuse — built around a pretrained speech pipeline (HuBERT for content, ECAPA-TDNN for speaker embeddings, and a HiFi-GAN/FreeVC-based vocoder for resynthesis).

## What it does

1. Accepts an uploaded call recording (WAV or MP3).
2. Extracts content and speaker-embedding representations from the pretrained pipeline.
3. Perturbs the speaker embedding enough to break voice-cloning/re-identification while keeping the linguistic content intact.
4. Resynthesizes and returns a processed WAV file.
5. Validates file size and duration up front, and logs every step with structured logging.

## Architecture

```
app/
├── main.py           # FastAPI app entry point
├── config.py          # settings
├── routers/            # obfuscation endpoint(s)
├── services/            # the obfuscation pipeline (HuBERT / ECAPA-TDNN / vocoder)
├── models/              # pretrained model loading/wrappers
└── utils/                # logging, validation helpers
tests/                     # test suite
Dockerfile                  # container build
```

## Setup

**Requirements:** Python 3.10+, CUDA-capable GPU recommended (the pipeline runs on CPU too, just slower).

```bash
git clone https://github.com/AbhishekRK41/voice-obfuscation-api-final.git
cd voice-obfuscation-api-final
pip install -r requirements.txt
```

## Run locally

```bash
uvicorn app.main:app --reload
```

## Run with Docker

```bash
docker build -t voice-api .
docker run -p 8000:8000 voice-api
```

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Health check |
| `POST` | `/obfuscate` | Upload a file (`form-data`, field `file`) → returns the obfuscated WAV |

## Housekeeping before you show this to recruiters

- `temp/` currently has committed sample output `.wav` files and `app/__pycache__/` is tracked in git. Add a `.gitignore` (`temp/*`, `__pycache__/`, `*.pyc`) and remove them from version control so the repo only contains source.

## License

Add a license if you plan to share this publicly as a portfolio.
