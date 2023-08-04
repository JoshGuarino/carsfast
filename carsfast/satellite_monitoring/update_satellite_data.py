import requests
import time

while True:
    response = requests.get('https://api.cfast.dev/satellite/')
    data = response.json()
    # Stats(satellite=1, altitude=data.altitude, last_updated=data.last_updated)
    print(data)
    time.sleep(10)

