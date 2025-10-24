# Gunicorn configuration file for DiracAI Django Backend

import multiprocessing

# Server socket
bind = "127.0.0.1:8001"  # Using port 8001 to avoid conflicts
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '/home/sammy/myprojectdir/logs/gunicorn_access.log'
errorlog = '/home/sammy/myprojectdir/logs/gunicorn_error.log'
loglevel = 'info'

# Process naming
proc_name = 'diracai_backend'

# Server mechanics
daemon = False
pidfile = '/home/sammy/myprojectdir/gunicorn.pid'
user = 'sammy'
group = 'sammy'
tmp_upload_dir = None

# SSL (if needed)
# keyfile = '/path/to/keyfile'
# certfile = '/path/to/certfile'


