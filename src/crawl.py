import tools

def task(term):
    courseLists = [[]]
    # fetch course information for each course term
    
    courseIDs, subjects = tools.get_subjects(term)
    courseList = []
    for i in range(len(subjects)):
        nums = tools.get_courseNum(term, courseIDs[i])
        
        for num in nums:
            courseList = tools.get_course_info(term, subjects[i], courseIDs[i], num)
            if courseList is not None:
                courseLists.append(courseList)

    
    # write parsed data to file output in excel
    print("Writing to excel")
    for courseList in courseLists:
        tools.writeToText(courseList, term)
