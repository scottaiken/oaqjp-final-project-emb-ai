"""
Implements the backend connection for the Final project
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Implements the backend server transaction for emotion detection
    """
    url = ('https://sn-watson-emotion.labs.skills.network/'
            'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    req_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = req_json, timeout=10)
    res_dict = {}
    if response.status_code >= 200 and response.status_code <= 299:
        res_json = json.loads(response.text)
        if "emotionPredictions" in res_json and \
                len(res_json["emotionPredictions"]) > 0 and \
                "emotion" in res_json["emotionPredictions"][0]:
            emotions = res_json["emotionPredictions"][0]["emotion"]
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
    elif response.status_code == 400:
        res_dict['anger'] = None
        res_dict['fear'] = None
        res_dict['joy'] = None
        res_dict['sadness'] = None
        res_dict['disgust'] = None
        res_dict['dominant_emotion'] = None
    return res_dict
    