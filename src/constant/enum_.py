from enum import Enum

class PacketType(Enum):
    PK_NULL = 0
    PK_REQ_SCHEDULE = 1
    PK_REQ_SEAT = 2
    PK_WRITE_CSV = 3
    PK_WRITE_JSON = 4
    PK_REQ_EXIT = 5