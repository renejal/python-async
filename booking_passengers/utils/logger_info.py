import logging

from uamqp import message

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class messages(metaclass=SingletonMeta):
    init = False
    logger = None
    def inicialize(self):
        if self.init:
            logger = logging.getLogger("gds_otas")
            logger.setLevel(logging.INFO)
            fhandler = logging.FileHandler(filename='bookings.log', mode='a')
            logger.addHandler(fhandler)
            self.logger = logger
            self.init = True
        return self.logger
    def get(self):
        return self.logger



    