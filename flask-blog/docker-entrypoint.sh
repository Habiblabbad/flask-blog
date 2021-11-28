#!/bin/sh

flask db upgrade
python /app/flask-blog/app.py