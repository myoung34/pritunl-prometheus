#!/bin/sh
export PATH=$PATH:/usr/local/bin
export PYTHONPATH=/app
cd /app
#flask db init
#flask db migrate
#flask db upgrade
python /app/run.py
