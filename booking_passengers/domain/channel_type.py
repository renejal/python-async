import enum

class ChannelType(enum.Enum):
    DEFAULT = 0
    DIRECT = enum.auto()
    WEB = enum.auto()
    GDS = enum.auto()
    API = enum.auto()