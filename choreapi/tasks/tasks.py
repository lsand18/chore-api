import schedule
import time
from datetime import datetime
from choreapi.models import Chore
# https://pypi.org/project/schedule/


# this does not appear to work right now.  When tasks.py was in views, it blocked all other requests.
def reset_chores():
    current_time = datetime.now()
    if current_time.hour == 0 and current_time.minute == 0:
        print("chores reset")
        allChores = Chore.objects.all()
        for chore in allChores:
            chore.complete = False
            chore.user = None
            chore.save()
        

schedule.every().hour.do(reset_chores)


while True:
    schedule.run_pending()
    time.sleep(1)

# UTC time - works
# def reset_chores():
#     print("Chores reset")

# schedule.every().day.at("16:49").do(reset_chores)


# while True:
#     schedule.run_pending()
#     time.sleep(1)