# redes-avanzadas-tit31_14
# redes-avanzadas-tit31_14
# Proyecto de Redes Avanzadas - Equipo TIT31_14

Este proyecto simula un sistema distribuido de sensores conectados a servicios mediante HTTP y MQTT, con visualización en Grafana.

## Estructura del Proyecto
TIT31_14/
├── middleware/
│ └── middleware_http_to_mqtt.py
├── sensores/
│ └── temperatura.py
│ └── humedad.py
│ └── co2.py
│ └── covs.py
├── servicios/
│ └── mqtt_to_mysql.py
│ └── balanceador.py
│ └── token_bucket.py
│ └── filtro_ips.py
│ └── servicio_rest.py
│ └── wadl_service.py
├── grafana/
│ └── monitor_sensores_dashboard.json
├── README.md
└── requirements.txt

## Requisitos

- Python 3.x
- MySQL
- Grafana

## Instalación

```bash
pip install -r requirements.txt

## Ejecucion  
python servicios/token_bucket.py
python servicios/filtro_ips.py
python servicios/balanceador.py
python servicios/servicio_rest.py
python servicios/wadl_service.py

## Instalación

Grafana debe estar configurado con la base de datos redes_avanzadas, y el dashboard se importa desde grafana/monitor_sensores_dashboard.json.

