from app.auth.models import User
import pytest
from flask import Flask
from app import create_app, db
from app.token_request.models import Token_request, TokenState
from app.token_request.routes import create

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()
@pytest.fixture(scope='module')
def create_test_user():
    user = User(username='profesor1', email='profesor1@profesor1.com', password='profesor1')
    db.session.add(user)
    db.session.commit()
    return user
@pytest.fixture
def authenticated_client(client, create_test_user):
    user = create_test_user
    with client.session_transaction() as session:
        session['user_id'] = user.id
        session['_fresh'] = True

    yield client
def test_create_view_get(client):
    response = client.get("/token_request/create")
    assert response.status_code == 200

def test_create_view_post_valid(client):
    response = client.post("/token_request/create", data={
        'num_token': 2,
        'description': 'Test description'
    })
    # Asegúrate de cambiar este assert según tu lógica de redireccionamiento
    assert response.status_code == 302

def test_create_view_post_invalid(client):
    response = client.post("/token_request/create", data={
        'num_token': 4,  # Más del límite permitido
        'description': 'Test description'
    })
    assert response.status_code == 200
    # Aquí puedes verificar si se muestra un mensaje de error específico


