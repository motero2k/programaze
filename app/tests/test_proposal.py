import unittest

from app import get_test_client,app
from app import db,create_app
from app.auth.models import User
from app.proposal.models import Proposal,ProposalType,State
from app.innosoft_day.models import Innosoft_day
from flask_login import current_user, login_user, logout_user,LoginManager, UserMixin,FlaskLoginClient
from flask import Flask

#MAGIC NUMBERS FOR TESTING -----------------------------
INNOSOFT_DAY_ID_WITH_PROPOSALS=2

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
def url_get_all_proposals(innosoft_id):
    return "/proposal/all/"+str(innosoft_id)
    
def url_get_all_proposals_by_state(innosoft_id,state):
    return "/proposal/all/"+str(innosoft_id)+"/filter_by_state/"+state.name


#SUIT FOR TEST
innosoft_day_test= None
proposal_test1=None
proposal_test2=None
proposal_test3=None
proposal_test4=None
proposal_test5=None

class ProposalTestCase(unittest.TestCase):
    
    
    def setUp(self):
        app.config['TESTING']=True
        self.client=app.test_client()
        innosoft_day_test=Innosoft_day(description="Jornada 2199/2200"
                                       , subject="Inteligencia Artificial", year=2200)
        db.session.add(innosoft_day_test)
        db.session.commit()
        
        proposal_test1 = Proposal(description="TEST 1", subject="Charla medioambiente", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ADMISION, innosoft_day_id=innosoft_day_test.id)
        proposal_test2 = Proposal(description="TEST 2", subject="Charla IA en la medicina", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day_test.id)
        proposal_test3 = Proposal(description="TEST 3", subject="Concurso Imagenes Ia", proposal_type=ProposalType.ACTIVITY, state=State.ON_PREPARATION, innosoft_day_id=innosoft_day_test.id)
        proposal_test4 = Proposal(description="TEST 4", subject="Stand de Sostenibilidad", proposal_type=ProposalType.STAND, state=State.CONFIRMATED, innosoft_day_id=innosoft_day_test.id)
        proposal_test5 = Proposal(description="TEST 5", subject="Charla de Emprendedores", proposal_type=ProposalType.TALK, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day_test.id)
        proposal_test6 = Proposal(description="TEST 6", subject="Kahoot IA", proposal_type=ProposalType.ACTIVITY, state=State.PENDING_OF_ACEPTATION, innosoft_day_id=innosoft_day_test.id)
        

    
    def tearDown(self):
        pass

    
    def test_get_proposals_of_innosoft_day(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            response=self.client.get(url_get_all_proposals(INNOSOFT_DAY_ID_WITH_PROPOSALS))
            l=Proposal.query.filter_by(innosoft_day_id=INNOSOFT_DAY_ID_WITH_PROPOSALS).all()
            self.assertTrue(len(l)>0)
            self.assertEqual(response.status_code, 200)
            real_data=response.get_json()
            print(real_data)
            self.assertTrue(len(real_data)==len(l))
            for data in response.get_json():
                print(data)
                self.assertTrue(data['innosoft_day_id']==INNOSOFT_DAY_ID_WITH_PROPOSALS)
    
    
    def test_get_proposals_of_innosoft_day_and_filtered_by_state(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            #NO DEBERÍA SER UN GET
            response=self.client.get(url_get_all_proposals_by_state(INNOSOFT_DAY_ID_WITH_PROPOSALS,State.PENDING_OF_ADMISION))
            l= Proposal.query.filter_by(innosoft_day_id=INNOSOFT_DAY_ID_WITH_PROPOSALS,state= State.PENDING_OF_ADMISION).all()
            self.assertTrue(len(l)>0)
            print(l)
            self.assertEqual(response.status_code, 200)
            real_data=response.get_json()
            print(real_data)
            self.assertTrue(len(real_data)==len(l))
            for data in response.get_json():
                print(data)
                self.assertTrue(data['innosoft_day_id']==INNOSOFT_DAY_ID_WITH_PROPOSALS)
                self.assertEqual(data['estado'],State.PENDING_OF_ADMISION.value)
    
    def test_reject_proposal_positive(self):
        self.client.post("/login",data={
            "username":"profesor1",
            "password":"profesor1"
        },follow_redirects=True)
        with self.client.application.app_context():
            #CAMBIAR ESTADO AL MERGEAR
            rejected_proposal=Proposal.query.filter_by(state=State.PENDING_OF_ADMISION).first()
            id=rejected_proposal.id
            print(id)
            self.assertEqual(rejected_proposal.state,State.PENDING_OF_ADMISION)
            response=self.client.get("/proposal/view/"+str(id)+"/reject",follow_redirects=True)
            #assert response.status_code == 201
            same_proposal=Proposal.query.get_or_404(id)
            self.assertEqual(same_proposal.state,State.REJECTED)
            


if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
    