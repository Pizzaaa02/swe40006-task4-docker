# SWE40006 – Task 4: Deploy Containers using Docker

**Student:** Adrian Chew Hon Bing (105556362)
**Unit:** SWE40006 Software Deployment and Evolution
**Level attempted:** High Distinction (sub-tasks 4.1 – 4.4)

This repository holds the source code and Dockerfiles for Deployment Activity 4.
It is provided as the publicly accessible location for the source, as required by
the assignment (the source files are **not** pasted into the report).

## Contents

| Sub-task | Folder | What it is |
|----------|--------|------------|
| 4.1 (Pass) | – | `docker run hello-world` (no custom source) |
| 4.2 (Credit) | [`task42_pyweb/`](task42_pyweb) | A Python **Flask hello-world web server** (port 5000) |
| 4.3 (Distinction) | [`task43_webapp/`](task43_webapp) | A **new web app** – "Container Dashboard" (port 8080), published to a public URL |
| 4.4 (HD) | [`task44_nonweb/`](task44_nonweb) | A **non-web** command-line app – "Prime & Pi Analyzer" |

## How to build and run

### 4.2 – Python hello-world web server
```bash
cd task42_pyweb
docker build -t task42-pyweb .
docker run -d --name c42 -p 5000:5000 task42-pyweb
# open http://localhost:5000
```

### 4.3 – Container Dashboard web app (the one published publicly)
```bash
cd task43_webapp
docker build -t task43-webapp .
docker run -d --name c43 -p 8080:8080 task43-webapp
# open http://localhost:8080  (API: /api/info, health: /health)
```

### 4.4 – Non-web CLI app
```bash
cd task44_nonweb
docker build -t task44-nonweb .
docker run --rm task44-nonweb --samples 500000 --limit 100
```

## Pulling to another Docker device (4.2)
Push the image to a registry (Docker Hub or a local registry) and pull it on
another device:
```bash
docker tag task42-pyweb <registry>/task42-pyweb
docker push <registry>/task42-pyweb
# on the other device:
docker pull <registry>/task42-pyweb
```

All applications use the `python:3.12-slim` base image to supply the Python
run-time inside the container.
