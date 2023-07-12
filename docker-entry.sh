exec gunicorn --timeout=180 -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 skill:app
