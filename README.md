# Model Deployment Demonstration

## Project Overview

This project demonstrates the deployment of a pre-trained model from the [Hugging Face Model Hub](https://huggingface.co/models) to process inference requests within a Dockerized environment. The architecture includes Flask as the application server, NGINX for handling multiple parallel requests, and Gunicorn as the WSGI HTTP Server. A Streamlit application provides a user interface to interact with the model's inference endpoint.

## Why this Model?

The chosen model from the Hugging Face Model Hub demonstrates the capabilities of transfer learning and the power of pre-trained models in reducing the need for extensive computational resources during training. We focus on a model that exemplifies versatility and robustness in natural language processing tasks, showcasing the practical deployment for AI-based solutions.

## Components

### Docker Container

The Docker container encapsulates the Flask server, NGINX, Gunicorn, and the Streamlit application, ensuring a consistent and isolated environment for deployment. The configuration allows for easy scaling and management in cloud platforms.

- **Dockerfile**: Defines the steps to set up the Python environment, install dependencies, and configure the services needed for the application.

### Flask Server

`flask_server.py` handles the routing and processing of incoming HTTP POST requests for model inference, serving as the backbone of the application.

### NGINX

Configured to manage multiple incoming requests efficiently, ensuring optimal load distribution and enhanced performance.

- **nginx.conf**: Configuration file that sets up NGINX as a reverse proxy to direct requests to Gunicorn.

### Gunicorn

Used for serving the Flask application, allowing for concurrent handling of multiple requests.

- **startup.sh**: Script to start NGINX, Gunicorn, and the Streamlit application, ensuring all components are running simultaneously.

### Streamlit Application

Provides a user-friendly interface for sending requests to the deployed model and visualizing the responses.

- **streamlit_app.py**: The Streamlit application code.

### Requirements

Lists all Python dependencies required for the project, ensuring all necessary libraries are installed.

- **requirements.txt**: Contains Flask, transformers, torch, streamlit, requests, gunicorn.

## Setup and Deployment

1. Build the Docker container:
   ```bash
   docker build -t model-deployment .
   2. Run the container:
   ```bash
   docker run -p 80:80 -p 8501:8501 model-deployment

## Demonstrating the Inference

A notebook (not provided here) should be used to demonstrate how to send POST requests to the container endpoint and receive responses, highlighting the end-to-end functionality.

## Sentiment Analysis Interface

### Interface Overview

- **URL**: [Sentiment Analysis Interface](http://48.216.158.146/)
- **Functionality**: Users can enter any text into the input field and press the "Analisar Sentimento" button. The system then processes the text using a pre-trained model from the Hugging Face Model Hub and returns the sentiment as either POSITIVE or NEGATIVE along with a confidence score.

### Implementation Details

- **Deployment**: The interface is hosted on Azure Container Instances, ensuring scalable and efficient handling of requests.
- **Technology Stack**:
  - **Frontend**: Streamlit — for creating a user-friendly web interface.
  - **Backend**: Flask — serves the inference requests and communicates with the model.
  - **Model**: Utilizes a pre-trained NLP model for sentiment analysis, capable of understanding nuances in the text.

### Usage Example

The screenshot below illustrates a sample interaction with the interface:

![Sentiment Analysis Interface Example](http://example.com/screenshot.png) *Note: Replace with an actual link to the screenshot if available online.*

Users can access the interface through the provided URL, type their text, and submit it for analysis. The result is displayed below the input field, showing the sentiment and the confidence level of the prediction.


