import subprocess
import time

subprocess.Popen("python exchange_rate/main.py")

try:
    while True:
        time.sleep(3)
        subprocess.Popen("python app/example.py")
except KeyboardInterrupt:
    exit()