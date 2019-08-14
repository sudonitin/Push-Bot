import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=17, minute=35)
def scheduled_job():
    os.system("run.sh")

sched.start()
