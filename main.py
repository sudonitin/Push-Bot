import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

#the line below executes the scheduled_job function everyday at 5:35pm
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=19, minute=55)
def scheduled_job():
    os.system("run.sh")
    print("hello")

sched.start()
