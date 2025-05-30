from flask import Flask, request, jsonify

app = Flask(__name__)
IP_PERMITIDAS = ['127.0.0.1']

@app.route('/sensor', methods=['POST'])
def recibir_dato():
    ip = request.remote_addr
    if ip in IP_PERMITIDAS:
        print("Dato permitido de", ip, ":", request.json)
        return jsonify({"status": "aceptado"})
    else:
        return jsonify({"error": "IP no autorizada"}), 403

if __name__ == '__main__':
    app.run(port=5002)
