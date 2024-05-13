FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install nginx, gunicorn, and other dependencies
RUN apt-get update && apt-get install -y nginx && pip install gunicorn

# Install Streamlit
RUN pip install streamlit

# Copy the dependencies file to the working directory
COPY requirements.txt .
# Install any Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Copy nginx configuration (you need to provide this file in your project directory)
COPY nginx.conf /etc/nginx/sites-available/default

# Expose port 80 to the outside world
EXPOSE 80

# Make startup script executable
COPY startup.sh /usr/local/bin/startup.sh
RUN chmod +x /usr/local/bin/startup.sh

# Start nginx, gunicorn and streamlit using a startup script
CMD ["/usr/local/bin/startup.sh"]
