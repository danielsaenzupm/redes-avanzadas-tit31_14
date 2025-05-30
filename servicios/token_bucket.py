import time
from flask import Flask, request, jsonify

app = Flask(__name__)

bucket_capacity = 10
tokens = bucket_capacity
refill_rate = 1
last_checked = time.time()

def refill():
    global tokens, last_checked
    now = time.time()
    tokens_to_add = int((now - last_checked) * refill_rate)
    tokens = min(bucket_capacity, tokens + tokens_to_add)
    last_checked = now

@app.route('/sensor', methods=['POST'])
def recibir_dato():
    refill()
    global tokens
    if tokens > 0:
        tokens -= 1
        print("Dato recibido:", request.json)
        return jsonify({"status": "aceptado"})
    else:
        return jsonify({"status": "rechazado, sin tokens"}), 429

if __name__ == '__main__':
    app.run(port=5001)
