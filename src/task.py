import crawl
import numpy as np
import parse

def task(courseTerm):
    courseLists = []
    
    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)

    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        for courseNum in courseNums:
            print('fetcing %s:%s' % (courseSubjectKey, courseNum))
            courseList = crawl.fetchSchedule(courseTerm, courseSubjectValue, courseSubjectKey, courseNum)
            if courseList:
                courseLists.extend(courseList)

    
    # write parsed data to file output in excel
    print("Writing data...")
    parse.writeCSV(courseLists, courseTerm)
    parse.writeJson(courseLists, courseTerm)
