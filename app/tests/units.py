import unittest

from app import get_test_client,app
from app import db,create_app
from app.auth.models import User
from flask_login import current_user, login_user, logout_user,LoginManager, UserMixin,FlaskLoginClient
from flask import Flask



class FlaskAppTestCase(unittest.TestCase):
    
    

    def setUp(self):
        app.config['TESTING']=True
        self.client=app.test_client()

    
    def tearDown(self):
        pass

    #ACTUALIZAR CUANDO SE MERGEE LA RAMA

    def test_show_env(self):
        response = self.client.get('/env')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
