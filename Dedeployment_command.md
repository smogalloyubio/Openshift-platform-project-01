# OpenShift Deployment Guide

This folder contains OpenShift manifests and a quick deployment guide for the app in this repository.
The example is configured for the `ubiowororuki-dev` namespace and deploys the `myapp-dev` application.

## What is included

- `deployment.yaml` - Deployment manifest for the Flask app container
- `service.yaml` - Service exposing container port `5000`
- `route.yaml` - Route that makes the app accessible from outside the cluster

## Prerequisites

- Access to an OpenShift cluster
- `oc` CLI installed and available on your PATH
- Login credentials or token for your OpenShift cluster
- Optional: access to the OpenShift web console if you prefer UI interaction

## How to use

### 1. Log in to OpenShift

```

oc login https://<OPENSHIFT_API_URL> --token=<YOUR_TOKEN>
```

If your cluster uses self-signed TLS, add:

```
oc login https://<OPENSHIFT_API_URL> --token=<YOUR_TOKEN> --insecure-skip-tls-verify=true
```

### 2. Verify your project/namespace

```
oc project ubiowororuki-dev
```

If the namespace does not exist, create it:

```
oc new-project ubiowororuki-dev
```

### 3. Apply the OpenShift manifests

```
oc apply -f Openshift/deployment.yaml
oc apply -f Openshift/service.yaml
oc apply -f Openshift/route.yaml
```

This creates:
- Deployment: `myapp-dev`
- Service: `myapp-dev`
- Route: `myapp-dev`

### 4. Check deployment status

```
oc get pods -n ubiowororuki-dev
oc get svc -n ubiowororuki-dev
oc get route -n ubiowororuki-dev
```

### 5. Find the app URL

```
oc get route myapp-dev -n ubiowororuki-dev -o jsonpath='{.spec.host}'
```

Then open the returned host URL in your browser.

## Notes on the deployment

- The app container expects port `5000` and the manifests expose that port.
- The `deployment.yaml` references the internal OpenShift image registry image:
  `image-registry.openshift-image-registry.svc:5000/ubiowororuki-dev/myapp-dev:latest`
- To deploy from a custom image, update the `image` field in `deployment.yaml`.

## GitHub Actions CI/CD

This repository also includes a GitHub Actions workflow in `.github/workflows/openshift_deploy.yaml`.
That workflow builds and scans a Docker image, pushes it to Quay, and triggers an OpenShift build.

### Required secrets for GitHub Actions

- `QUAY_USERNAME`
- `QUAY_TOKEN`
- `OPENSHIFT_SERVER`
- `OPENSHIFT_TOKEN`
- `WEBHOOK_SECRET`

## When to use this guide

Use this file when you want to deploy the app manually with `oc apply`. For automated deployment, rely on the workflow and the configured OpenShift build webhook.

---

If you want, I can also add a brief bullet list of the OpenShift manifest contents or a clean summary for recruiters here.