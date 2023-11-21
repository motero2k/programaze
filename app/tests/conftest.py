import pytest
from app import create_app,db

@pytest.feature()
def app():
    app=create_app()
    with app.app_context():
        db.create_all()
        
    yield app

@pytest.feature()
def client(app):
    return app.test_client()