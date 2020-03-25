#!/bin/bash
cd /home/pi/Greenist_backend;
env FLASK_APP=app.py python3 -m flask run --host 0.0.0.0;
cd -;