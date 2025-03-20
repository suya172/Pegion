from flask import Flask, request, jsonify
import requests
import Config
import json

app = Flask(__name__)

DISCORD_WEBHOOK_URL = Config.WEBHOOK_URL
LINE_CHANNEL_ACCESS_TOKEN = Config.LINE_CHANNEL_ACCESS_TOKEN

@app.route("/")
def index():
    return "I'm alive!"

@app.route("/webhook", methods=["POST"])
def line_webhook():
    # todo: 署名の検証
    data = request.json
    print(json.dumps(data, indent=2))
    if "events" in data:
        for event in data["events"]:
            if event["type"] == "message" and "text" in event["message"]:
                message = event["message"]["text"]
                send_to_discord(message)
    return jsonify({"status": "ok"})

def send_to_discord(message):
    payload = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    app.run(port=5000)
