from database.connection import engine

def test_connection():
    with engine.connect() as connection:
        assert connection is not None