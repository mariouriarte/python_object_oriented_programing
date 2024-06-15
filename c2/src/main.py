from ecommerce.database import get_database, Database
from typing import Optional

db: Optional[Database] = None


def initialize_database(connection: Optional[str] = None) -> None:
    global db
    db = get_database(connection)


if __name__ == "__main__":
    initialize_database()
    print(db)
