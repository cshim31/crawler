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
    courseSubjectPair = crawl.fetchCourseSubject(courseTerm)
    for courseSubjectKey,courseSubjectValue in courseSubjectPair.items():
        courseNums = crawl.fetchCourseNum(courseTerm, courseSubjectKey)
        for courseNum in courseNums:
            packet = CoursePacket(PacketType.PK_REQ_SCHEDULE, courseTerm, courseSubjectKey, courseSubjectValue, courseNum)
            contentsProcess.putPackage(Package(packet, session))


    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_CSV, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_WRITE_JSON, courseTerm), session))
    contentsProcess.putPackage(Package(CoursePacket(PacketType.PK_REQ_EXIT, courseTerm), session))