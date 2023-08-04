import mysql.connector
from db.mysql_repository import *


class LanguageTranslator:
    def __init__(self):
        self.translations_db = MySQLRepository()

    def translate_word(self, word, source_language, target_language):
        translation = self._translate(word, source_language, target_language)
        synonyms = self._get_synonyms(word, target_language)
        pos = self._get_pos(word, target_language)

        self.translations_db.get_translation(word, source_language, target_language)

        return translation, synonyms, pos

    def _translate(self, word, source_language, target_language):
        translation = f"{word} ({source_language}) => {word} ({target_language})"
        return translation

    def _get_synonyms(self, word, language):
        synonyms = ["synonym1", "synonym2", "synonym3"]
        return synonyms

    def _get_pos(self, word, language):
        pos = "Noun"
        return pos
