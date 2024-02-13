
import schedule
import time

from tool.search_job import *
import utils.log as log 

def main():
    job()
    
    schedule.every().interval(3600).do(job)
    

    while True:
        schedule.run_pending()
        time.sleep(1)


def job():
    log.success(f"実行開始")
    search_jobs()


if __name__ == "__main__":
    main()