import crawl
import numpy as np
import time
from threading import Thread

from constant import constant
import crawl
from data.package import CoursePackage
import parse
import thread

packageList = []
courseList = []
seatList = []
running = True

# main thread task
def task(courseTerm):
    global running

    threadList = [Thread(target=subTaskOne, args=()) for i in range(constant.THREAD_COUNT)]

    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        for courseNum in courseNums:
            package = CoursePackage(courseTerm, courseSubjectKey, courseSubjectValue, courseNum)
            packageList.append(package)
            #print(package)

    
    while threadList:
        thread.checkThreadStatus(threadList)
        sleep(10)


    print("Terminating threads...")
    running = False

    # write parsed data to file output in excel
    print("Writing csv...")
    parse.writeCSV(courseList, courseTerm)
    parse.writeCSV(seatList, courseTerm + 'seat')
    print("Writing json...")
    parse.writeJson(courseList, courseTerm)
    parse.writeJson(seatList, courseTerm + 'seat')

# subthread task
def subTaskOne(): 
    while running:
        if not packageList: 
            continue

        package = packageList.pop(0)

        schedule = crawl.fetchCourseSchedule(package.getTerm(), package.getSubjectKey(), package.getSubjectValue(), package.getNum())

        if schedule: 
            #seats = [crawl.fetchCourseSeat(course.getTerm(), course.getCRN()) for course in schedule]
            seats = []
            for course in schedule:
                print(course.getArea())
                seats.append(crawl.fetchCourseSeat(course.getTerm(), course.getCRN()))

            courseList.extend(schedule)
            seatList.extend(seats)
        #print('fetcing %s:%s, %s' % (package.getSubjectKey(), package.getNum(), package.getTerm()))
            

