# Configuración Gunicorn
import multiprocessing

# Número de workers
workers = multiprocessing.cpu_count() * 2 + 1

# Dirección y puerto
bind = "0.0.0.0:5000"

# Configuración de workers
worker_class = 'eventlet'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Configuración adicional
preload_app = True
max_requests = 1000
max_requests_jitter = 50