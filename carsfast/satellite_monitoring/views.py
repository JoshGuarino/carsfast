import datetime
import requests
from django.http import JsonResponse, HttpResponse
from satellite_monitoring.utility import max_altitude, min_altidude, avg_altitude, determine_status
from satellite_monitoring.models import Satellites, Stats


def index(request):
    return HttpResponse('Hello World!')


def stats(request):
    five_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    records = Stats.objects.filter(last_updated__range=(five_min_ago, datetime.datetime.now()))
    return JsonResponse({
        'max_altitude': max_altitude(records), 
        'min_altitude': min_altidude(records), 
        'avg_altitude': avg_altitude(records)
    })


def health(request):
    satellite = Satellites.objects.get(pk=1)
    return JsonResponse({'message': satellite.status})


def update(request):
    response = requests.get('https://api.cfast.dev/satellite/')
    data = response.json()
    satellite = Satellites.objects.get(pk=1)
    one_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)
    records = Stats.objects.filter(last_updated__range=(one_min_ago, datetime.datetime.now()))
    Stats(
        satellite=satellite,
        altitude=data['altitude'],
        last_updated=data['last_updated'],
    ).save()
    satellite.status = determine_status(records)
    satellite.save()
    return JsonResponse({'message': 'successfully updated satellite data'})