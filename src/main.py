from time import gmtime, strftime, time, sleep
from threading import Thread

from log import *
from constant import config
import crawl
import task
import thread as th

threadList = []

def run():
    start_time = time()
    formatted_stime = gmtime()

    th.executeThreads(threadList)
    th.joinThreads(threadList)
    
    end_time = time()
    formatted_etime = gmtime()

    log_info(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_stime))
    log_info(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_etime))
    log_info(f"--- {end_time - start_time} seconds ---")

def generateThreads():
    # fetch number of semester as defined in constant.py
    terms = crawl.fetchCourseTerm(config.SEMESTER)


    for term in terms:
        threadList.append(Thread(target=task.task, args=(term,)))

def init():
    generateThreads()
    

def main():
    init()

    
if __name__ == "__main__":
    main()
    run()