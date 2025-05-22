import requests
import random
import time

URL = "http://localhost:5000/ingesta"

while True:
    dato = {
        "sensor_id": "sede1-hum-001",
        "tipo": "humedad",
        "valor": round(random.uniform(40.0, 60.0), 2)
    }
    try:
        r = requests.post(URL, json=dato)
        print("Enviado:", dato, "| Estado:", r.status_code)
    except Exception as e:
        print("❌ Error:", e)
    time.sleep(10)
