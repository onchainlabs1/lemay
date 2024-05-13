# flask_server.py
import os
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    prediction = model(text)
    return jsonify(prediction)

if __name__ == '__main__':
    # Alterando a porta para 8000
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

