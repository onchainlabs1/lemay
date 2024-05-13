# Model Deployment Demonstration

## Project Overview

This project showcases the deployment of the `bert-base-uncased` model from the [Hugging Face Model Hub](https://huggingface.co/models) for processing inference requests within a Dockerized environment. It utilizes Flask, NGINX, and Gunicorn to manage multiple parallel requests, with a Streamlit application providing an interactive user interface.

## Why this Model?

The `bert-base-uncased` model was chosen for its efficiency in natural language understanding, requiring minimal fine-tuning to deliver high performance in sentiment analysis tasks. Its pre-training on a large and diverse text corpus makes it well-suited for quick deployment in real-world applications.

## Sentiment Analysis Interface

### Interface Overview

- **URL**: [Access the Sentiment Analysis Interface](http://48.216.158.146/)
- **Functionality**: Users input text, and the system analyzes sentiment, returning results as either POSITIVE or NEGATIVE with a confidence score.

### Implementation Details

- **Deployment**: Hosted on Azure Container Instances for scalable and efficient request handling.
- **Technology Stack**:
  - **Frontend**: Streamlit — provides a user-friendly interface.
  - **Backend**: Flask — manages inference requests.
  - **Model**: Employs a pre-trained NLP model for nuanced sentiment analysis.

### Usage Example

Below is a sample interaction with the interface:
![Sentiment Analysis Interface Example](http://example.com/screenshot.png) *Note: Replace with an actual link to the screenshot if available online.*

Users can visit the provided URL, submit their text, and view the analysis results displayed beneath the input field.

## Components

### Docker Container

The Docker setup encapsulates the Flask server, NGINX, Gunicorn, and Streamlit, ensuring a consistent and isolated environment suitable for scaling and cloud deployment.

- **Dockerfile**: Configures the Python environment and installs necessary dependencies.

### Flask Server

`flask_server.py` processes incoming HTTP POST requests for model inference, acting as the primary application server.

### NGINX

Manages incoming requests effectively, set up as a reverse proxy in `nginx.conf` to direct traffic to Gunicorn for enhanced performance.

### Gunicorn

Serves the Flask application, allowing for the handling of multiple concurrent requests.

- **startup.sh**: Initializes NGINX, Gunicorn, and the Streamlit app, ensuring all components are active.

### Streamlit Application

Facilitates interactions with the model through a web-based interface detailed in `streamlit_app.py`.

### Requirements

- **requirements.txt**: Includes Flask, transformers, torch, streamlit, requests, gunicorn, ensuring all dependencies are met.

## Setup and Deployment

1. Build the Docker container:
   ```bash
   docker build -t model-deployment .

2.Run the container:
  ```bash
docker run -p 80:80 -p 8501:8501 model-deployment

AI ARCHITECTURE ELEVATOR PITCH:
https://www.youtube.com/watch?v=ZW-hsYpi36A

GENERAL KNOWLEDGE VIDEO DEMONSTRATION:
https://www.youtube.com/watch?v=N98e7LbzxkI

EXPLORATORY DATA ANALYSIS DEMONSTRATION:
[https://github.com/onchainlabs1/lemay](https://github.com/onchainlabs1/exploratory/)
