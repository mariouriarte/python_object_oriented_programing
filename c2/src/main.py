from ecommerce.database import Database
from typing import Optional

db: Optional[Database] = None


def initialize_database(connection: Optional[str] = None) -> None:
    global db
    db = Database(connection)
