import requests
import json
from bs4 import BeautifulSoup
import re
class Course:
    def __init__(self, term='', courseTitle='', courseCRN='', courseID='', sectionID='', type='', time='', days='', location='', instructor='', subject = '', level='', credit=''):
        self.term = term
        self.courseTitle = courseTitle
        self.courseCRN = courseCRN
        self.courseID = courseID
        self.sectionID = sectionID
        self.type = type
        self.time = time
        self.days = days
        self.location = location
        self.instructor = instructor
        self.subject = subject
        self.level = level
        self.credit = credit

    # getters & setters
    def getTerm(self):
        return self.term

    def getCourseTitle(self):
        return self.courseTitle
    
    def getCourseCRN(self):
        return self.courseCRN

    def getCourseID(self):
        return self.courseID

    def getSectionID(self):
        return self.sectionID

    def getType(self):
        return self.type    

    def getTime(self):
        return self.time 

    def getDays(self):
        return self.days

    def getLocation(self):
        return self.location

    def getInstructor(self):
        return self.instructor

    def getSubject(self):
        return self.subject

    def getLevel(self):
        return self.level
    
    def getCredit(self):
        return self.credit

    # string format
    def __str__(self):
        return self.getTerm() + ',' + self.getSubject() + ',' + self.getCourseTitle() + ',' + self.getCourseCRN() + ',' + self.getCourseID()  + ',' + self.getSectionID() + ',' + self.getType() + ',' + self.getTime()  + ',' + self.getDays()  + ',' + self.getLocation()  + ',' + self.getInstructor()  + ',' + self.getLevel()  + ',' + self.getCredit() + '\r\n'


# @param number of course terms to be extracted
def get_terms(num): 
    course_terms = []
    URL = 'https://oscar.gatech.edu/pls/bprod/bwckctlg.p_disp_dyn_ctlg'

    # Instantiate a request objects to document
    req = requests.get(URL)
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
            course_terms.append(term)

        if len(course_terms) is num :
            break

    print('Found ', len(course_terms), ' course terms')       
    return course_terms


def get_subjects(course_term):
    courseIDs = []
    course_subjects = []
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_disp_cat_term_date'
    
    data = {
        'call_proc_in' : 'bwckctlg.p_disp_dyn_ctlg',
        'cat_term_in' : course_term
    }
    response = requests.post(URL, data)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # bring option lists into list
    lists = soup.find_all('option', value = True)

    # Iterate the list of terms and append to list
    for list in lists:
        courseID = list['value']
        course_subject = list.text
        courseIDs.append(courseID)
        course_subjects.append(course_subject)

    print(course_term, ': Found ', len(course_subjects), ' course subjects')       
    return courseIDs, course_subjects

# :param one single subject per each call
def get_courseNum(course_term, cours_IDs):
    course_nums = []
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_display_courses?term_in='+course_term+'&call_proc_in=bwckctlg.p_disp_dyn_ctlg&sel_subj=dummy&sel_levl=dummy&sel_schd=dummy&sel_coll=dummy&sel_divs=dummy&sel_dept=dummy&sel_attr=dummy&sel_subj='+cours_IDs+'&sel_crse_strt=&sel_crse_end=&sel_title=&sel_levl=%&sel_schd:%&sel_coll:%&sel_divs:%&sel_dept:%&sel_from_cred:&sel_to_cred:&sel_attr:%'
    '''
    # facing error during post
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_display_courses'
    data = {
        'term_in': course_term,
        'call_proc_in': 'bwckctlg.p_disp_dyn_ctlg',
        'sel_subj' : 'dummy',
        'sel_level' : 'dummy',
        'sel_schd' : 'dummy',
        'sel_coll' : 'dummy',
        'sel_divs' : 'dummy',
        'sel_dept' : 'dummy',
        'sel_attr' : 'dummy',
        'sel_subj': course_subject,
        'sel_crse_strt': None,
        'sel_crse_end': None,
        'sel_title': None,
        'sel_levl': '%',
        'sel_schd': '%',
        'sel_coll': '%',
        'sel_divs': '%',
        'sel_dept': '%',
        'sel_from_cred': None,
        'sel_to_cred': None,
        'sel_attr': '%'
    }
    '''
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

     # bring a tag lists into list
    lists = soup.find_all('td', class_='nttitle')
    # Iterate the list of subject numbers and append to list
    for list in lists:
        title = list.text
        courseNum = title.split(' ')[1]
        course_nums.append(courseNum)

    print(cours_IDs, ': Found ', len(course_nums), ' course numbers')       
    return course_nums


def get_course_info(course_term, course_subject, course_ID, course_num):
    print(course_term, ' : ', course_subject, ' : ', course_ID, ' : ', course_num)
    courseList = []
    URL = 'https://oscar.gatech.edu/bprod/bwckctlg.p_disp_listcrse?term_in='+course_term+'&subj_in='+course_ID+'&crse_in='+course_num+'&schd_in=%' 
    '''
    data = {
        'term_in' : course_term,
        'subj_in' : course_ID,
        'crse_in' : course_num,
        'schd_in' : '%'
    }
'''
    response = requests.get(URL)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # bring course list to lists 
    data = soup.find('table', class_='datadisplaytable')

    # check if course schedule exists or not
    if(not data.find('th', class_='ddtitle')):
        print("ERROR::Schedule not found")
        return

    lists = str(data).split('<th class="ddtitle" scope="colgroup">')[1:]
    # Iterate the list of terms and append to list
    for list in lists:
        # reinstantiate soup object for course info body
        soup = BeautifulSoup(list, 'html.parser')
        # course header info
        titleStr = soup.find('a').text
        title = titleStr.split('-')
        term = course_term.strip()
        subject = course_subject.strip()
        courseTitle = ''.join(title[:-3]).strip()  
        courseCRN = title[-3].strip()
        courseID = title[-2].strip()
        sectionID = title[-1].strip()
        print(title)
        # course body info
        body = soup.find('td', class_='dddefault')
        level = body.find(text=re.compile('Levels')).strip()
        credit = body.find(text=re.compile('Credits')).strip()
        bodyInfo = body.find_all('td')
        if bodyInfo:
            type = bodyInfo[0].text.strip()
            time = bodyInfo[1].text.strip()
            days = bodyInfo[2].text.strip()
            location = bodyInfo[3].text.strip()
            instructor = bodyInfo[6].text.strip()

            # Instantiate each course and append to course list
            courseList.append(Course(term, courseTitle, courseCRN, courseID, sectionID, type, time, days, location, instructor, subject, level, credit))

        else:
            courseList.append(Course(term, courseTitle, courseCRN, courseID, sectionID, level=level, credit=credit))

    return courseList


# write html text to index.html for debug
# :param string html text
def debug_writeToHTML(html):
    f = open("data/index.html", 'w', encoding='UTF-8')
    f.write(html)
    f.close()

# output parsed data to excel file
# :param list of Course object
def writeToExcel(courseList):
    f = open("data/" + courseList[0].getTerm() + '.txt', 'w', encoding='UTF-8')
    
    for course in courseList:
        f.write(str(course))
    
    f.close()
    