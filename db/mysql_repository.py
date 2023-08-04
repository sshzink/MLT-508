from db.repository import *
import mysql.connector


class MySQLRepository(AbstractRepository):
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
        self.cursor.close()
        self.connection.close()

    def create_table(self):
        create_table_query = (
            "CREATE TABLE IF NOT EXISTS translations ("
            "word VARCHAR(255) NOT NULL,"
            "source_language VARCHAR(255) NOT NULL,"
            "target_language VARCHAR(255) NOT NULL,"
            "translation TEXT NOT NULL,"
            "synonyms TEXT,"
            "pos VARCHAR(50),"
            "PRIMARY KEY (word, source_language)"
            ")"
        )
        with self.connection.cursor() as cursor:
            cursor.execute(create_table_query)
        self.connection.commit()

    def save_translation(self, word, source_language, target_language, translation, synonyms, pos):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO translations (word, source_language, target_language, translation, synonyms, pos) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (word, source_language, target_language, translation, synonyms, pos)
            )
        self.connection.commit()

    def get_translation(self, word, source_language, target_language):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT translation, synonyms, pos FROM translations WHERE word = %s AND source_language = %s AND target_language = %s",
                (word, source_language, target_language)
            )
            result = cursor.fetchone()
            if result:
                translation, synonyms, pos = result
                return {
                    "translation": translation,
                    "synonyms": synonyms.split(",") if synonyms else [],
                    "pos": pos,
                }
            else:
                return None

    def close_connection(self):
        self.connection.close()
