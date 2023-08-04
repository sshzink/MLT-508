import abc
from app.common_enums import *


class AbstractRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def xyz(self):
