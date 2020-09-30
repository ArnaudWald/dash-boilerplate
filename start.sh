#! /usr/bin/env sh
set -e

# Start Gunicorn
exec gunicorn flask_scheduler:server -b :8050 -w 4 --capture-output --error-logfile "-" --enable-stdio-inheritance --preload
