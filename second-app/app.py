import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def reverse_message():
    response = requests.get("http://first-app-service:5000")
    data = response.json()
    data["message"] = data["message"][::-1]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
