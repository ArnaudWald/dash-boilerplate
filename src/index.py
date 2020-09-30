# -*- coding: utf-8 -*-
"""Run the main app without the cron-job scheduler."""
from main_app import app
import main_layout

app.layout = main_layout.layout

if __name__ == '__main__':
    # Use this when deploying locally
    # app.run_server(debug=True)
    # Use this when deploying on Docker
    app.run_server(host='0.0.0.0', port=8050, debug=True)
