from database.session import SessionLocal

def test_session():
    session = SessionLocal()
    try:
        assert session is not None
    finally:
        session.close()