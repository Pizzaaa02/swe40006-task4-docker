# Task 4.2 - containerise a Python Flask hello-world web server.
# The python:3.12-slim base image supplies the Python run-time (sub-task:
# "Add Python install run-time").
FROM python:3.12-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY app.py .

# The Flask server listens on 5000 inside the container.
EXPOSE 5000

CMD ["python", "app.py"]
