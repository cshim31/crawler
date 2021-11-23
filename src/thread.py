from threading import Thread

def executeThreads(threadList):
    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

def joinThreads(threadList):
    for thread in threadList:
        thread.join()
        #print(thread.name, " executed")

def checkThreadStatus(threadList):
    bisAlive = False
    for thread_ in threadList:
        bisAlvie = bisAlive or thread_.is_alive()
    return bisAlive

