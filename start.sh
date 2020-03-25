#!/bin/bash
cd /home/pi/Greenist_backend;
source flask/bin/activate; 
pip install -r requirements.txt; 
env FLASK_APP=app.py python -m flask run --host 0.0.0.0;
cd -;