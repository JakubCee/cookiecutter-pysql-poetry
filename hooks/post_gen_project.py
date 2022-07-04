import subprocess


subprocess.check_call(["poetry init"])
subprocess.check_call(["poetry install"])
subprocess.check_call(["git init"])
subprocess.check_call(["pre-commit install"])
