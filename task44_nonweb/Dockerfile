# Task 4.4 - containerise the non-web command-line application.
# No ports are exposed because this is not a web app - it runs to completion
# and prints its results to the console.
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

# Runs the CLI program when the container starts.
ENTRYPOINT ["python", "app.py"]
