import unittest

from app import app
from app import db
from app.votation.models import Votation,StateVotation
from app.proposal.models import Proposal

def url_get_all_votations():
    return "/test/votations"

class VotationTestCase(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING']=True
        self.client=app.test_client()

        with self.client.application.app_context():
            saved_proposal = Proposal.query.first()
            global votation_test_id
            votation_test=Votation(state_votation=StateVotation.ACCEPTED, proposal_id=saved_proposal.id)
            db.session.add(votation_test)
            db.session.commit()
            votation_test_id=votation_test.id
    
    def tearDown(self):
        with self.client.application.app_context():        
            db.session.delete(db.session.get(Votation,votation_test_id))
            db.session.commit()
            db.session.close()
    
    def test_get_votations(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)

        with self.client.application.app_context():
            # Obtenemos la votación
            saved_votation = Votation.query.filter_by(id=votation_test_id).first()

            # Comprobamos si se ha obtenido correctamente
            self.assertIsNotNone(saved_votation)
            self.assertEqual(saved_votation.state_votation, StateVotation.ACCEPTED)

    def test_update_votation(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        
        with self.client.application.app_context():
             # Obtenemos la votación y actualizamos su estado
             saved_votation = Votation.query.filter_by(id=votation_test_id).first()
             saved_votation.state_votation = StateVotation.IN_PROGRESS

             # Volvemos a hacer la consulta a la base de datos y comprobamos si la información se ha actualizado correctamente
             saved_votation = Votation.query.filter_by(id=votation_test_id).first()
             self.assertEqual(saved_votation.state_votation, StateVotation.IN_PROGRESS)

    def test_create_and_delete_votation(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        
        with self.client.application.app_context():
             # Creamos la votación y la añadimos a la base de datos
             saved_proposal = Proposal.query.first()
             votation_test2=Votation(state_votation=StateVotation.REJECTED, proposal_id=saved_proposal.id)
             db.session.add(votation_test2)
             db.session.commit()
             
             # Obtenemos la votación
             votation_test_id2=votation_test2.id
             saved_votation = Votation.query.filter_by(id=votation_test_id2).first()

             # Comprobamos si se ha creado y almacenado correctamente
             self.assertIsNotNone(saved_votation)
             self.assertEqual(saved_votation.state_votation, StateVotation.REJECTED)

             # Eliminamos la votación de la base de datos
             db.session.delete(db.session.get(Votation,votation_test_id2))
             db.session.commit()

             # Comprobamos si se ha eliminado correctamente
             saved_votation = Votation.query.filter_by(id=votation_test_id2).first()
             self.assertIsNone(saved_votation)

if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
    