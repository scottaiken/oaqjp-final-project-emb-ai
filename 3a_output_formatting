import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    req_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = req_json)
    res_dict = {}
    if response.status_code >= 200 and response.status_code <= 299:
        res_json = json.loads(response.text)
        if "emotionPredictions" in res_json and len(res_json["emotionPredictions"]) > 0:
            prediction0 = res_json["emotionPredictions"][0]
            if "emotion" in prediction0:
                emotions = prediction0["emotion"]
                # print(f"{emo}")
                if isinstance(emotions, dict):
                    dominant_emo = ""
                    dominant_score = 0.0
                    for k, v in emotions.items():
                        res_dict[k] = v
                        if v > dominant_score:
                            dominant_score = v
                            dominant_emo = k
                    res_dict['dominant_emotion'] = dominant_emo
                # print(f"{res_dict}")
    return res_dict
    