from constant.enum_ import PacketType

class Packet:
    def __init__(self, type_=PacketType.PK_NULL):
        self.type_ = type_

    def getType(self):
        return self.type_

class CoursePacket(Packet):
    def __init__(self, type_=PacketType.PK_NULL, courseTerm='', courseSubjectAbbr='', courseSubjectText='', courseNum=''):
        Packet.__init__(self, type_)
        self.courseTerm = courseTerm
        self.courseSubjectAbbr = courseSubjectAbbr
        self.courseSubjectText = courseSubjectText
        self.courseNum = courseNum

    # getters & setters
    def getCourseTerm(self):
        return self.courseTerm

    def getcourseSubjectText(self):
        return self.courseSubjectText

    def getcourseSubjectAbbr(self):
        return self.courseSubjectAbbr

    def getCourseNum(self):
        return self.courseNum

#    def __str__(self):
#        return 'Pakcage : %s %s' %(self.getcourseSubjectText(), self.getCourseNum)


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

#    def __str__(self):
#        return 'Pakcage : %s %s' %(self.getCourseTerm(), self.getCourseCRN)
