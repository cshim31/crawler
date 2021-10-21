from time import gmtime, strftime, time, sleep
from threading import Thread

import tools
import constant
import crawl

threadList = []

def executeThreads():
    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

def run():
    start_time = time()
    formatted_stime = gmtime()

    executeThreads()
    
    # run until thread completes
    running = True
    while running:
        sleep(10) # check every 10s
        # reset system variables
        running = True
        isAlive = True
        if threadList:
            isAlive = threadList[0].is_alive()            
        for thread in threadList:
            isAlive = not (isAlive or thread.is_alive())

        running = running != isAlive # xor

    # time report
    end_time = time()
    formatted_etime = gmtime()

    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_stime))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_etime))
    print("--- %s seconds ---" % (end_time - start_time))

def generateThreads():
    # fetch number of semester as defined in constant.py
    terms = tools.get_terms(constant.SEMESTER)

    for term in terms:
        threadList.append(Thread(target=crawl.task, args=(term,)))

def init():
    generateThreads()
    

def main():
    init()


    
if __name__ == "__main__":
    main()
    run()