import mysql.connector
from db.mysql_repository import *
from db.repository import *
from model.enums import *

class Services:
    def __init__(self):
        self.repo = MySQLRepository()

    def translate_word(self, word: str, target_language: LANG):
        # Fetch word data for the input word
        word_data = self.repo.get_word_by_form(word, target_language)
        if not word_data:
            return None

        pos = POS(word_data.pos).name

        # Determine the target column based on the target language
        target_column = f'eq_in_{target_language.value}'
        translation_id = getattr(word_data, target_column)

        if translation_id:
            # Fetch the translation in the target language
            translation = self.repo.get_word_by_id(translation_id, target_language)
            if translation:
                return f"{translation.form}, {pos}"

        return None
