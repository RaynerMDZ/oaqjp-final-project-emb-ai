import requests, json

def emotion_detector(text_to_analyze):
    base_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if text_to_analyze is None:
        return None

    text_to_analyze = text_to_analyze.strip()

    request_body = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(base_url, headers=headers, json=request_body)

    data = json.loads(response.text)

    predictions = (data or {}).get("emotionPredictions") or []
    if not predictions or not isinstance(predictions[0], dict):
        return None

    emotion = predictions[0].get("emotion") or {}
    if not isinstance(emotion, dict):
        return None

    anger_score = float(emotion.get("anger", 0.0))
    disgust_score = float(emotion.get("disgust", 0.0))
    fear_score = float(emotion.get("fear", 0.0))
    joy_score = float(emotion.get("joy", 0.0))
    sadness_score = float(emotion.get("sadness", 0.0))

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(scores, key=scores.get) if scores else None

    if data and response.status_code == 200:
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion,
        }
    elif response.status_code == 400:
        return "Invalid text! Please try again!"
    else:
        return f"Error: {response.status_code} - {response.text}"
    return None
