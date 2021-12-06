
class Seat:
    def __init__(self, courseTerm, crn, seatCapacity='', seatActual='', seatRemaining='', waitlistCapacity='', waitlistActual='', waitlistRemaining=''):
        self.courseTerm = courseTerm
        self.crn = crn
        self.seatCapacity = seatCapacity
        self.seatActual = seatActual
        self.seatRemaining = seatRemaining
        self.waitlistCapacity = waitlistCapacity
        self.waitlistActual = waitlistActual
        self.waitlistRemaining = waitlistRemaining

    def getCourseTerm(self):
        return self.courseTerm

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
