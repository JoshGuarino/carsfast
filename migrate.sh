#!/usr/bin/env bash
python3 carsfast/manage.py migrate
python3 carsfast/manage.py makemigrations satellite_monitoring