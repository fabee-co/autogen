#!/bin/bash
cd /home/site/wwwroot

# Start the Uvicorn server
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app --bind=0.0.0.0:8000