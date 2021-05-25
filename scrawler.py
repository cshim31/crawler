import tools

def main():
    # bring course terms in list
    terms = tools.get_terms(2)
    courseLists = []
    # extraction continues for each course term
    for term in terms: 
        subjects = tools.get_subjects(term)
        courseList = []
        for subject in subjects:
            # bring course numbers for each subject
            nums = tools.get_courseNum(term, subject)
            
            for num in nums:
                # extract course information for each course term 
                courseList = tools.get_course_info(term, subject, num)
        # append course information for each term to list
        courseLists.append(courseList)

    
    # write parsed data to file output in excel
    for courseList in courseLists:
        tools.writeToExcel(courseList)

if __name__ == "__main__":
    main()