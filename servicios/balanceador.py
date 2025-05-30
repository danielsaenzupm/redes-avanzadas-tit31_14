from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICIOS = ['http://localhost:5000', 'http://localhost:5001']
contador = 0

@app.route('/balanceador', methods=['POST'])
def balancear():
    global contador
    servicio = SERVICIOS[contador % len(SERVICIOS)]
    contador += 1
    try:
        res = requests.post(f"{servicio}/sensor", json=request.json)
        return res.text, res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5003)
