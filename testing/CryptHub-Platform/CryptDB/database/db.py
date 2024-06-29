from surrealdb import SurrealDB



def get_db():
    db = SurrealDB("ws://localhost:8000/database/namespace")
