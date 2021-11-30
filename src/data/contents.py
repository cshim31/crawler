from collections import deque
import time

from data.package import Package
from constant.enum_ import PacketType 
import crawl
import parse
import thread as th

class ContentsProcess:
    def __init__(self):
        self.threadPool_ = []
        self.packageQueue_ = deque([])
        self.runFuncTable = {}
        self.running = True

        self.registerRunFunc()

    def putPackage(self, package):
        self.packageQueue_.append(package)
       # print('put %s' %(package))

    def execute(self):
        if not self.packageQueue_:
            return 

        package = self.packageQueue_.popleft()
        
        if not package:
            return

        self.run(package)
        

    def run(self, package):
        packageType = package.getPacket().getType()
        if not self.runFuncTable[packageType]:
            return

        self.runFuncTable[packageType](package.getSession(), package.getPacket())
            

    def terminate(self):
        setRunning(False)


    def process(self):
        while self.running:
            self.execute()

    def registerRunFunc(self): 
        self.runFuncTable[PacketType.PK_NULL] = None
        self.runFuncTable[PacketType.PK_REQ_SCHEDULE] = self.pakcet_request_schedule
        self.runFuncTable[PacketType.PK_REQ_SEAT] = self.packet_request_seat
        self.runFuncTable[PacketType.PK_WRITE_CSV] = self.packet_write_csv
        self.runFuncTable[PacketType.PK_WRITE_JSON] = self.packet_write_json
        self.runFuncTable[PacketType.PK_REQ_EXIT] = self.packet_request_exit

    # getters & setters
    def getThreadPool(self):
        return self.threadPool_

    def getPackageQueue(self):
        return self.packageQueue_

    def getRunFuncTable(self):
        return self.runFuncTable

    def getRunning(self):
        return self.running
        
    def setRunning(self, running):
        self.running = running


    # packet functionalities
    def pakcet_request_schedule(self, session, packet):
        print('Processing Schedule %s:%s' %(packet.getCourseTerm(), packet.getCourseSubjectAbbr()))
        schedule = crawl.fetchCourseSchedule(packet.getCourseTerm(), packet.getCourseSubjectAbbr(), packet.getCourseSubjectText())
        if schedule: 
            session.getCourseList().extend(schedule)
        
        return

    def packet_request_seat(self, session, packet):
        print('Processing Seat %s:%s' %(packet.getCourseTerm(), packet.getCourseSubjectAbbr()))
        crnList = crawl.fetchCourseCRN(packet.getCourseTerm(), packet.getCourseSubjectAbbr())
        if not crnList:
            return

        
        for crn in crnList:
            seat = crawl.fetchCourseSeat(packet.getCourseTerm(), crn)
            if seat:
                session.getSeatList().append(seat) 

        return

    def packet_write_csv(self, session, packet):
        parse.writeCSV(session.getCourseList(), packet.getCourseTerm() + '_course')
        parse.writeCSV(session.getSeatList(), packet.getCourseTerm() + '_seat')

        return 

    def packet_write_json(self, session, packet):
        parse.writeJson(session.getCourseList(), packet.getCourseTerm() +  '_course')
        parse.writeJson(session.getSeatList(), packet.getCourseTerm() + '_seat')

        return

    def packet_request_exit(self, session, packet):
        i = 0
        bisAlive = True

        while bisAlive and i <= 10:
            bisAlive = th.checkThreadStatus(self.threadPool_)
            time.sleep(10)
            i += 1

        if not bisAlive:
            self.setRunning(False)
            print('Threads Terminated')

        else:
            print('TIMEOUT::Failed terinating threads')

        return