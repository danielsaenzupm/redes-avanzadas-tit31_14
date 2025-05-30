#!/bin/bash

# Detener todas las sesiones de tmux relacionadas con el proyecto
echo "Cerrando sesiones tmux del proyecto TIT31_14..."

tmux kill-session -t token_bucket 2>/dev/null
tmux kill-session -t filtro_ips 2>/dev/null
tmux kill-session -t balanceador 2>/dev/null
tmux kill-session -t servicio_rest 2>/dev/null
tmux kill-session -t wadl_service 2>/dev/null
tmux kill-session -t middleware 2>/dev/null
tmux kill-session -t mqtt_to_mysql 2>/dev/null
tmux kill-session -t sensor_temperatura 2>/dev/null
tmux kill-session -t sensor_humedad 2>/dev/null
tmux kill-session -t sensor_co2 2>/dev/null
tmux kill-session -t sensor_covs 2>/dev/null

echo "Todas las sesiones han sido cerradas."
