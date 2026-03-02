from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():

    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']

    response_text = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
