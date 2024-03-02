from flask import Flask, request, jsonify
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

url = "http://localhost:11436/api/generate"


@app.route("/chat", methods=["POST"])
def home():
    request_body = request.get_json()
    if request_body:
        print("Retrieving Ollama results...")
        llm_result = requests.post(url, json=request_body)
        return jsonify(llm_result.json()['response'])
    else:
        return {"response", "error"}

if __name__ == "__main__":
    app.run(host="0.0.0.0")
