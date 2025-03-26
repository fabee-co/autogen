import subprocess
import sys
import os

def main():
    cmd = ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "app:app"]
    subprocess.call(cmd)

if __name__ == "__main__":
    main()