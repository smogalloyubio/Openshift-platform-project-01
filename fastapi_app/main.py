from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
from fastapi_app.utils import run_oc
import os 
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

NAMESPACE = "ubiowororuki-dev"
APP_NAME = "myapp-dev"


GH_TGH_TOKEN = os.getenv("GH_TGH_TOKEN")  
GITHUB_REPO = "smogalloyubio/Openshift-Platform-Fastapi-Project"
WORKFLOW_FILE = "openshift_deploy.yaml"  


@app.get("/debug-token")
def debug_token():
    return {"GH_TGH_TOKEN": GH_TGH_TOKEN}


@app.post("/start-github-actions")
def start_github_actions():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GH_TGH_TOKEN}"
    }

    data = { "ref": "main" }

    response = requests.post(url, json=data, headers=headers)

    return {
        "message": "GitHub Actions workflow triggered",
        "status": response.status_code,
        "response": response.text
    }

@app.get("/")
def dashboard():
    return FileResponse("statics/index.html")

@app.post("/deploy-yaml")
def deploy_yaml():
    return run_oc([
        "oc", "apply", "-f", "Openshift/",
        "-n", NAMESPACE
    ])

@app.post("/start-build")
def start_build():
    return run_oc([
        "oc", "start-build", APP_NAME,
        "--follow",
        "-n", NAMESPACE
    ])

@app.post("/get-route")
def get_route():
    return run_oc([
        "oc", "get", "route",
        "-n", NAMESPACE
    ])

@app.post("/expose-route")
def expose_route():
    return run_oc([
        "oc", "expose", "service", APP_NAME,
        "-n", NAMESPACE
    ])

class ScaleUpRequest(BaseModel):
    replicas: int = 4

@app.post("/scale-up")
def scale_up(req: ScaleUpRequest):
    return run_oc([
        "oc", "scale", "deployment", APP_NAME,
        f"--replicas={req.replicas}",
        "-n", NAMESPACE
    ])

class ScaleDownRequest(BaseModel):
    replicas: int = 1   

@app.post("/scale-down")
def scale_down(req: ScaleDownRequest):
    return run_oc([
        "oc", "scale", "deployment", APP_NAME,
        f"--replicas={req.replicas}",
        "-n", NAMESPACE
    ])


@app.post("/view-logs")
def view_logs():
    return run_oc([
        "oc", "logs", f"deployment/{APP_NAME}",
        "-n", NAMESPACE
    ])

class ImageWithConfigRequest(BaseModel):
    name: str
    image: str

    configmap_name: str
    config_key: str
    config_value: str
    config_mount_path: str

    secret_name: str
    secret_key: str
    secret_value: str
    secret_mount_path: str

    port: int = 8080
    replicas: int = 1


@app.post("/deploy-image-with-config")
def deploy_image_with_config(req: ImageWithConfigRequest):

    # 1. Create ConfigMap
    cm = run_oc([
        "oc", "create", "configmap", req.configmap_name,
        f"--from-literal={req.config_key}={req.config_value}",
        "-n", NAMESPACE
    ])


    secret = run_oc([
        "oc", "create", "secret", "generic", req.secret_name,
        f"--from-literal={req.secret_key}={req.secret_value}",
        "-n", NAMESPACE
    ])

    image = req.image.strip()
    deploy = run_oc([
        "oc", "new-app", req.image,
        "--name", req.name,
        "-n", NAMESPACE
    ])


    mount_cm = run_oc([
        "oc", "set", "volume", f"deployment/{req.name}",
        "--add",
        f"--name={req.configmap_name}-vol",
        f"--mount-path={req.config_mount_path}",
        "--configmap-name", req.configmap_name,
        "-n", NAMESPACE
    ])


    mount_secret = run_oc([
        "oc", "set", "volume", f"deployment/{req.name}",
        "--add",
        f"--name={req.secret_name}-vol",
        f"--mount-path={req.secret_mount_path}",
        "--secret-name", req.secret_name,
        "-n", NAMESPACE
    ])

 
    env = run_oc([
        "oc", "set", "env", f"deployment/{req.name}",
        f"--from=secret/{req.secret_name}",
        "-n", NAMESPACE
    ])

   
    svc = run_oc([
        "oc", "expose", "deployment", req.name,
        f"--port={req.port}",
        "-n", NAMESPACE
    ])


    route = run_oc([
        "oc", "create", "route", "edge", req.name,
        "--service", req.name,
        f"--port={req.port}",
        "--insecure-policy=Redirect",
        "-n", NAMESPACE
    ])


    scale = run_oc([
        "oc", "scale", f"deployment/{req.name}",
        f"--replicas={req.replicas}",
        "-n", NAMESPACE
    ])

    return {
        "configmap": cm,
        "secret": secret,
        "deployment": deploy,
        "mount_configmap": mount_cm,
        "mount_secret": mount_secret,
        "env": env,
        "service": svc,
        "route": route,
        "scale": scale
    }
