from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

from hundredseconds.accounts.models import User
from datetime import datetime

def execute_calls():
    now = datetime.now()
    users = User.objects.filter(calling_hour=now.hour, calling_minute=now.minute)
    # do something to call users with facebook data


sched.add_cron_job(execute_calls, minute='0-59')


while True:
    pass


