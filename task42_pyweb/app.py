"""Task 4.2 - A simple Python (Flask) 'hello-world' web server.

Demonstrates: deploying a Python app in Docker, with the Python run-time
supplied by the python:3.12-slim base image, serving a hello-world web page.
"""
import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "<h1>Hello World</h1>"
        "<p>This is a Python Flask web server running inside a Docker container.</p>"
        f"<p>Container hostname: <b>{socket.gethostname()}</b></p>"
    )


if __name__ == "__main__":
    # 0.0.0.0 so the server is reachable from outside the container.
    app.run(host="0.0.0.0", port=5000)
