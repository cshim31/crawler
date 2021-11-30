from constant.enum_ import PacketType

class Packet:
    def __init__(self, type_=PacketType.PK_NULL):
        self.type_ = type_

    def getType(self):
        return self.type_

class CoursePacket(Packet):
    def __init__(self, type_=PacketType.PK_REQ_SCHEDULE, courseTerm='', courseSubjectAbbr='', courseSubjectText=''):
        Packet.__init__(self, type_)
        self.courseTerm = courseTerm
        self.courseSubjectAbbr = courseSubjectAbbr
        self.courseSubjectText = courseSubjectText

    # getters & setters
    def getCourseTerm(self):
        return self.courseTerm

    def getCourseSubjectText(self):
        return self.courseSubjectText

    def getCourseSubjectAbbr(self):
        return self.courseSubjectAbbr

class SeatPacket(Packet):
    def __init__(self, type_=PacketType.PK_REQ_SEAT, courseTerm='', courseSubjectAbbr=''):
        Packet.__init__(self, type_)
        self.courseTerm = courseTerm
        self.courseSubjectAbbr = courseSubjectAbbr
    # getters & setters
    def getCourseTerm(self):
        return self.courseTerm

    def getCourseSubjectAbbr(self):
        return self.courseSubjectAbbr

