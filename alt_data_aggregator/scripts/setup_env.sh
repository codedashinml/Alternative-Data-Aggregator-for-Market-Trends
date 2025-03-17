#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir -p data/raw data/processed data/outputs logs/ingestion_logs logs/processing_logs logs/ml_logs