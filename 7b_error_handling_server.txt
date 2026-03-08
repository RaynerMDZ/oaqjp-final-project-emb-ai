"""Flask application exposing an emotion detection endpoint."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector/<text>', methods=['GET'])
def detect_emotion(text=None):
    """Return formatted emotion scores and dominant emotion for input text."""
    try:
        if text is None:
            text = request.args.get("textToAnalyze", "")

        text = text.strip() if isinstance(text, str) else ""
        if not text:
            return "Invalid text! Please try again!"

        emotion_dict = emotion_detector(text)
        if isinstance(emotion_dict, str):
            return emotion_dict

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
    except Exception:
        return "Unable to process the request at this time. Please try again."

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')

@app.errorhandler(404)
def not_found(_error):
    """Return a plain-text not found message."""
    return "Endpoint not found.", 404

@app.errorhandler(405)
def method_not_allowed(_error):
    """Return a plain-text method not allowed message."""
    return "Method not allowed.", 405

@app.errorhandler(500)
def internal_server_error(_error):
    """Return a plain-text internal server error message."""
    return "Unable to process the request at this time. Please try again.", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
