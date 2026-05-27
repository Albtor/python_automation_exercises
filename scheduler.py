import schedule
import time

def job():
    print("This task runs every 7 minutes")
    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
