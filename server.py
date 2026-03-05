"""Flask application exposing an emotion detection endpoint."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector/<text>', methods=['GET'])
def detect_emotion(text=None):
    """Return formatted emotion scores and dominant emotion for input text."""
    if text is None:
        text = request.args.get("textToAnalyze", "")

    emotion_dict = emotion_detector(text)
    if not emotion_dict or emotion_dict.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {emotion_dict['anger']}, "
        f"'disgust': {emotion_dict['disgust']}, "
        f"'fear': {emotion_dict['fear']}, "
        f"'joy': {emotion_dict['joy']} and "
        f"'sadness': {emotion_dict['sadness']}. "
        f"The dominant emotion is {emotion_dict['dominant_emotion']}."
    )

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)
