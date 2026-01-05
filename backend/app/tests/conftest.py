from collections.abc import Generator
import pytest
import os
# Set environment before importing ANYTHING else
os.environ["ENVIRONMENT"] = "testing"

from fastapi.testclient import TestClient
from sqlmodel import Session
from sqlalchemy import event

from app.core.db import engine
from app.api.deps import get_db
from app.main import app

@pytest.fixture(scope="function")
def db() -> Generator[Session, None, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    nested = session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(sess, trans):
        if trans.nested and not trans._parent.nested:
            sess.begin_nested()

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()

@pytest.fixture(scope="function")
def client(db: Session):
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c