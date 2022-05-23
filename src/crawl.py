import requests
from bs4 import BeautifulSoup
import re
import numpy as np

from constant import config
from data.course import Course
from data.seat import Seat
from log import *
import parse

# crawl the list of course terms with specified num input
# return most recent $(num) course terms
# :param number of course terms to be extracted
# :return list of course terms

def fetchCourseTerm(num): 
    URL = 'https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    req = requests.get(URL, headers=headers, timeout=config.TIMEOUT)
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser')

    options = soup.find_all('option', value=True)
    terms = [option['value'] for option in options]
    
    courseTerm = [term for term in terms if term and int(term) % 100 < 10]

    return courseTerm[:num]


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

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(URL, headers=headers, params=payload, timeout=config.TIMEOUT)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tagList = soup.find_all('option', value = True)

    courseSubjectPair = {}
    for tag in tagList:
        courseSubjectPair[tag['value']] = tag.text

    return courseSubjectPair


# crawl the list of course CRN associated with specified course term, course subject, course ID, and course number input
# :param course term
# :param course subject 
# :param course ID 
# :param course number with 
# :return list of course object 
def fetchCourseCRN(courseTerm, courseSubjectAbbr):
    courseCRNList = []
    URL = 'https://oscar.gatech.edu/bprod/bwckschd.p_get_crse_unsec'
    
    payload = [
        ('term_in', courseTerm),
        ('sel_subj', 'dummy'),
        ('sel_day', 'dummy'),
        ('sel_schd', 'dummy'),
        ('sel_insm', 'dummy'),
        ('sel_camp', 'dummy'),
        ('sel_levl', 'dummy'),
        ('sel_sess', 'dummy'),
        ('sel_instr', 'dummy'),
        ('sel_ptrm', 'dummy'),
        ('sel_attr', 'dummy'),
        ('sel_subj', courseSubjectAbbr),
        ('sel_crse', ''),
        ('sel_title', ''),
        ('sel_from_cred', ''),
        ('sel_to_cred', ''),
        ('sel_instr', '%'),
        ('sel_attr', '%'),
        ('begin_hh', '0'),
        ('begin_mi', '0'),
        ('begin_ap', 'a'),
        ('end_hh', '0'),
        ('end_mi', '0'),
        ('end_ap', 'a'),
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    response = requests.get(URL, headers=headers, params=payload, timeout=config.TIMEOUT)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    scheduleTableContent = soup.find('table', class_='datadisplaytable')
    if(not scheduleTableContent.find('th', class_='ddtitle')):
        return

    scheduleTables = scheduleTableContent.prettify().split('<th class="ddtitle" scope="colgroup">')[1:]
    
    for scheduleTable in scheduleTables:
        soup = BeautifulSoup(scheduleTable, 'html.parser')
        tableHead = soup.find('a')
        title = tableHead.text.split(' - ')

        courseTitle = title[0].strip()
        courseCRN = title[1].strip()
        courseArea = title[2].strip()
        courseSection = title[3].strip()

        courseCRNList.append(courseCRN)

    return courseCRNList

# crawl the list of course information associated with specified course term, course subject, course ID, and course number input
# :param course term
# :param course subject 
# :param course ID 
# :param course number with 
# :return list of course object 
def fetchCourseSchedule(courseTerm, courseSubjectAbbr, courseSubjectText):
    #log_debug(f'fetcing {courseTerm}:{courseSubjectText}: {courseNum}')
    courseList = []
    URL = 'https://oscar.gatech.edu/bprod/bwckschd.p_get_crse_unsec'
    
    payload = [
        ('term_in', courseTerm),
        ('sel_subj', 'dummy'),
        ('sel_day', 'dummy'),
        ('sel_schd', 'dummy'),
        ('sel_insm', 'dummy'),
        ('sel_camp', 'dummy'),
        ('sel_levl', 'dummy'),
        ('sel_sess', 'dummy'),
        ('sel_instr', 'dummy'),
        ('sel_ptrm', 'dummy'),
        ('sel_attr', 'dummy'),
        ('sel_subj', courseSubjectAbbr),
        ('sel_crse', ''),
        ('sel_title', ''),
        ('sel_from_cred', ''),
        ('sel_to_cred', ''),
        ('sel_instr', '%'),
        ('sel_attr', '%'),
        ('begin_hh', '0'),
        ('begin_mi', '0'),
        ('begin_ap', 'a'),
        ('end_hh', '0'),
        ('end_mi', '0'),
        ('end_ap', 'a'),
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    response = requests.get(URL, headers=headers, params=payload, timeout=config.TIMEOUT)
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
        if not bodyInfo: continue

        courseClass = bodyInfo[0].text.strip()
        courseTime = bodyInfo[1].text.strip()
        courseDay = bodyInfo[2].text.strip()
        courseLocation = bodyInfo[3].text.strip()
        courseInstructor = bodyInfo[6].text.split('(')[0].strip()

        parse.removeSpaces(courseInstructor)

        courseList.append(Course(courseTerm, courseSubjectText, courseTitle, courseCRN, courseArea, courseSection, courseClass, courseTime, courseDay, courseLocation, courseInstructor, courseUniversity, courseCredit, courseAttribute))

    return courseList

def fetchCourseSeat(courseTerm, courseCRN):
    URL = 'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched'
    payload = [
        ('term_in', courseTerm),
        ('crn_in', courseCRN),
    ]

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    response = requests.get(URL, headers=headers, params=payload, timeout=config.TIMEOUT)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    courseSeat = soup.find('table', class_='datadisplaytable') 

    if not courseSeat:
        return

    seatTable = courseSeat.find('table', class_='datadisplaytable') 

    if not seatTable:
        return
    
    seatTableRow = seatTable.find_all('tr')

    courseSeats = seatTableRow[1].find_all('td', class_='dddefault')
    seatCap = courseSeats[0].text
    seatActual = courseSeats[1].text
    seatRemaining = courseSeats[2].text
    
    courseWaitlistSeat = seatTableRow[2].find_all('td', class_='dddefault')
    waitlistCap = courseWaitlistSeat[0].text
    waitlistActual = courseWaitlistSeat[1].text
    waitlistRemaining = courseWaitlistSeat[2].text

    seat = Seat(courseTerm, courseCRN, seatCap, seatActual, seatRemaining, waitlistCap, waitlistActual, waitlistRemaining)
    
    return seat