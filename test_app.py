import subprocess

result = subprocess.run(["python", "app.py"], capture_output=True, text=True)

assert result.returncode == 0
assert "Cloud CI Pipeline Running" in result.stdout
