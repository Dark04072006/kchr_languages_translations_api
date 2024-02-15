from sqlite3 import Connection

from app.models.translation import Translation


class TranslationDAO:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def get_like(
        self, var: str, word: str, limit: int, offset: int
    ) -> list[Translation]:
        query = "SELECT * FROM translations WHERE variation = ? AND word LIKE ? LIMIT ? OFFSET ?"
        params = (var, f"%{word}", limit, offset)
        cursor = self.connection.execute(query, params)

        return [Translation(*translation) for translation in cursor.fetchall()]
