import unittest

from app import get_test_client,app
from app import db,create_app
from app.auth.models import User
from app.proposal.models import Proposal,ProposalType,State
from app.innosoft_day.models import Innosoft_day
from flask_login import current_user, login_user, logout_user,LoginManager, UserMixin,FlaskLoginClient
from flask import Flask
from ..votation.models import Votation,StateVotation

#MAGIC NUMBERS FOR TESTING -----------------------------
INNOSOFT_DAY_ID_WITH_PROPOSALS=2
ALUMNO_1_ID=4

#---------------------------------------------------

#TIPS PARA CREAR TEST EN EVIDENTIA:
#1º Como las rutas originales de la app no devuelven respuestas, tienes que hacer TU
# la respuesta desde el routes de test
#2º El objetivo es hacer que devuelva una respuesta json, al hacer esto ya puedes leer
#los datos que te devuelve en los test
#3º la respuesta debería quedar asi: return jsonif({'key': datos})
#4º Al hacer esto, ya aparecera el contenido que querias en el response.get_json()

#OJO, response.json NO SIRVE, tienes que hacerlo por get_json()
#y el nombre en la ruta de test y del test debe ser la misma





#CUANDO SE MERGE CON DEVELOP, SOLO HABRÍA QUE ACTUALIZAR LAS DIRECCIONES DE LOS MÉTODOS
#cuyas direcciones hayan cambiado (también hay que cambiarlas en routes)
#OJO, PON DIRECCIONES DISTINTAS A LAS REALES, PORQUE SI NO LAS DIRECCIONES DE TEST SUSTITUYEN
#A LAS REALES
def url_get_all_proposals(innosoft_id):
    return "/test/innosoft_days/"+str(innosoft_id)+"/proposals"
    
def url_get_all_proposals_by_state(innosoft_id,state):
    return "/test/innosoft_days/"+str(innosoft_id)+"/proposals?state="+str(state.name)


