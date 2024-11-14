# Speech-to-Text Analysis Dashboard

## Overview
Real-time speech recognition and sentiment analysis web application built with Flask and Google's Speech Recognition API. Features an intuitive dashboard displaying transcription history, sentiment scores, and downloadable transcripts.
![Interface](https://github.com/miladnasiri/Speech-to-text-/blob/3333193a09e5647366bd3cd151c8c85d6a86ccd9/dashboard.png)
## Architecture & Methodology
- **Speech Recognition**: Google Speech-to-Text API via SpeechRecognition library
- **Sentiment Analysis**: NLTK VADER (Valence Aware Dictionary for Sentiment Reasoning)
- **Backend**: Flask RESTful API with modular design
- **Frontend**: Responsive UI with TailwindCSS and vanilla JavaScript
- **Data Storage**: File-based transcript storage with timestamp organization
- **Analysis Pipeline**:
 1. Audio Capture -> Speech Recognition
 2. Text Processing -> Sentiment Analysis
 3. Data Storage -> File System
 4. Real-time Updates -> WebUI

## Features
- Real-time speech-to-text conversion
- Sentiment analysis (Positive/Negative/Neutral scores)
- Transcript history with timestamps
- Downloadable transcripts
- Responsive dashboard UI
- Audio feedback and visual indicators

## Technology Stack
- Python 3.8+
- Flask 3.1.0
- NLTK 3.8.1
- SpeechRecognition 3.11.0
- PyAudio 0.2.14
- TailwindCSS
- Google Speech API

## Installation
```bash
git clone https://github.com/miladnasiri/Speech-to-text-.git
cd Speech-to-text-
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python src/app.py
```
## Project Structure
```bash
CopySpeech-to-Text/
├── src/
│   ├── app.py          # Flask application
│   ├── templates/      # HTML templates
│   └── static/         # CSS, JS assets
├── data/
│   └── transcripts/    # Stored transcripts
└── requirements.txt    # Dependencies
```
## API Endpoints

GET / : Dashboard interface
POST /recognize : Speech recognition endpoint
GET /transcripts/<filename> : Download endpoint

## Dependencies
```bash
CopyFlask==3.1.0
SpeechRecognition==3.11.0
pyaudio==0.2.14
nltk==3.8.1
pillow==11.0.0
pytest==8.3.3
```
## Features in Detail

1.Speech Recognition

- Real-time audio capture
- Google Speech API integration
- Error handling for unclear speech


Sentiment Analysis

- VADER sentiment scoring
- Compound score calculation
- Positive/Negative/Neutral breakdown


## Data Management

- Timestamp-based filing
- Downloadable transcripts
- Historical record keeping


## User Interface

- Real-time feedback
- Visual sentiment indicators
- Responsive design
- Download functionality




MIT License
Authors
Milad Nasiri

