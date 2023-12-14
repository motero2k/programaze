import unittest

from app import app
from app import db
from app.innosoft_day.models import Innosoft_day

def url_get_all_innosoft_days():
    return "/test/innosoft_days"

class InnosoftDayTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING']=True
        self.client=app.test_client()

        with self.client.application.app_context():
            global innosoft_day_test_id
            innosoft_day_test=Innosoft_day(description="Jornada 2199/2200", subject="Inteligencia Artificial", year=2200)
            db.session.add(innosoft_day_test)
            db.session.commit()
            innosoft_day_test_id=innosoft_day_test.id
    
    def tearDown(self):
        with self.client.application.app_context():        
            db.session.delete(db.session.get(Innosoft_day,innosoft_day_test_id))
            db.session.commit()
            db.session.close()
    
    def test_get_innosoft_day(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)

        with self.client.application.app_context():
            saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()

            self.assertIsNotNone(saved_innosoft_day)
            self.assertEqual(saved_innosoft_day.description, "Jornada 2199/2200")
            self.assertEqual(saved_innosoft_day.subject, "Inteligencia Artificial")
            self.assertEqual(saved_innosoft_day.year, 2200)

    def test_update_innosoft_day(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        
        with self.client.application.app_context():
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()
             saved_innosoft_day.description = "Descripción actualizada"
             saved_innosoft_day.subject = "Tema actualizado"
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()

             self.assertEqual(saved_innosoft_day.description, "Descripción actualizada")
             self.assertEqual(saved_innosoft_day.subject, "Tema actualizado")
             self.assertEqual(saved_innosoft_day.year, 2200)

if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
    