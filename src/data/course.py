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

class Seat:
    def __init__(self, crn, seatCapacity='', seatActual='', seatRemaining='', waitlistCapacity='', waitlistActual='', waitlistRemaining=''):
        self.crn = crn
        self.seatCapacity = seatCapacity
        self.seatActual = seatActual
        self.seatRemaining = seatRemaining
        self.waitlistCapacity = waitlistCapacity
        self.waitlistActual = waitlistActual
        self.waitlistRemaining = waitlistRemaining

    def getCRN(self):
        return self.crn

    def getSeatCapacity(self):
        return self.seatCapacity

    def getSeatActual(self):
        return self.seatActual

    def getWaitlistCapacity(self):
        return self.waitlistCapacity

    def getWaitlistActual(self):
        return self.waitlistActual

    def getWaitlistRemaining(self):
        return self.waitlistRemaining
