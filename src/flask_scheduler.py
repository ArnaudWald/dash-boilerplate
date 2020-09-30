# -*- coding: utf-8 -*-
"""Start workers."""
from apscheduler.triggers.cron import CronTrigger
from flask_apscheduler import APScheduler
import logging

from main_app import app
import main_layout


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


# ############################### #
# ## Job scheduling definition ## #
# ############################### #
class Config(object):
    """Job configuration."""

    JOBS = [
        # job-1 is run every 30 minutes
        {
            'id': 'job-1',
            'func': 'job1:job1',
            'trigger': CronTrigger.from_crontab("*/30 * * * *"),
            # 'jitter': 120,
        },
        # job2 is run every 6 hours and 15 minutes (00:15, 06:15, 12:15, 18:15)
        {
            'id': 'job-2',
            'func': 'job2:job2',
            'trigger': CronTrigger.from_crontab("15 */6 * * *"),
            # 'jitter': 120,
        }
    ]
    SCHEDULER_API_ENABLED = True


# Add scheduling to server
server = app.server
server.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(server)
scheduler.start()


# ####################### #
# ## Layout definition ## #
# ####################### #
app.layout = main_layout.layout

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
