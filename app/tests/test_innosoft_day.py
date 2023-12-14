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
            # Obtenemos la jornada
            saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()

            # Comprobamos si se ha obtenido correctamente
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
             # Obtenemos la jornada y actualizamos su tema y descripción
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()
             saved_innosoft_day.description = "Descripción actualizada"
             saved_innosoft_day.subject = "Tema actualizado"

             # Volvemos a hacer la consulta a la base de datos y comprobamos si la información se ha actualizado correctamente
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id).first()
             self.assertEqual(saved_innosoft_day.description, "Descripción actualizada")
             self.assertEqual(saved_innosoft_day.subject, "Tema actualizado")
             self.assertEqual(saved_innosoft_day.year, 2200)

    '''
    def test_create_and_delete_innosoft_day(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        
        with self.client.application.app_context():
             # Creamos la jornada y la añadimos a la base de datos
             innosoft_day_test2=Innosoft_day(description="Jornada 2299/2300", subject="Ciberseguridad", year=2300)
             db.session.add(innosoft_day_test2)
             db.session.commit()
             
             # Obtenemos la jornada
             innosoft_day_test_id2=innosoft_day_test2.id
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id2).first()

             # Comprobamos si se ha creado y almacenado correctamente
             self.assertIsNotNone(saved_innosoft_day)
             self.assertEqual(saved_innosoft_day.description, "Jornada 2299/2300")
             self.assertEqual(saved_innosoft_day.subject, "Ciberseguridad")
             self.assertEqual(saved_innosoft_day.year, 2300)

             # Eliminamos la jornada de la base de datos
             db.session.delete(db.session.get(Innosoft_day,innosoft_day_test_id2))
             db.session.commit()

             # Comprobamos si se ha eliminado correctamente
             saved_innosoft_day = Innosoft_day.query.filter_by(id=innosoft_day_test_id2).first()
             self.assertIsNone(saved_innosoft_day)
            '''
if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
    