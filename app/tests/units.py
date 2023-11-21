import unittest
from app.token_request.models import Token_request,TokenState
from app.auth.models import User
from app import get_test_client, db
from flask_login import current_user, login_user, login_manager,FlaskLoginClient
from app.auth.forms import SignupForm, LoginForm



class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        with self.app.application.app_context():
            print("USERSSSSS:",User.query.all())
            user = User("lolitofdez222","a233@us.es","pass",0)
            print("USER SELECTED",user)
            login_manager.session_protection = None
            


    def client(self):
        # Configura Flask y Flask-Login
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Desactiva CSRF para pruebas
        login_manager.init_app(self.app)

        # Crea un usuario para las pruebas
        user = User(username='usuario_prueba', password='contrasena_prueba')
        
        # Inicia sesión al usuario de prueba
        with self.app.test_client() as client:
            login_user(user)
            yield client

    def tearDown(self):
        pass

   
    def test_token(self):
        with self.app.application.app_context():
            user = User.query.get(1)
            test_client = FlaskLoginClient
            
            
            # This request has user 1 already logged in!
            self.app.post('/login', data=dict(
            email='profesor1',
            password='profesor1'
    ), follow_redirects=True)
            response = client.post('/token_request/create', data=dict(
            num_token = 1,
            description='Quiero proponer',
            token_state=TokenState.PENDING_OF_ACEPTATION,
        ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

    def test_show_env(self):
        response = self.app.get('/env')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
    

    def test_test_db(self):app.get('
        response = self./test_db')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        try:
            self.assertEqual(response.json['message'], 'Connection to the database successful')
        except KeyError:
            print("Received unexpected response: ", response.json)
            raise


if __name__ == '__main__':
    unittest.main()