#SUIT FOR TEST
class ProposalTestCase(unittest.TestCase):
    
    
    
    def setUp(self):
        app.config['TESTING']=True
        self.client=app.test_client()
        with self.client.application.app_context():
            global innosoft_day_test_id
            innosoft_day_test=Innosoft_day(description="Jornada 2199/2200"
                                       , subject="Inteligencia Artificial", year=2200)
            db.session.add(innosoft_day_test)
            db.session.commit()
            innosoft_day_test_id=innosoft_day_test.id
            
            #Con esto creas variables globales de los id, NO HAGAS VARIABLES GLOBALES
            #DE LOS PROPIOS SUIT TEST
            global proposal_test1_id
            global proposal_test2_id
            global proposal_test3_id
            global proposal_test4_id
            global proposal_test5_id
            proposal_test1 = Proposal(description="TEST 1", subject="TEST 1", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ADMISION, innosoft_day_id=innosoft_day_test.id, user_id=ALUMNO_1_ID)
            proposal_test2 = Proposal(description="TEST 2", subject="TEST 2", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day_test.id, user_id=ALUMNO_1_ID)
            proposal_test3 = Proposal(description="TEST 3", subject="TEST 3", proposal_type=ProposalType.ACTIVITY, state=State.ON_PREPARATION, innosoft_day_id=innosoft_day_test.id, user_id=ALUMNO_1_ID)
            proposal_test4 = Proposal(description="TEST 4", subject="TEST 4", proposal_type=ProposalType.STAND, state=State.CONFIRMATED, innosoft_day_id=innosoft_day_test.id, user_id=ALUMNO_1_ID)
            proposal_test5 = Proposal(description="TEST 5", subject="TEST 5", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day_test.id, user_id=ALUMNO_1_ID)
        
            db.session.add(proposal_test1)
            db.session.add(proposal_test2)
            db.session.add(proposal_test3)
            db.session.add(proposal_test4)
            db.session.add(proposal_test5)
            db.session.commit()
            proposal_test1_id=proposal_test1.id
            proposal_test2_id=proposal_test2.id
            proposal_test3_id=proposal_test3.id
            proposal_test4_id=proposal_test4.id
            proposal_test5_id=proposal_test5.id
        

    
    def tearDown(self):
        with self.client.application.app_context():
            db.session.delete(db.session.get(Proposal,proposal_test1_id))
            db.session.delete(db.session.get(Proposal,proposal_test2_id))
            db.session.delete(db.session.get(Proposal,proposal_test3_id))
            db.session.delete(db.session.get(Proposal,proposal_test4_id))
            db.session.delete(db.session.get(Proposal,proposal_test5_id))
            db.session.commit()
            self.assertTrue(db.session.get(Proposal,proposal_test1_id)==None)
        
            db.session.delete(db.session.get(Innosoft_day,innosoft_day_test_id))
            db.session.commit()
            db.session.close()
        

    """
    def test_get_proposals_of_innosoft_day(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            print(innosoft_day_test_id)
            response=self.client.get(url_get_all_proposals(innosoft_day_test_id))
            l=Proposal.query.filter_by(innosoft_day_id=innosoft_day_test_id).all()
            self.assertTrue(len(l)>0)
            self.assertEqual(response.status_code, 200)
            real_data=response.get_json()
            print(real_data)
            self.assertTrue(len(real_data)==len(l))
            for data in response.get_json():
                print(data)
                self.assertTrue(data['innosoft_day_id']==innosoft_day_test_id)
    """
    """
    def test_get_proposals_of_innosoft_day_and_filtered_by_state(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            #NO DEBERÍA SER UN GET
            print(innosoft_day_test_id)
            print(State.PENDING_OF_ADMISION.name)
            response=self.client.get(url_get_all_proposals_by_state(innosoft_id=innosoft_day_test_id,state=State.PENDING_OF_ADMISION))
            l= Proposal.query.filter_by(innosoft_day_id=innosoft_day_test_id,state= State.PENDING_OF_ADMISION).all()
            self.assertTrue(len(l)>0)
            print(l)
            self.assertEqual(response.status_code, 200)
            real_data=response.get_json()
            print(real_data)
            self.assertTrue(len(real_data)==len(l))
            for data in response.get_json():
                print(data)
                self.assertTrue(data['innosoft_day_id']==innosoft_day_test_id)
                self.assertEqual(data['estado'],State.PENDING_OF_ADMISION.value)
    """
    """ 
    test_accept_proposal_positive(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            #CAMBIAR ESTADO AL MERGEAR
            #/proposal/view/<int:id>/accept
            pending_of_admision_proposal=Proposal.query.get_or_404(proposal_test1_id)
            self.assertEqual(pending_of_admision_proposal.state,State.PENDING_OF_ADMISION)
            v=Votation.query.filter_by(proposal_id=proposal_test1_id).first()
            self.assertEqual(v,None)
            response=self.client.get("/proposal/view/"+str(proposal_test1_id)+"/accept",follow_redirects=True)
            assert response.status_code == 200
            same_proposal=Proposal.query.get_or_404(proposal_test1_id)
            self.assertEqual(same_proposal.state,State.PENDING_OF_ACEPTATION)
            votation=Votation.query.filter_by(proposal_id=proposal_test1_id).first()
            self.assertNotEqual(votation,None)
            #SI AL HACER UN CAMBIO SE CREA UNA NUEVA ENTIDAD, BORRALA DESDE EL PROPIO TEST,
            #NO DESDE EL TEARDOWN
            db.session.delete(votation)
            db.session.commit()
    """
    """
    def test_reject_proposal_positive(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            pending_of_admision_proposal=Proposal.query.get_or_404(proposal_test1_id)
            self.assertEqual(pending_of_admision_proposal.state,State.PENDING_OF_ADMISION)
            response=self.client.get("/proposal/view/"+str(proposal_test1_id)+"/reject",follow_redirects=True)
            assert response.status_code == 200
            same_proposal=Proposal.query.get_or_404(proposal_test1_id)
            self.assertEqual(same_proposal.state,State.REJECTED)   
    """
    """
    def test_confirm_proposal_positive(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            on_preparation_proposal=Proposal.query.get_or_404(proposal_test3_id)
            self.assertEqual(on_preparation_proposal.state,State.ON_PREPARATION)
            response=self.client.get("/proposal/view/"+str(proposal_test3_id)+"/confirm",follow_redirects=True)
            assert response.status_code == 200
            same_proposal=Proposal.query.get_or_404(proposal_test3_id)
            self.assertEqual(same_proposal.state,State.CONFIRMATED)   
    """

if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
    