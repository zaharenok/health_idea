import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

@app.route("/webhook", methods=["POST"])
def webhook():
    received_secret = request.headers.get("X-Webhook-Secret")
    if received_secret != WEBHOOK_SECRET:
        return jsonify({"error": "Invalid webhook secret"}), 403
    data = request.json
    # Пример использования ключей
    response = {
        "message": "Webhook received!",
        "api_key_used": API_KEY,
        "secret_key_used": SECRET_KEY,
        "received_data": data
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
