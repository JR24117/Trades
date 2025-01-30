import schedule
import time
from bot import run_bot

schedule.every().hour.do(run_bot)

while True:
    schedule.run_pending()
    time.sleep(1)
