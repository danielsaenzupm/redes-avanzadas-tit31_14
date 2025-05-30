from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/datos', methods=['GET'])
def obtener_datos():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin123',
        database='redes_avanzadas'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datos_sensor ORDER BY fecha DESC LIMIT 10")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(port=5004)
