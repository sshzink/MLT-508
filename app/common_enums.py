from enum import Enum


class PartOfSpeech(Enum):
    NOUN = 1
    VERB = 2
    ADJECTIVE = 3
    ADVERB = 4
    PRONOUN = 5
    PREPOSITION = 6
    CONJUNCTION = 7
    INTERJECTION = 8


class Language(Enum):
    English = "en"
    Spanish = "es"
    French = "fr"
