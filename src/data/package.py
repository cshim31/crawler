from . import packet
from . import session

class Package:
    def __init__(self, packet=None, session=None):
        self.packet = packet
        self.session = session

    def getPacket(self):
        return self.packet

    def getSession(self):
        return self.session