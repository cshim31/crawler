import crawl
import numpy as np
import parse
import time
from threading import Thread

class Package:
    def __init__(self, courseTerm='', courseSubjectKey='', courseSubjectValue='', courseNum=''):
        self.courseTerm = courseTerm
        self.courseSubjectKey = courseSubjectKey
        self.courseSubjectValue = courseSubjectValue
        self.courseNum = courseNum

    # getters & setters
    def getTerm(self):
        return self.courseTerm

    def getSubjectKey(self):
        return self.courseSubjectKey

    def getSubjectValue(self):
        return self.courseSubjectValue

    def getNum(self):
        return self.courseNum

packageList = []
courseList = []
running = True

def task(courseTerm):
    threadList = []

    threadList.append(Thread(target=subTask, args=()))

    for thread in threadList:
        thread.start()
        print(thread.name, " executed")

    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        for courseNum in courseNums:
            packageList.append(Package(courseTerm, courseSubjectKey, courseSubjectValue, courseNum))
            print('Pakcage : %s %s' %(courseSubjectKey, courseNum))

    while packageList:
        time.sleep(5)


    running = False

    # write parsed data to file output in excel
    print("Writing csv...")
    parse.writeCSV(courseList, courseTerm)
    print("Writing json...")
    parse.writeJson(courseList, courseTerm)

def subTask(): 
    while running:
        if packageList:
            package = packageList.pop(0)
            print('fetcing %s:%s, %s' % (package.getSubjectKey(), package.getNum(), package.getTerm()))
            schedule = crawl.fetchSchedule(package.getTerm(), package.getSubjectKey(), package.getSubjectValue(), package.getNum())
            if schedule:
                courseList.extend(schedule)