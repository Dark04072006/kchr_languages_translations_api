from sqlite3 import Connection

from app.models.translation import Translation
from app.models.variation import TranslationVariation


class TranslationDAO:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def get_like(
        self, var: TranslationVariation, word: str, limit: int, offset: int
    ) -> list[Translation]:
        query = "SELECT * FROM translations WHERE variation = ? AND word LIKE ? LIMIT ? OFFSET ?"
        params = (var.value, f"%{word}", limit, offset)
        cursor = self.connection.execute(query, params)

        return [Translation(*translation) for translation in cursor.fetchall()]
