import subprocess

result = subprocess.run(["ip", "link", "show", "ethO"], capture_output=True, text=True)
print(result.stdout)