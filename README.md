# Model Deployment Demonstration

🤗 This project showcases the deployment of the `bert-base-uncased` model from the Hugging Face Model Hub for processing inference requests within a Dockerized environment. It utilizes Flask, NGINX, and Gunicorn to manage multiple parallel requests, with a Streamlit application providing an interactive user interface.

## Why this Model?

The `bert-base-uncased` model was chosen for its efficiency in natural language understanding, requiring minimal fine-tuning to deliver high performance in sentiment analysis tasks. Its pre-training on a large and diverse text corpus makes it well-suited for quick deployment in real-world applications.

## Sentiment Analysis Interface

### Interface Overview

- **URL**: [Access the Sentiment Analysis Interface](http://52.146.57.234/)
- **URL**: [Access the Sentiment Analysis Notebook](https://colab.research.google.com/drive/14o5zHaN4gnqzoZzTR1ZoX9fd3c-ycQFV?usp=sharing)
- **Functionality**: Users input text and receive an analysis indicating whether the sentiment is POSITIVE or NEGATIVE, along with a confidence score.

#### Example Usage

**Input**:  
"I love this product! It works wonderfully."

**Output**:  
Sentiment: `POSITIVE`  
Confidence: `0.94`

This succinct example demonstrates the interface's capability to analyze and reflect the sentiment of user input effectively.

Below is a sample interaction with the interface:

![Sentiment Analysis Interface Example](https://github.com/onchainlabs1/lemay/blob/main/Sentiment-analysis-interface.png) 

### Implementation Details

- **Deployment**: Hosted on Azure Container Instances for scalable and efficient request handling.
- **Technology Stack**:
  - **Frontend**: Streamlit — provides a user-friendly interface.
  - **Backend**: Flask — manages inference requests.
  - **Model**: Employs a pre-trained NLP model for nuanced sentiment analysis.


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

1. **Build the Docker container:**
   Use the following command to build the Docker container:
   ```bash
   docker build -t model-deployment .
   
Run the container:
Use the following command to run the container, mapping necessary ports:

docker run -p 80:80 -p 8501:8501 model-deployment


## AI Architecture Elevator Pitch
[AI Architecture Elevator Pitch Video](https://www.youtube.com/watch?v=ZW-hsYpi36A)

## General Knowledge Video Demonstration
[General Knowledge Video Demonstration](https://www.youtube.com/watch?v=N98e7LbzxkI)

## Exploratory Data Analysis Demonstration 
[Exploratory Data Analysis on GitHub](https://github.com/onchainlabs1/exploratory/)


🚀 Thanks for checking this out! 😊 Excited to see what we can create together — let's make something awesome! 🚀



