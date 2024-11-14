from flask import Flask, render_template, jsonify, request, send_from_directory
import speech_recognition as sr
from datetime import datetime
from pathlib import Path
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)
recognizer = sr.Recognizer()
microphone = sr.Microphone()

TRANSCRIPT_DIR = Path("data/transcripts")
TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

@app.route('/')
def home():
   transcripts = []
   for file in TRANSCRIPT_DIR.glob("*.txt"):
       with open(file, 'r') as f:
           text = f.read()
           sentiment = sia.polarity_scores(text)
           transcripts.append({
               'filename': file.name,
               'text': text,
               'timestamp': datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
               'sentiment': sentiment
           })
   return render_template('index.html', transcripts=sorted(transcripts, key=lambda x: x['timestamp'], reverse=True))

@app.route('/recognize', methods=['POST'])
def recognize_speech():
   with microphone as source:
       recognizer.adjust_for_ambient_noise(source, duration=0.5)
       try:
           audio = recognizer.listen(source, timeout=5)
           text = recognizer.recognize_google(audio)
           
           timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
           file_path = TRANSCRIPT_DIR / f"transcript_{timestamp}.txt"
           with open(file_path, "w") as f:
               f.write(text)
           
           sentiment = sia.polarity_scores(text)
           
           return jsonify({
               'success': True,
               'text': text,
               'sentiment': sentiment,
               'timestamp': timestamp
           })
       except sr.UnknownValueError:
           return jsonify({'success': False, 'error': 'Could not understand audio'})
       except sr.RequestError as e:
           return jsonify({'success': False, 'error': str(e)})

@app.route('/transcripts/<path:filename>')
def download_transcript(filename):
   return send_from_directory(TRANSCRIPT_DIR, filename)

if __name__ == '__main__':
   app.run(debug=True, port=5001)
