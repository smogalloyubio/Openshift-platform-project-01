

# 🚀 OpenShift Platform Automation

A full-stack DevOps automation platform that simplifies application deployment, management, and monitoring on OpenShift using **FastAPI**, **Docker**, **GitHub Actions**, and **OpenShift APIs**.

---

## Project Overview
Managing applications on Kubernetes and OpenShift often requires developers to interact directly with the `oc` CLI, write complex YAML manifests, and manually execute deployment commands. These repetitive tasks can slow software delivery, introduce configuration errors, and increase the dependency on DevOps engineers for routine operations.

The **OpenShift Platform Automation** project was built to simplify these workflows by providing an intuitive web-based platform backed by a FastAPI automation engine. Instead of manually executing cluster commands, users can perform common OpenShift operations through a graphical dashboard or REST API.
The platform integrates with **GitHub Actions** to automate Continuous Integration and Continuous Deployment (CI/CD), builds and manages Docker images, deploys workloads to OpenShift, and provides operational capabilities such as deployment management, application scaling, route creation, log retrieval, and configuration management.
This project demonstrates how modern DevOps practices, including Infrastructure Automation, Containerization, CI/CD, Security Scanning, and Platform Engineering, can be combined into a single solution that improves developer productivity and operational efficiency.

---
##  Project Objectives
The primary objectives of this project are to:
* Simplify application deployment to OpenShift.
* Reduce manual interaction with the OpenShift CLI.
* Automate repetitive DevOps tasks.
* Provide a user-friendly dashboard for managing applications.
* Demonstrate modern CI/CD best practices.
* Improve deployment consistency and reliability.
* Showcase a practical Platform Engineering solution built with open-source technologies.

---
# 💼 Business Problem

Many organizations adopting Kubernetes and OpenShift encounter several operational challenges during application deployment and management.
Some of the most common problems include:
* Manual deployment using lengthy `oc` commands.
* Complex Kubernetes and OpenShift YAML configurations.
* Slow release cycles caused by manual deployment approvals.
* Heavy reliance on DevOps engineers for simple operational tasks.
* Limited visibility into application health and deployment status.
* Lack of centralized tools for scaling, log retrieval, and route management.
* Inconsistent deployment processes across development teams.
These challenges reduce developer productivity, increase deployment risk, and slow the delivery of new features.

---

# ✅ Solution

OpenShift Platform Automation addresses these challenges by providing a centralized automation platform that combines application deployment, operational management, and CI/CD into a single interface.

Using this platform, developers can:

* Deploy applications with a single click.
* Trigger automated CI/CD pipelines.
* Build and push Docker images automatically.
* Scale applications without using the command line.
* View deployment logs directly from the dashboard.
* Manage OpenShift Routes and Services.
* Deploy ConfigMaps and Secrets.
* Monitor deployment status through a centralized interface.
This significantly reduces operational complexity while enabling faster and more reliable software delivery.

---

# ⭐ Key Features

The platform includes the following capabilities:

### 🚀 Deployment Automation

* One-click application deployment
* Automated OpenShift BuildConfig execution
* YAML deployment automation
* Route creation
* Service deployment
* Deployment rollout management

### ⚙️ OpenShift Operations

* Scale application replicas
* Retrieve deployment logs
* View deployment status
* Expose applications using Routes
* Deploy ConfigMaps
* Deploy Secrets
* Trigger OpenShift Builds

### 🔄 CI/CD Automation

* Automated GitHub Actions workflow
* Docker image build
* Container image publishing
* Automatic deployment trigger
* Manual workflow dispatch support

### 🐳 Containerization

* Dockerized FastAPI application
* Lightweight Python runtime
* Production-ready Dockerfile
* Image publishing to Quay.io

### 🔒 Security

* Trivy vulnerability scanning
* GitHub Secrets integration
* Secure OpenShift authentication
* Secure container image publishing

### 🧪 Testing

* Automated unit testing with Pytest
* CI validation
* Docker build verification

### 🖥️ Dashboard

The web dashboard provides an easy-to-use interface for:

* Deploying applications
* Viewing deployment status
* Scaling replicas
* Monitoring logs
* Managing Routes
* Executing OpenShift automation tasks

---

# 🏗️ High-Level Architecture
![Architectural Diagram](https://github.com/smogalloyubio/Openshift-platform-project-01/blob/main/ArchitectureDiagram/openshift%20cluster.jpg)
---

##  Business Value
Modern DevOps teams face challenges:

- Manual OpenShift deployments slow down delivery.  
- YAML configuration errors cause downtime.  
- Developers depend on DevOps engineers for every change.  
- No unified dashboard for builds, logs, and scaling.

This platform solves those problems by offering:

- **One‑click deployments**  
- **Automated CI/CD pipelines**  
- **Centralized configuration management**  
- **Reduced DevOps workload**  
- **Faster onboarding for new developers**

---

## Problem & Solution

| Problem | Solution |
|----------|-----------|
| Manual OpenShift commands | FastAPI automates all cluster operations |
| YAML complexity | Auto‑generated manifests |
| Slow deployments | GitHub Actions pipeline triggers builds automatically |
| No visibility | Dashboard shows logs, routes, and replica status |

---
![VDEIO  DEMOSTRATION LINK BELOW]
https://drive.google.com/file/d/1zCL85bGMT5S07hPlfglaOFpvnUr9YoVX/view?usp=sharing
---

## Architecture Overview

### System Components
- **FastAPI Backend** — automation engine (`fastapi_app/main.py`)
- **Web UI** — dashboard for deployment and scaling
- **OpenShift Cluster** — executes deployments, services, routes
- **GitHub Actions** — CI/CD pipeline for build and deploy
- **Quay.io Registry** — stores container images

---

## Architecture Diagrams

###  High‑Level Architecture
![High-Level Architecture](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Copilot_20260525_095756.png)

###  System Architecture
![System Architecture](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Copilot_20260525_095822.png)


---

## Tools Used

| Tool | Purpose |
|------|----------|
| **FastAPI** | Backend automation API |
| **OpenShift CLI (`oc`)** | Executes cluster commands |
| **Docker / Quay.io** | Container image management |
| **GitHub Actions** | CI/CD automation |
| **Python 3.12** | Core language |
| **HTML + JS** | Dashboard interface |

---

## Installation

```bash
git clone https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project.git
cd Openshift-Platform-Fastapi-Project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### High‑Level Flow


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
install virtual env
python3 -m venv venv
source venv/bin/activate
uvicorn fastapi_app.main:app --reload 
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
![GITHUB ACTION PIPELINE](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.19.22.png)

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

![OPENSHIFT DEPLOYMENT](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.18.51.png)

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
![DASHBOARD UI](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.18.07.png)

For OpenShift deployment, configure the required secrets, then use the GitHub Actions workflow or deploy the provided manifests with `oc apply -f Openshift/ * -n ubiowororuki-dev`.

---
![DASHBOARD UI](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.19.07.png)
