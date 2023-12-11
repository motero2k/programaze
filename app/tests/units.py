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
    """
    def test_access_restricted_url_with_correct_role(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        response=self.client.get("/innosoft_days/1/proposals")
        self.assertEqual(response.status_code, 200)
    """
    def test_show_env(self):
        response = self.client.get('/env')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    """
    def test_test_db(self):
        response = self.client.get('/test_db')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        try:
            self.assertEqual(response.json['message'], 'Connection to the database successful')
        except KeyError:
            print("Received unexpected response: ", response.json)
            raise
    """

if __name__ == '__main__':
    unittest.main()
