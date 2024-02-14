from sqlite3 import Connection
from typing import Any, Generator

from dishka import Provider, Scope, provide

from app.main.config import DB_URL
from app.database.translation_dao import TranslationDAO


class DbAdaptersProvider(Provider):
    @provide(scope=Scope.APP, provides=Connection)
    def connection(self) -> Generator[Connection, Any, None]:
        with Connection(DB_URL, check_same_thread=False) as connection:
            yield connection

    translation_dao = provide(
        TranslationDAO, scope=Scope.REQUEST, provides=TranslationDAO
    )
