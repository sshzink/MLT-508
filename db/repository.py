import abc
from model.enums import *
from model.word import *

class Lexicon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_word_by_form(self, form: str, lang: LANG) -> Word:
        pass

    @abc.abstractmethod
    def get_word_by_id(self, id: int, lang: LANG) -> Word:
        pass
