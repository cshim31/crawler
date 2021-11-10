import crawl

def task(term):
    courseLists = [[]]
    # fetch course information for each course term
    
    courseIDs, subjects = crawl.get_subjects(term)
    courseList = []
    for i in range(len(subjects)):
        nums = crawl.get_courseNum(term, courseIDs[i])
        
        for num in nums:
            courseList = crawl.get_course_info(term, subjects[i], courseIDs[i], num)
            if courseList is not None:
                courseLists.append(courseList)

    
    # write parsed data to file output in excel
    print("Writing data...")
    crawl.writeToText(courseLists, term)
    crawl.writeToJson(courseLists, term)
    #crawl.writeToCsv(courseList, term)
    crawl.integrateToText(courseLists, term)
    crawl.convertToCsv(term)
    crawl.convertToCsv('course')
