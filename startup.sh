#!/bin/bash

# Start Nginx
service nginx start

# Start Gunicorn to serve the Flask application
gunicorn --workers 4 --bind 0.0.0.0:8000 flask_server:app &

# Start Streamlit
streamlit run streamlit_app.py --server.port 8501
