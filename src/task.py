import crawl
import numpy as np
import time
from threading import Thread

import crawl
from constant import config
from constant.enum_ import PacketType
from data.contents import ContentsProcess
from data.package import Package
from data.packet import Packet, CoursePacket, SeatPacket
from data.session import Session
import parse
import thread as th

# main thread task
def task(courseTerm):
    contentsProcess = ContentsProcess()

    contentsProcess.threadPool_.extend([Thread(target=contentsProcess.process, args=()) for i in range(config.THREAD_COUNT)])
    th.executeThreads(contentsProcess.getThreadPool())

    session = Session([], [])
    
    # request schedule
    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectAbbr,courseSubjectText in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectAbbr)
        for courseNum in courseNums:
            print('requesting %s:%s, %s' % (courseSubjectAbbr, courseNum, courseTerm))
            packet = CoursePacket(PacketType.PK_REQ_SCHEDULE, courseTerm, courseSubjectAbbr, courseSubjectText, courseNum)
            contentsProcess.putPackage(Package(packet, session))

            courseCRNList = crawl.fetchCourseCRN(courseTerm, courseSubjectAbbr, courseSubjectText, courseNum)
            if not courseCRNList:
                print('request pass')
                continue
            contentsProcess.putPackage(SeatPacket(PacketType.PK_REQ_SEAT, courseTerm, courseCRN) for courseCRN in courseCRNList) 
    '''
    # request seat
    for courseSubjectAbbr,courseSubjectText in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectAbbr)
        for courseNum in courseNums:
            courseCRNList = crawl.fetchCourseCRN(courseTerm, courseSubjectAbbr, courseSubjectText, courseNum)
            if not courseCRNList:
                print('request pass')
                continue
                
            for courseCRN in courseCRNList:
                print('requesting %s:%s' %(courseTerm, courseCRN))
                packet = SeatPacket(PacketType.PK_REQ_SEAT, courseTerm, courseCRN) 
                contentsProcess.putPackage(Package(packet, session))

    '''
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_CSV, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_JSON, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_REQ_EXIT, courseTerm), session))