from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotion-detector/<text>', methods=['GET'])
def detect_emotion(text=None):
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

if __name__ == '__main__':
    app.run(port=5000)
