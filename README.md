# OpenShift Platform FastAPI Project

## Project Overview

This repository contains a simple Python web application with an OpenShift deployment pipeline. The app is a mock cryptocurrency dashboard built with Flask, and the project includes automation for building, scanning, pushing, and deploying the application to an OpenShift cluster.

The main application runs in `app.py` and exposes both HTML pages and JSON endpoints. There is also a FastAPI helper service in `fastapi_app/main.py` that can trigger OpenShift commands and GitHub Actions workflow dispatches.

## What is included

- `app.py` - Flask web app that serves a dashboard and several JSON API endpoints.
- `Dockerfile` - builds the application container using Python 3.12.
- `requirements.txt` - Python dependencies.
- `tests/test_app.py` - basic tests for the Flask application.
- `Openshift/` - OpenShift manifests for deploying the app.
- `.github/workflows/openshift_deploy.yaml` - GitHub Actions pipeline for test, scan, build, push, and deploy.

## How the app works

The Flask app in `app.py` provides:
- `/` - renders the UI from `templates/index.html`
- `/api/crypto` - mock crypto asset data
- `/api/crypto/<coin_id>/history` - generated 30-day price history
- `/api/stats` - mock market statistics
- `/health` - health check endpoint

The endpoints return JSON and are designed for demo or prototype usage rather than production data.

## Local setup and run

### Prerequisites

- Python 3.12
- `pip`
- `git`

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run locally

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

### Run tests

```bash
pytest tests/ -v
```

This verifies the main Flask routes and API endpoints.

## Container build and deployment

The project is containerized with `Dockerfile` and deployed to OpenShift.

### Docker image

- Base image: `python:3.12-slim`
- Installs dependencies from `requirements.txt`
- Copies the repository contents into `/app`
- Exposes port `5000`
- Starts the app with `python app.py`

### OpenShift manifests

The `Openshift/` folder contains:
- `deployment.yaml` - deployment for `myapp-dev` in `ubiowororuki-dev`
- `service.yaml` - service that exposes port `5000`
- `route.yaml` - OpenShift route to make the app reachable externally

The deployment is configured to use the image pushed to the OpenShift internal registry at:

`image-registry.openshift-image-registry.svc:5000/ubiowororuki-dev/myapp-dev:latest`

## GitHub Actions deployment pipeline

The workflow `.github/workflows/openshift_deploy.yaml` is the main CI/CD flow:

1. `test` - checkout, install Python, run `pytest`
2. `scan_docker` - scan the repository with Trivy
3. `build` - build the Docker image, scan it, and push to Quay
4. `deploy` - install `oc`, authenticate with OpenShift, and trigger the OpenShift build webhook

### Required secrets

The GitHub workflow relies on the following repository secrets:
- `QUAY_USERNAME`
- `QUAY_TOKEN`
- `OPENSHIFT_SERVER`
- `OPENSHIFT_TOKEN`
- `WEBHOOK_SECRET`

### Deployment flow

When a push is made to `main` or the workflow is manually dispatched, GitHub Actions will:
- run tests
- scan code and image security
- build and push the container image to Quay
- authenticate with OpenShift
- hit the OpenShift build webhook for `myapp-dev`

## OpenShift automation helper

The FastAPI app in `fastapi_app/main.py` provides optional automation endpoints for OpenShift operations, including:
- deploy YAMLs from `Openshift/*`
- start a build
- get or expose routes
- scale deployment replicas
- view deployment logs
- deploy a custom image with ConfigMaps and Secrets

This helper is useful for demonstration or custom deployment workflows, but the main app itself is `app.py`.


## Quick start summary

```bash
git clone https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project.git
cd Openshift-Platform-Fastapi-Project
pip install -r requirements.txt
python3 -m venv venv
source venv/bin/activate
```

For OpenShift deployment, configure the required secrets, then use the GitHub Actions workflow or deploy the provided manifests with `oc apply -f Openshift/ * -n ubiowororuki-dev`.

---
