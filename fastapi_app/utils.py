import subprocess

def run_oc(cmd: list[str]):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": " ".join(cmd),
        "stdout": result.stdout,
        "stderr": result.stderr,
        "success": result.returncode == 0
    }
