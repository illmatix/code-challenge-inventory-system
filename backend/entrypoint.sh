#!/bin/bash
# Start Gunicorn server
exec gunicorn -b 0.0.0.0:5000 "app.routes:app"
