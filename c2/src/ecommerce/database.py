from typing import Optional

class Database:
    """The database implementation"""

    def __init__(self, connection: Optional[str] = None) -> None:
        """Create a connection to a database"""
        pass

# database = Database("path/to/data")
def get_database(connection: Optional[str] = None) -> Database:
    global db
    if not db:
        db = Database(connection)
    return db
