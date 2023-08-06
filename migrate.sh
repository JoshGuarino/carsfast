#!/usr/bin/env bash
python carsfast/manage.py migrate
python carsfast/manage.py makemigrations satellite_monitoring