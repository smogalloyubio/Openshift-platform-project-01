

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
![Architectural Diagram](https://github.com/smogalloyubio/Openshift-platform-project-01/blob/main/ArchitectureDiagram/_openshiftnewapp.jpg)
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

---

# 🛠️ Technology Stack

The platform leverages modern DevOps and cloud-native technologies to automate application deployment and management on OpenShift.

| Category             | Technologies          |
| -------------------- | --------------------- |
| Backend Framework    | FastAPI               |
| Programming Language | Python 3.12           |
| Frontend             | HTML, CSS, JavaScript |
| Containerization     | Docker                |
| Container Registry   | Quay.io               |
| CI/CD                | GitHub Actions        |
| Container Platform   | Red Hat OpenShift     |
| Kubernetes CLI       | OpenShift CLI (`oc`)  |
| Security Scanning    | Trivy                 |
| Testing              | Pytest                |
| Version Control      | Git & GitHub          |

---

# 📂 Project Structure

The repository is organized into logical components to separate application code, deployment manifests, automation workflows, and tests.

```text
Openshift-Platform-Fastapi-Project
│
├── fastapi_app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── templates/
│
├── static/
│
├── Kustomized/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── route.yaml
│   ├── configmap.yaml
│   └── secret.yaml
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── openshift_deploy.yaml
│
├── Dockerfile
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📁 Repository Overview

| Directory              | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **fastapi_app/**       | FastAPI backend containing API routes and OpenShift automation logic |
| **templates/**         | HTML templates used by the dashboard                                 |
| **static/**            | CSS, JavaScript, and static assets                                   |
| **Kustomized/**         | Kubernetes and OpenShift deployment manifests                        |
| **tests/**             | Automated test suite                                                 |
| **.github/workflows/** | GitHub Actions CI/CD workflows                                       |
| **Dockerfile**         | Docker image definition                                              |
| **requirements.txt**   | Python dependencies                                                  |
| **README.md**          | Project documentation                                                |

---

# 📋 Prerequisites
Before running this project, ensure the following tools are installed on your machine.

| Tool                 | Version                       |
| -------------------- | ----------------------------- |
| Python               | 3.12 or later                 |
| Git                  | Latest                        |
| Docker               | Latest                        |
| OpenShift CLI (`oc`) | Latest                        |
| GitHub Account       | Required                      |
| Quay.io Account      | Required for image publishing |
| OpenShift Cluster    | Required for deployment       |

---

# 🚀 Installation

## Step 1 — Clone the Repository

```bash
git clone https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project.git
```

Move into the project directory.

```bash
cd Openshift-Platform-Fastapi-Project
```

---

## Step 2 — Create a Virtual Environment

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

After installation, verify that all dependencies have been installed successfully.

```bash
pip list
```

---

# ⚙️ Configuration

The application requires access to an OpenShift cluster and a container registry.

These values can be configured using GitHub Secrets or environment variables.

Example:

```env
OPENSHIFT_SERVER=https://api.cluster.example.com:6443

OPENSHIFT_TOKEN=<your-openshift-token>

QUAY_USERNAME=<your-quay-username>

QUAY_PASSWORD=<your-quay-password>

WEBHOOK_SECRET=<build-webhook-secret>
```

---

# 🔐 GitHub Repository Secrets

To enable automated deployments through GitHub Actions, configure the following repository secrets.

| Secret             | Purpose                       |
| ------------------ | ----------------------------- |
| `OPENSHIFT_SERVER` | OpenShift API endpoint        |
| `OPENSHIFT_TOKEN`  | Authentication token          |
| `QUAY_USERNAME`    | Quay username                 |
| `QUAY_TOKEN`       | Quay access token             |
| `WEBHOOK_SECRET`   | OpenShift BuildConfig webhook |

These secrets are securely injected into the GitHub Actions workflow during execution.

---

# ▶️ Running the Application Locally

After installing all dependencies, start the FastAPI application.

```bash
uvicorn fastapi_app.main:app --reload
```

By default, the application will be available at:

```text
http://localhost:5000
```

Open your browser and navigate to the URL above to access the dashboard.

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running, open:

Swagger UI

```text
http://localhost:5000/docs
```

ReDoc

```text
http://localhost:5000/redoc
```

These pages provide an interactive interface for testing all available API endpoints.

---

# ⚙️ Environment Variables

The application supports the following environment variables.

| Variable           | Description                          |
| ------------------ | ------------------------------------ |
| `OPENSHIFT_SERVER` | OpenShift API Server                 |
| `OPENSHIFT_TOKEN`  | OpenShift Authentication Token       |
| `QUAY_USERNAME`    | Quay Registry Username               |
| `QUAY_PASSWORD`    | Quay Registry Password               |
| `WEBHOOK_SECRET`   | OpenShift BuildConfig Webhook Secret |

---

# ✅ Verifying the Installation

After starting the application, verify the installation by checking the following:

* The FastAPI server starts without errors.
* The dashboard is accessible in your browser.
* The Swagger documentation loads successfully.
* The application can communicate with the OpenShift cluster.
* Docker is installed and functioning correctly.
* The `oc` CLI is authenticated with your cluster.

If all the above checks pass, your environment is ready for deployment and automation.
---

## GitHub Actions deployment pipeline
![GITHUB ACTION PIPELINE](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.19.22.png)
---


![OPENSHIFT DEPLOYMENT](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.18.51.png)



---

# 🐳 Docker Containerization

To ensure consistency across development, testing, and production environments, the application is fully containerized using Docker.
Containerization eliminates the "it works on my machine" problem by packaging the application and all its dependencies into a portable container image that can run consistently across any environment.

## Dockerfile Overview

The Docker image is built using a lightweight Python base image and includes all required application dependencies.

### Build Process

1. Pull the Python 3.12 Slim base image.
2. Set the application working directory.
3. Copy the dependency file.
4. Install Python packages.
5. Copy the application source code.
6. Expose port **5000**.
7. Start the FastAPI application.

---

## Build the Docker Image

```bash
docker build -t openshift-platform:latest .
```
---

## Run the Docker Container

```bash
docker run -d \
-p 5000:5000 \
--name openshift-platform \
openshift-platform:latest
```

Open your browser:

```text
http://localhost:5000
```

---

## Verify the Container

Check running containers.

```bash
docker ps
```

View application logs.

```bash
docker logs openshift-platform
```

Stop the container.

```bash
docker stop openshift-platform
```

Remove the container.

```bash
docker rm openshift-platform
```

---

# ☸️ OpenShift Deployment

Once the Docker image has been built and pushed to the container registry, the application can be deployed to an OpenShift cluster.

The repository contains Kubernetes and OpenShift manifests that automate the deployment process.

---

## Deployment Resources

| Resource   | Purpose                              |
| ---------- | ------------------------------------ |
| Deployment | Creates and manages application Pods |
| Service    | Provides internal network access     |
| Route      | Exposes the application externally   |
| ConfigMap  | Stores application configuration     |
| Secret     | Stores sensitive credentials         |

---

## OpenShift Manifest Directory

```text
Openshift/

├── deployment.yaml
├── service.yaml
├── route.yaml
├── configmap.yaml
└── secret.yaml
```

---

## Deploy the Application

Apply all manifests.

```bash
oc apply -f Openshift/
```

Verify the deployment.

```bash
oc get pods

oc get svc

oc get routes
```

Describe the deployment.

```bash
oc describe deployment myapp-dev
```

---

## Scaling the Application

Scale the deployment to three replicas.

```bash
oc scale deployment myapp-dev \
--replicas=3
```

Verify the replica count.

```bash
oc get deployment
```

---

## Viewing Application Logs

Retrieve logs from the running Pods.

```bash
oc logs deployment/myapp-dev
```

Follow logs in real time.

```bash
oc logs deployment/myapp-dev -f
```

---

## Checking Application Health

Verify that the application is running correctly.

```bash
oc get all
```

Check application events.

```bash
oc get events
```

---

# ⚙️ GitHub Actions CI/CD Pipeline

The project includes a fully automated Continuous Integration and Continuous Deployment (CI/CD) pipeline built with GitHub Actions.

Every code change is automatically validated, scanned, built, and deployed without manual intervention.

This automation reduces deployment time, improves software quality, and ensures consistent releases.

---

## Pipeline Workflow

The workflow is located at:

```text
.github/workflows/openshift_deploy.yaml
```

---

## Pipeline Stages

### 1. Checkout Repository

Downloads the latest version of the source code.

---

### 2. Install Dependencies

Installs all required Python packages.

---

### 3. Run Automated Tests

Runs the Pytest test suite to validate the application.

```bash
pytest tests/ -v
```

---

### 4. Security Scan

The repository is scanned using **Trivy** to detect:

* Vulnerable packages
* Known CVEs
* Security misconfigurations
* Dependency vulnerabilities

---

### 5. Build Docker Image

Builds a new container image from the latest source code.

```bash
docker build -t openshift-platform .
```

---

### 6. Push Image to Quay

Authenticates with Quay.io and publishes the Docker image.

Example image:

```text
quay.io/your-repository/openshift-platform:latest
```

---

### 7. Authenticate with OpenShift

GitHub Actions securely authenticates using the repository secrets.

```text
OPENSHIFT_SERVER

OPENSHIFT_TOKEN
```

---

### 8. Trigger Deployment

The workflow triggers an OpenShift BuildConfig webhook to deploy the latest version of the application.

---

## GitHub Secrets

The workflow requires the following encrypted repository secrets.

| Secret           | Purpose              |
| ---------------- | -------------------- |
| OPENSHIFT_SERVER | OpenShift API URL    |
| OPENSHIFT_TOKEN  | Authentication Token |
| QUAY_USERNAME    | Quay Username        |
| QUAY_TOKEN       | Quay Access Token    |
| WEBHOOK_SECRET   | BuildConfig Webhook  |

---

# 🔄 End-to-End Deployment Workflow

The following diagram illustrates the complete deployment process.



# 🔐 Security

Security is integrated throughout the deployment pipeline.

## Implemented Security Controls

* GitHub encrypted secrets
* OpenShift authentication tokens
* Trivy vulnerability scanning
* Secure Docker image publishing
* Private container registry
* Automated security validation during CI

These controls help identify vulnerabilities early in the software delivery lifecycle and reduce the risk of deploying insecure container images.

---

# 🧪 Testing

The project includes automated testing to ensure application stability and deployment reliability.

## Run Tests

```bash
pytest tests/ -v
```

---

## Test Coverage

| Test Type               | Tool           |
| ----------------------- | -------------- |
| Unit Testing            | Pytest         |
| Docker Build Validation | Docker         |
| CI Validation           | GitHub Actions |
| Security Scanning       | Trivy          |

---

## Expected Test Results

A successful test run should verify:

* Application starts successfully.
* API endpoints respond correctly.
* Docker image builds successfully.
* No critical security vulnerabilities are detected.
* GitHub Actions workflow completes successfully.
* OpenShift deployment is triggered without errors.

---
![DASHBOARD UI](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.18.07.png)

For OpenShift deployment, configure the required secrets, then use the GitHub Actions workflow or deploy the provided manifests with `oc apply -f Openshift/ * -n ubiowororuki-dev`.

---
![DASHBOARD UI](https://github.com/smogalloyubio/Openshift-Platform-Fastapi-Project/blob/main/screenshoot/Screenshot%202026-05-25%20at%2009.19.07.png)
```
