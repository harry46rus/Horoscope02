# import schedule
from schedule import *
import schedule
import time

def job():
    print("I'm working...")

# Run job every 3 second/minute/hour/day/week,
# Starting 3 second/minute/hour/day/week from now
# schedule.every(10).seconds.do(job)

# job()

# for i in range(100):
#      time.sleep(3)
#      # main()
#      job()

while True:
    time.sleep(3)
    # main()
    job()