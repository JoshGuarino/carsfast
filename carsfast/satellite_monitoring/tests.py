import datetime
from django.test import TestCase
from satellite_monitoring.models import Stats, Satellites
from satellite_monitoring.utility import max_altitude, min_altidude, avg_altitude, determine_status



class HealthTestCase(TestCase):
    def setUp(self):
        self.satellite = Satellites(status='Altitude is A-OK')
        self.data = [
            Stats(satellite=self.satellite, altitude=170, last_updated=datetime.datetime.now()),
            Stats(satellite=self.satellite, altitude=160, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=10)),
            Stats(satellite=self.satellite, altitude=170, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=20)),
            Stats(satellite=self.satellite, altitude=160, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=30)),
            Stats(satellite=self.satellite, altitude=170, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=40)),
            Stats(satellite=self.satellite, altitude=160, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=50))
        ]
        
    def test_max_altitude(self):
        max = max_altitude(self.data)
        self.assertEqual(max, 170)

    def test_min_altitude(self):
        min = min_altidude(self.data)
        self.assertEqual(min, 160)

    def test_avg_altitude(self):
        avg =  avg_altitude(self.data)
        self.assertEqual(avg, 165)

    def test_warning_status(self):
        data = self.data
        data.append(Stats(satellite=self.satellite, altitude=155, last_updated=datetime.datetime.now() - datetime.timedelta(seconds=60)))
        warning_status = determine_status(data)
        self.assertEqual(warning_status, 'WARNING: RAPID ORBITAL DECAY IMMINENT')

    def test_resume_status(self):
        data = self.data
        data.insert(0, Stats(satellite=self.satellite, altitude=155, last_updated=datetime.datetime.now() + datetime.timedelta(seconds=60)))
        resume_status = determine_status(data)
        self.assertEqual(resume_status, 'Sustained Low Earth Orbit Resumed')

    def test_ok_status(self):
        data = self.data
        ok_status = determine_status(data)
        self.assertEqual(ok_status, 'Altitude is A-OK')