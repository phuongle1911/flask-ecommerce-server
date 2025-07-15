# works as common point for all test files, set up fixtures...

import pytest
from app import app, db

@pytest.fixture
def client():
  # Create sample server
  app.config["TESTING"] = True
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  with app.app_context():
    db.create_all()
    yield app.test_client()
    db.session.remove()
    db.drop_all()
