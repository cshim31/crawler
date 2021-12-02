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

    session = Session()
    # request schedule
    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectAbbr,courseSubjectText in courseSubjectPair.items():
        print('requesting %s:%s' % (courseSubjectAbbr, courseTerm))
        
        packet = CoursePacket(PacketType.PK_REQ_SCHEDULE, courseTerm, courseSubjectAbbr, courseSubjectText)
        contentsProcess.putPackage(Package(packet, session))

        packet = SeatPacket(PacketType.PK_REQ_SEAT, courseTerm, courseSubjectAbbr)
        contentsProcess.putPackage(Package(packet, session))

    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_COURSE_CSV, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_COURSE_JSON, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_SEAT_CSV, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_SEAT_JSON, courseTerm), session))

    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_REQ_EXIT, courseTerm), session))

    th.joinThreads(contentsProcess.getThreadPool())