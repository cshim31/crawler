class CoursePackage:
    def __init__(self, courseTerm='', courseSubjectKey='', courseSubjectValue='', courseNum=''):
        self.courseTerm = courseTerm
        self.courseSubjectKey = courseSubjectKey
        self.courseSubjectValue = courseSubjectValue
        self.courseNum = courseNum

    # getters & setters
    def getTerm(self):
        return self.courseTerm

    def getSubjectKey(self):
        return self.courseSubjectKey

    def getSubjectValue(self):
        return self.courseSubjectValue

    def getNum(self):
        return self.courseNum

    def __str__(self):
        return 'Pakcage : %s %s' %(getSubjectKey(), getNum)