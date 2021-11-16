from time import gmtime, strftime, time, sleep
from threading import Thread

from constant import constant
import crawl
import task
import thread

threadList = []

def run():
    start_time = time()
    formatted_stime = gmtime()

    thread.executeThreads(threadList)
    
    # time report
    end_time = time()
    formatted_etime = gmtime()

    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_stime))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_etime))
    print("--- %s seconds ---" % (end_time - start_time))

def generateThreads():
    # fetch number of semester as defined in constant.py
    terms = crawl.fetchCourseTerm(constant.SEMESTER)

    for term in terms:
        threadList.append(Thread(target=task.task, args=(term,)))

def init():
    generateThreads()
    

def main():
    init()

    
if __name__ == "__main__":
    main()
    run()