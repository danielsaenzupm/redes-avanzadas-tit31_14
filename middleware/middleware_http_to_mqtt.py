from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Conexión a MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="redes_avanzadas"
)
cursor = conn.cursor()

@app.route('/ingesta', methods=['POST'])
def recibir_datos():
    data = request.get_json()

    sensor_id = data.get("sensor_id")
    tipo = data.get("tipo")
    valor = data.get("valor")

    if not all([sensor_id, tipo, valor]):
        return {'estado': 'ERROR', 'mensaje': 'Datos incompletos'}, 400

    query = "INSERT INTO datos_sensor (sensor_id, tipo, valor) VALUES (%s, %s, %s)"
    cursor.execute(query, (sensor_id, tipo, valor))
    conn.commit()

    return {'estado': 'OK'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
