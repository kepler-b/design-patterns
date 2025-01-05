class Service:
    def __init__(self, database):
        self.database = database

class Database:
    def query(self):
        return "Querying database..."

def execute():
    db = Database()
    service = Service(db)  # Dependency injected externally
    print(service.database.query())  # Output: Querying database...
