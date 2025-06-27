
from flask import Flask, request, jsonify

app = Flask(__name__)

# نموذج ذكاء صناعي بسيط يحلل المؤشرات ويعطي توصية
def analyze_signals(data):
    macd = data.get('macd', 0)
    rsi = data.get('rsi', 50)
    ema50 = data.get('ema50', 0)
    ema200 = data.get('ema200', 0)
    price = data.get('price', 0)

    if macd > 0 and rsi > 55 and ema50 > ema200:
        return "buy"
    elif macd < 0 and rsi < 45 and ema50 < ema200:
        return "sell"
    else:
        return "hold"

@app.route("/", methods=["GET"])
def index():
    return "Gold AI API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        signal = analyze_signals(data)
        return jsonify({"signal": signal})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
