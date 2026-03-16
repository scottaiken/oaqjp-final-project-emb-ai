from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final project")

@app.route('/emotionDetector')
def emotion_detector_endpoint():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if isinstance(response, dict):
        if 'anger' in response and 'disgust' in response and \
           'fear' in response and 'joy' in response and \
           'sadness' in response and 'dominant_emotion' in response:
           return ("For the given statement, the system response is "
                   "'anger': "   + str(response['anger'])   + ", "
                   "'disgust': " + str(response['disgust']) + ", "
                   "'fear': "    + str(response['fear'])    + ", "
                   "'joy': "     + str(response['joy'])     + ", and "
                   "'sadness': " + str(response['sadness']) + ". "
                   "The dominant emotion is "
                   "<b>" + response['dominant_emotion'] + "</b>.")
    pass

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
