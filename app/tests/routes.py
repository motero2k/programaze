import os

from flask import Blueprint, jsonify
from sqlalchemy import text
from app import db
from app.proposal.models import Proposal,ProposalType

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/test')
def test_route():
    return 'Test route'


@test_routes.route('/env')
def show_env():
    env_vars = {key: value for key, value in os.environ.items()}
    return jsonify(env_vars)


@test_routes.route('/test_db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return jsonify({'message': 'Connection to the database successful'})
    except Exception as e:
        return jsonify({'error': str(e)})

#-------------RUTAS DE TEST DE PROPOSAL-----------------------------------

@test_routes.route('/proposal/all/<int:id>')
def test_get_proposals_from_innosoft_day(id):
    data_collection = Proposal.query.filter_by(innosoft_day_id=id).all()
    prepared_data = [{
        'id' : proposal.id,
        'descripcion': proposal.description,
        'tema': proposal.subject,
        'tipo de propuesta': proposal.proposal_type.value,  # Usar el valor en cadena
        'estado': proposal.state.value,  # Usar el valor en cadena
        'innosoft_day_id': proposal.innosoft_day_id
    } for proposal in data_collection]
    return jsonify(prepared_data)

@test_routes.route('/proposal/all/<int:id>/filter_by_state/<state>')
def test_get_proposals_of_innosoft_day_and_filtered_by_state(id,state):
    data_collection = Proposal.query.filter_by(innosoft_day_id=id,state= state).all()
    prepared_data = [{
        'id' : proposal.id,
        'tema': proposal.subject,
        'tipo de propuesta': proposal.proposal_type.value,  # Usar el valor en cadena
        'estado': proposal.state.value,  # Usar el valor en cadena
        'innosoft_day_id': proposal.innosoft_day_id
    } for proposal in data_collection]
    return jsonify(prepared_data)
