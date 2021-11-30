from enum import Enum

class PacketType(Enum):
    PK_NULL = 0
    PK_REQ_SCHEDULE = 10000
    PK_REQ_SEAT = 10001
    PK_WRITE_CSV = 50000
    PK_WRITE_JSON = 50001
    PK_REQ_EXIT = 1
