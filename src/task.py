import crawl
import numpy as np

def task(courseTerm):
    courseLists = [[]]
    
    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)

    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        
        for courseNum in courseNums:
            courseList = crawl.fetchSchedule(courseTerm, courseSubjectValue, courseSubjectKey, courseNum)
            if courseList is not None:
                courseLists.append(courseList)

    
    # write parsed data to file output in excel
    print("Writing data...")
    crawl.writeToText(courseLists, courseTerm)
    crawl.writeToJson(courseLists, courseTerm)
    #crawl.writeToCsv(courseList, term)
    crawl.integrateToText(courseLists, courseTerm)
    crawl.convertToCsv(courseTerm)
    crawl.convertToCsv('course')
