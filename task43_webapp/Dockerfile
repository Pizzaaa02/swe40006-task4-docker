# Task 4.3 - containerise the newly-developed 'Container Dashboard' web app.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# The app listens on 8080 inside the container.
EXPOSE 8080

CMD ["python", "app.py"]
