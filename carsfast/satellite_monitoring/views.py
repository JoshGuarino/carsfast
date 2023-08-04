
from django.http import JsonResponse, HttpResponse
from satellite_monitoring.models import Satellites, Stats

def index(request):
    return HttpResponse('Hello World!')

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