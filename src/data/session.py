class Session:
    def __init__(self, courseList=[], seatList=[]):
        self.courseList = courseList
        self.seatList = seatList

    def getCourseList(self):
        return self.courseList

    def getSeatList(self):
        return self.seatList