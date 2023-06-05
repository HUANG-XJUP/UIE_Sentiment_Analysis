from flask import Flask, request, jsonify
from backend.models import Models

app = Flask(__name__)


@app.route('/analysis', methods=['POST'])
def analysis():
    if request.method == "POST":
        data = request.json['input_text']
        task = request.json['task']
        CLA = Models(data)
        if task == 'sentiment_analysis':
            result = CLA.sentiment_analysis()
        if task == 'entity_recognition':
            result = CLA.entity_recognition()
        if task == 'opinion_extraction':
            result = CLA.opinion_extraction()
    else:
        result = 'it is not post request'
    return jsonify(result)


if __name__ == '__main__':
    app.run()

