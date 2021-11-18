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

class CourseSeat:
    def __init__(self, seat, waitlistSeat):
        self.seat = seat
        self.waitlistSeat = waitlistSeat
    
    def getSeat(self):
        return self.seat

    def getWaitlistSeat(self):
        return self.waitlistSeat

    def __str__(self):
        return f'Seat={self.getSeat()}, Waitlist={self.getWaitlistSeat()}'

class Seat:
    def __init__(self, capacity, actual, remaining):
        self.capacity = capacity
        self.actual = actual
        self.remaining = remaining

    def __str__(self):
        return '('+ self.capacity + ',' + self.actual + ',' + self.remaining + ')'

class WaitlistSeat:
    def __init__(self, capacity, actual, remaining):
        self.capacity = capacity
        self.actual = actual
        self.remaining = remaining

    def __str__(self):
        return '('+ self.capacity + ',' + self.actual + ',' + self.remaining + ')'