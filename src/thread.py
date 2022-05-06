from threading import Thread
from log import *

def executeThreads(threadList):
    for thread in threadList:
        thread.start()
        log_debug(f"{thread.name} executed")

def joinThreads(threadList):
    for thread in threadList:
        thread.join()
        #log_debug(f"{thread.name} executed")

# return true if threads are not done
# return false if threads are done
def checkThreadDone(threadList):
    bisAlive = False
    for thread_ in threadList:
        bisAlvie = not (bisAlive or thread_.is_alive())
    return bisAlive

