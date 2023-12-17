import os

from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app import db
from app.proposal.models import Proposal,ProposalType
from app.auth.models import User

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/test')
def test_route():
    return 'Test route'


@test_routes.route('/env')
def show_env():
    env_vars = {key: value for key, value in os.environ.items()}
    return jsonify(env_vars)

#-------------RUTAS DE TEST DE PROPOSAL-----------------------------------

@test_routes.route("/test/innosoft_days/<int:id>/proposals")
def test_get_proposals_from_innosoft_day(id):
    state = request.args.get('state', None)

    if state:
        # Lógica para mostrar propuestas filtradas por estado
        data_collection = Proposal.query.filter_by(innosoft_day_id=id, state=state).all()
    else:
        # Lógica para mostrar todas las propuestas sin filtrar por estado
        data_collection = Proposal.query.filter_by(innosoft_day_id=id).all()

    prepared_data = [{
        'id': proposal.id,
        'descripcion': proposal.description,
        'tema': proposal.subject,
        'tipo de propuesta': proposal.proposal_type.value,
        'estado': proposal.state.value,
        'innosoft_day_id': proposal.innosoft_day_id,
        'usuario': User.query.get_or_404(proposal.user_id).username
    } for proposal in data_collection]
    return jsonify(prepared_data)


