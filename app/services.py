import mysql.connector
from db.mysql_repository import *
from db.repository import *
from model.enums import *


class Services:
    def __init__(self):
        self.repo = MySQLRepository()

    def translate_word(self, word: str, source_language: LANG, target_language: LANG):
        word_data = self.repo.get_word_by_form(word, source_language)
        print(word_data.pos)
        if not word_data:
            return None

        pos = word_data.pos

        target_column = f'eq_in_{target_language.value}'
        print(target_column)
        translation_id = getattr(word_data, target_column)
        print(translation_id)

        if translation_id:
            translation = self.repo.get_word_by_id(translation_id, target_language)
            if translation:
                return {'translation': translation.form, 'pos': pos.name}

        return None
