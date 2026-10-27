# iot-rag-assistant

# IoT RAG Assistant

A learning project that answers questions using sample IoT sensor readings
and equipment documentation. It returns the data summary and the document
sources used.

## Features

- Reads fictional temperature and humidity data from CSV
- Answers basic questions about sensor readings
- Retrieves relevant documentation passages
- Returns source references
- Handles questions when evidence is missing

## Run locally

1. Create a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start the API with `uvicorn app.main:app --reload`.
4. Open `/docs` on the local server to try the API.

## Tests

Run `pytest`.

## Data and limitations

The included readings and documents are fictional examples. This project
is an educational prototype, not a safety or equipment-control system.
It does not control real devices.

## Inspiration

Inspired by Seeed-Projects/Smart-Home-RAG-Assistant:
https://github.com/Seeed-Projects/Smart-Home-RAG-Assistant

This repository is an independent learning implementation. Any reused code
or assets must be identified and used according to their applicable license.
