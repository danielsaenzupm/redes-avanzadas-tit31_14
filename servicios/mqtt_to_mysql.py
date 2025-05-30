import mysql.connector
import paho.mqtt.client as mqtt
import json

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="admin123",  
    database="redes_avanzadas"
)

cursor = conexion.cursor()

# Callback al recibir mensaje MQTT
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        tipo = data.get("tipo")
        valor = data.get("valor")
        unidad = data.get("unidad", "") 

        sql = "INSERT INTO datos_sensor (tipo, valor, unidad) VALUES (%s, %s, %s)"
        cursor.execute(sql, (tipo, valor, unidad))
        conexion.commit()
        print(f"Dato insertado: {data}")
    except Exception as e:
        print(f"Error al insertar en MySQL: {e}")

# Conexión al broker MQTT local
cliente = mqtt.Client()
cliente.on_message = on_message

cliente.connect("localhost", 1883, 60)
cliente.subscribe("sensores/#")

cliente.loop_forever() 

CREATE TABLE datos_sensor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    valor FLOAT,
    unidad VARCHAR(10),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

