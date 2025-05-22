import requests
import random
import time

URL = "http://localhost:5000/ingesta"

while True:
    dato = {
        "sensor_id": "sede1-covs-001",
        "tipo": "covs",
        "valor": round(random.uniform(0.1, 0.8), 2)
    }
    try:
        r = requests.post(URL, json=dato)
        print("Enviado:", dato, "| Estado:", r.status_code)
    except Exception as e:
        print("❌ Error:", e)
    time.sleep(10)
