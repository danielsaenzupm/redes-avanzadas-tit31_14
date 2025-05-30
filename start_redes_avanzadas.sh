
#!/bin/bash

# Crear nueva sesión de tmux
tmux new-session -d -s redes_avanzadas

# Servicios
tmux rename-window -t redes_avanzadas:0 'servicios'
tmux send-keys -t redes_avanzadas 'python3 servicios/token_bucket.py' C-m
tmux split-window -h -t redes_avanzadas
tmux send-keys -t redes_avanzadas 'python3 servicios/filtro_ips.py' C-m
tmux split-window -v -t redes_avanzadas
tmux send-keys -t redes_avanzadas 'python3 servicios/balanceador.py' C-m
tmux split-window -v -t redes_avanzadas
tmux send-keys -t redes_avanzadas 'python3 servicios/servicio_rest.py' C-m
tmux split-window -v -t redes_avanzadas
tmux send-keys -t redes_avanzadas 'python3 servicios/wadl_service.py' C-m

# Nueva ventana para middleware
tmux new-window -t redes_avanzadas -n 'middleware'
tmux send-keys -t redes_avanzadas:1 'python3 middleware/middleware_http_to_mqtt.py' C-m

# Nueva ventana para sensores
tmux new-window -t redes_avanzadas -n 'sensores'
tmux send-keys -t redes_avanzadas:2 'python3 sensores/temperatura.py' C-m
tmux split-window -h -t redes_avanzadas:2
tmux send-keys -t redes_avanzadas:2 'python3 sensores/humedad.py' C-m
tmux split-window -v -t redes_avanzadas:2
tmux send-keys -t redes_avanzadas:2 'python3 sensores/co2.py' C-m
tmux split-window -v -t redes_avanzadas:2
tmux send-keys -t redes_avanzadas:2 'python3 sensores/covs.py' C-m

# Atachar la sesión
tmux attach-session -t redes_avanzadas
