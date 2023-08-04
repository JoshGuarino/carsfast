#!/usr/bin/env bash
python3 carsfast/manage.py runserver & python3 carsfast/satellite_monitoring/update_satellite_data.py && fg