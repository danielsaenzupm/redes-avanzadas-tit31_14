import requests
import random
import time

URL = "http://localhost:5000/ingesta"

while True:
    dato = {
        "sensor_id": "sede1-co2-001",
        "tipo": "co2",
        "valor": round(random.uniform(300, 600), 2)
    }
    try:
        r = requests.post(URL, json=dato)
        print("Enviado:", dato, "| Estado:", r.status_code)
    except Exception as e:
        print("❌ Error:", e)
    time.sleep(10)
