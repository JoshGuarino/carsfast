import requests
import time

while True:
    time.sleep(10)
    requests.get('http://localhost:8000/satellite/update')