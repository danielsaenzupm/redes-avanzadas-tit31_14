import requests
import random
import time

URL = "http://localhost:5000/ingesta"

while True:
    dato = {
        "sensor_id": "sede1-temp-001",
        "tipo": "temperatura",
        "valor": round(random.uniform(20.0, 30.0), 2)
    }
    try:
        r = requests.post(URL, json=dato)
        print("Enviado:", dato, "| Estado:", r.status_code)
    except Exception as e:
        print("❌ Error:", e)
    time.sleep(10)
