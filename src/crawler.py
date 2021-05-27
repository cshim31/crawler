import time
from time import gmtime, strftime

import tools
import constant


def main():
    start_time = time.time()
    formatted_stime = gmtime()

    # bring one most recent course term into list
    terms = tools.get_terms(constant.DEFAULT)
    courseLists = [[]]
    # extraction continues for each course term
    for term in terms: 
        courseIDs, subjects = tools.get_subjects(term)
        courseList = []
        for i in range(len(subjects)):
            # bring course numbers for each subject
            nums = tools.get_courseNum(term, courseIDs[i])
            
            for num in nums:
                # extract course information for each course term 
                courseList = tools.get_course_info(term, subjects[i], courseIDs[i], num)
                if courseList is not None:
                    # append course information for each term to list
                    courseLists.append(courseList)

    
        # write parsed data to file output in excel
        print("Writing to excel")
        for courseList in courseLists:
            tools.writeToExcel(courseList, term)

    # time taken report
    end_time = time.time()
    formatted_etime = gmtime()

    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_stime))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", formatted_etime))
    print("--- %s seconds ---" % (end_time - start_time))
if __name__ == "__main__":
    main()