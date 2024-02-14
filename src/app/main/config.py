import os
from typing import Final


DB_URL: Final[str] = os.environ["DB_URL"]
SECRET_KEY: Final[str] = os.environ["SECRET_KEY"]
