#!/bin/bash
source ../.cronusVE/bin/activate
python ../website/backend_cronus/manage.py makemigrations
python ../website/backend_cronus/manage.py migrate