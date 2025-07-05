# Servidor Flask para ESP32

Este proyecto es un servidor básico en Flask que recibe datos enviados desde un dispositivo como el ESP32 mediante una solicitud HTTP POST.

## Cómo funciona

- El servidor expone una ruta `/datos` que acepta solicitudes POST con datos en formato JSON.
- Los datos recibidos se imprimen en la consola y se responde con un mensaje de confirmación.

## Archivos

- `app.py`: Código principal del servidor Flask.
- `requirements.txt`: Lista de dependencias necesarias.
- `README.md`: Descripción del proyecto.

## Ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
