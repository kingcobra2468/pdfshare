#!/bin/bash

python3 -m pdfshare.pdfbsd.pdfbsd &
gunicorn -c pdfshare/app/gunicorn_config.py pdfshare.app.wsgi:app