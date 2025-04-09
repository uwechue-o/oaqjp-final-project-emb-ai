import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)
    response_json = response.json()

    # Extracting the emotion scores
    emotion_scores = response_json["emotionPredictions"][0]["emotion"]

    # Finding the emotion with the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    highest_score = emotion_scores[dominant_emotion]

    print(f"Dominant Emotion: {dominant_emotion} (Score: {highest_score})") 

    for m in response_json["emotionPredictions"][0]["emotionMentions"]:
        mention_emotions = m["emotion"]
        mention_dominant_emotion = max(mention_emotions, key=mention_emotions.get)
        mention_emotions["dominant_emotion"] = mention_dominant_emotion

    print(json.dumps(response_json, indent=2))



    # try:
    #    formatted_response = response.json()
    #    print("Formatted Response:", json.dumps(formatted_response, indent=2))
    #    return formatted_response
    #except json.JSONDecodeError as e:
    #    print("Failed to decode JSON:", e)
    #    print("Raw response:", response.text)
    #    return None
