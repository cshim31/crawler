from constant.enum_ import PacketType

class Packet:
    def __init__(self, type_=PacketType.PK_NULL):
        self.type_ = type_

    def getType(self):
        return self.type_

class CoursePacket(Packet):
    def __init__(self, type_=PacketType.PK_NULL, courseTerm='', courseSubjectKey='', courseSubjectValue='', courseNum=''):
        Packet.__init__(self, type_)
        self.courseTerm = courseTerm
        self.courseSubjectKey = courseSubjectKey
        self.courseSubjectValue = courseSubjectValue
        self.courseNum = courseNum

    # getters & setters
    def getCourseTerm(self):
        return self.courseTerm

    def getCourseSubjectKey(self):
        return self.courseSubjectKey

    def getCourseSubjectValue(self):
        return self.courseSubjectValue

    def getCourseNum(self):
        return self.courseNum

    def __str__(self):
        return 'Pakcage : %s %s' %(getCourseSubjectKey(), getCourseNum)


class SeatPacket(Packet):
    def __init__(self, type_=PacketType.PK_NULL, courseTerm='', courseCRN=''):
        Packet.__init__(self, type_)
        self.courseTerm = courseTerm
        self.courseCRN = courseCRN

    # getters & setters
    def getCourseTerm(self):
        return self.courseTerm

    def getCourseCRN(self):
        return self.courseCRN

    def __str__(self):
        return 'Pakcage : %s %s' %(getCourseTerm(), getCourseCRN)
