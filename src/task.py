import crawl
import numpy as np
import time
from threading import Thread

from constant import constant
import crawl
from data import package
import parse

packageList = []
courseList = []
running = True

def task(courseTerm):
    global running

    threadList = [Thread(target=subTask, args=()) for i in range(constant.THREAD_COUNT)]

    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        for courseNum in courseNums:
            package = Package(courseTerm, courseSubjectKey, courseSubjectValue, courseNum)
            packageList.append(package)
            #print(package)

    while packageList:
        time.sleep(10)


    print("Terminating threads...")
    running = False

    # write parsed data to file output in excel
    print("Writing csv...")
    parse.writeCSV(courseList, courseTerm)
    print("Writing json...")
    parse.writeJson(courseList, courseTerm)

def subTask(): 
    while running:
        if not packageList: continue

        package = packageList.pop(0)

        #print('fetcing %s:%s, %s' % (package.getSubjectKey(), package.getNum(), package.getTerm()))
        schedule = crawl.fetchSchedule(package.getTerm(), package.getSubjectKey(), package.getSubjectValue(), package.getNum())
        if schedule:
            courseList.extend(schedule)