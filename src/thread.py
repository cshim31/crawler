from threading import Thread

def executeThreads(threadList):
    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

    for thread in threadList:
        thread.join()
        print(thread.name, " executed")

def checkThreadStatus(threadList):
    thread = threadList[-1]
    if thread.is_alive(): threadList.pop() 

