from db.repository import *
import mysql.connector
from model.word import *
from model.enums import *


class MySQLRepository(Lexicon):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'mlt'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor is not None:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()

    def get_word_by_form(self, word_form, lang):
        query = "SELECT * FROM words WHERE form = %s AND lang = %s"
        params = (word_form, lang.value)
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()

        print(result)

        if result:
            return Word(result['id'], result['form'], LANG(result['lang']), POS(result['pos']), result['eq_in_en'], result['eq_in_es'], result['eq_in_fr'])
        else:
            return None


    def get_word_by_id(self, word_id, lang):
        query = "SELECT * FROM words WHERE id = %s AND lang = %s"
        params = (word_id, lang.value)
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()

        if result:
            return Word(result['id'], result['form'], LANG(result['lang']), POS(result['pos']), result['eq_in_en'], result['eq_in_es'], result['eq_in_fr'])
        else:
            return None
