import requests
from bs4 import BeautifulSoup
import re
import constant
import numpy as np
import parse

class Course:
    def __init__(self, courseTerm='', courseMajor='', courseTitle='', courseCRN='', courseArea='', courseSection='', courseClass='', courseTime='', courseDay='', courseLocation='', courseInstructor='', courseUniversity='', courseCredit='', courseAttribute=[]):
        self.courseTerm = courseTerm
        self.courseMajor = courseMajor
        self.courseTitle = courseTitle
        self.courseCRN = courseCRN
        self.courseArea = courseArea
        self.courseSection = courseSection
        self.courseClass = courseClass
        self.courseTime = courseTime
        self.courseDay = courseDay
        self.courseLocation = courseLocation
        self.courseInstructor = courseInstructor
        self.courseUniversity = courseUniversity
        self.courseCredit = courseCredit
        self.courseAttribute = courseAttribute

    # getters & setters
    def getTerm(self):
        return self.courseTerm

    def getMajor(self):
        return self.courseMajor

    def getTitle(self):
        return self.courseTitle
    
    def getCRN(self):
        return self.courseCRN

    def getArea(self):
        return self.courseArea

    def getSection(self):
        return self.courseSection

    def getClass(self):
        return self.courseClass    

    def getTime(self):
        return self.courseTime 

    def getDay(self):
        return self.courseDay

    def getLocation(self):
        return self.courseLocation

    def getInstructor(self):
        return self.courseInstructor

    def getUniversity(self):
        return self.courseUniversity
    
    def getCredit(self):
        return self.courseCredit

    def getAttribute(self):
        return self.courseAttribute

    # string format
    def __str__(self):
        return self.getTerm() + '|' + self.getMajor() + '|' + self.getTitle() + '|' + self.getCRN() + '|' + self.getArea()  + '|' + self.getSection() + '|' + self.getClass() + '|' + self.getTime()  + '|' + self.getDay()  + '|' + self.getLocation()  + '|' + self.getInstructor()  + '|' + self.getUniversity()  + '|' + self.getCredit() + '|' + ','.join(self.getAttribute()) + '\n'

# crawl the list of course terms with specified num input
# return most recent $(num) course terms
# :param number of course terms to be extracted
# :return list of course terms
def fetchCourseTerm(num): 
    courseTerms = []
    URL = 'https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg'

    # Instantiate a request objects to document
    req = requests.get(URL, timeout=constant.TIMEOUT)
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser')

    # bring option lists into list
    lists = soup.find_all('option', value=True)

    # Iterate the list of terms and append to list
    for list in lists:
        valueTag = list['value']
        month = valueTag[-2:]
        if month[0] < '1' or month[0] == '1' and month[1] <= '2':  
            term = valueTag
            courseTerms.append(term)

        if len(courseTerms) is num :
            break
  
    return courseTerms


# crawl the list of course ID and subjects with specified course term input
# :param course term to extract course subjects available
# :return list of course ID with specified course term
# :return list of course subject
def fetchCourseSubject(courseTerm):
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_disp_cat_term_date'
    
    payload = [
        ('call_proc_in', 'bwckctlg.p_disp_dyn_ctlg'),
        ('cat_term_in', courseTerm)
    ]

    response = requests.get(URL, params=payload, timeout=constant.TIMEOUT)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tagList = soup.find_all('option', value = True)

    courseSubjectPair = {}
    for tag in tagList:
        courseSubjectPair[tag['value']] = tag.text

    return courseSubjectPair


# crawl the list of course number associated with specified course term and course ID input
# :param course term to extract course subjects available
# :param course ID to extract course number
# :return list of course number 
def fetchCourseNum(courseTerm, courseID):
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_display_courses'
    payload = [
        ('term_in', courseTerm),
        ('call_proc_in', 'bwckctlg.p_disp_dyn_ctlg'),
        ('sel_subj', 'dummy'),
        ('sel_levl', 'dummy'),
        ('sel_schd', 'dummy'),
        ('sel_coll', 'dummy'),
        ('sel_divs', 'dummy'),
        ('sel_dept', 'dummy'),
        ('sel_attr', 'dummy'),
        ('sel_subj', courseID),
        ('sel_crse_strt', ''),
        ('sel_crse_end', ''),
        ('sel_title', ''),
        ('sel_from_cred', ''),
        ('sel_to_cred', ''),
    ]

    response = requests.get(URL, params=payload, timeout=constant.TIMEOUT)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tagList = soup.find_all('td', class_='nttitle')

    courseNums = [tag.text.split(' ')[1] for tag in tagList]

    return courseNums


# crawl the list of course information associated with specified course term, course subject, course ID, and course number input
# :param course term
# :param course subject 
# :param course ID 
# :param course number with 
# :return list of course object 
def fetchSchedule(courseTerm, courseSubjectValue, courseSubjectText, courseID):
    courseList = []
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_disp_listcrse'
    payload = [
        ('term_in', courseTerm),
        ('subj_in', courseSubjectValue),
        ('crse_in', courseID),
        ('schd_in', '%')
    ]
    
    response = requests.get(URL, params=payload, timeout=constant.TIMEOUT)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    scheduleTableContent = soup.find('table', class_='datadisplaytable')
    if(not scheduleTableContent.find('th', class_='ddtitle')):
        return

    scheduleTables = scheduleTableContent.prettify().split('<th class="ddtitle" scope="colgroup">')[1:]

    for scheduleTable in scheduleTables:
        soup = BeautifulSoup(scheduleTable, 'html.parser')

        tableHead = soup.find('a')
        title = tableHead.text.split('-')

        courseTitle = title[0].strip()
        courseCRN = title[1].strip()
        courseArea = title[2].strip()
        courseSection = title[3].strip()

        tableBody = soup.find('td', class_='dddefault')
        courseUniversity = re.sub('[:\s+]', '', tableBody.find('span', text=re.compile('Levels:')).next_sibling).strip()
        courseCredit = tableBody.find(text=re.compile('Credits')).strip()
        attributes = tableBody.find_all(string=['Remote Synchronous Course', 'Remote Asynchronous Course', 'Hybrid', 'Residential'])
        courseAttribute = attributes.pop() if len(attributes) > 0 else ''

        bodyInfo = tableBody.find_all('td', class_='dddefault')
        courseClass = bodyInfo[0].text.strip()
        courseTime = bodyInfo[1].text.strip()
        courseDay = bodyInfo[2].text.strip()
        courseLocation = bodyInfo[3].text.strip()
        courseInstructor = bodyInfo[6].text.split('(')[0].strip()

        parse.removeSpaces(courseInstructor)

        courseList.append(Course(courseTerm, courseSubjectText, courseTitle, courseCRN, courseArea, courseSection, courseClass, courseTime, courseDay, courseLocation, courseInstructor, courseUniversity, courseCredit, courseAttribute))

    return courseList
