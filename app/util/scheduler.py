import schedule
import time
import utils


def job():
    utils.get_states_poll()
    utils.get_overall_poll()


schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
