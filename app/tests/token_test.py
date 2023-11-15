from app.auth.models import User
import pytest
from app import create_app
from flask_login import login_user, current_user, logout_user

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Desactiva CSRF para pruebas
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_authenticated(client):

    # Crea un usuario simulado
    user = User(id=1, username='testuser',email='a@us.es',password="s",token=0)  # Asegúrate de establecer los campos necesarios de tu modelo de usuario
    with app.app_context:
    # Autentica al usuario simulado
        login_user(user)

    # Verifica que el usuario esté autenticado
    assert current_user.is_authenticated

    response = client.post('/token_request/create', data={'num_token': 2, 'description': 'Test description'})
    
    assert b'Redirected' in response.data
    assert b'/token_request/create' not in response.data

    # Desconecta 

