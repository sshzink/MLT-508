from enum import Enum


class POS(Enum):
    NOUN = 1
    VERB = 2
    ADJECTIVE = 3
    ADVERB = 4
    PRONOUN = 5
    PREPOSITION = 6
    CONJUNCTION = 7
    INTERJECTION = 8


class LANG(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
