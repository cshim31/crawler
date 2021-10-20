import time
from time import gmtime, strftime

import tools
import constant

def main():
    start_time = time.time()
    formatted_stime = gmtime()

    # fetch number of semester as defined in constant.py
    terms = tools.get_terms(constant.DEFAULT)
    courseLists = [[]]
    # fetch course information for each course term
    for term in terms: 
        courseIDs, subjects = tools.get_subjects(term)
        courseList = []
        for i in range(len(subjects)):
            nums = tools.get_courseNum(term, courseIDs[i])
            
            for num in nums:
                courseList = tools.get_course_info(term, subjects[i], courseIDs[i], num)
                if courseList is not None:
                    courseLists.append(courseList)
                time.sleep(constant.DELAY)

    
        # write parsed data to file output in excel
        print("Writing to excel")
        for courseList in courseLists:
            tools.writeToText(courseList, term)

    # time taken report
    end_time = time.time()
    formatted_etime = gmtime()

    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_stime))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_etime))
    print("--- %s seconds ---" % (end_time - start_time))
if __name__ == "__main__":
    main()