import time
from django.http import JsonResponse, HttpResponse
import requests

def index(request):
    return HttpResponse('Hello, world.')


def stats(request):
    return JsonResponse({
        'max_altitude': 22, 
        'min_altitude': 0, 
        'avg_altitude': 11
        })


def health(request):
    return JsonResponse({
        'status': '<insert status here>'
        })

def update_satellite_data():
    # response = requests.get('https://satellite.carsfast.workers.dev/')
    # data = response.json()
    print(22)

while True:
    update_satellite_data()
    time.sleep(10)