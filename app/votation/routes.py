import logging
from app import get_authenticated_user_profile
from app.vote.models import Vote
from flask import render_template, request, jsonify
from flask_login import login_required
from . import votation_bp
from .models import Votation
from ..proposal.models import Proposal,State
from ..auth.models import User
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@votation_bp.route("/votation")
@login_required
def index():
    logger.info('Access votation index')

    return render_template("votation/index.html")


@votation_bp.route("/innosoft_days/<int:id>/votations/")
def all(id):    
    data_collection = Votation.query.join(Proposal).filter(Proposal.innosoft_day_id == id).all()
        # Obtener el valor del parámetro de consulta 'state'
    state = request.args.get('state', None)
    
    if state:
        # Lógica para mostrar propuestas filtradas por estado
        data_collection = Votation.query.join(Proposal).filter(Proposal.innosoft_day_id == id,Votation.state_votation==state).all()
    else:
        # Lógica para mostrar todas las propuestas sin filtrar por estado
        data_collection = Votation.query.join(Proposal).filter(Proposal.innosoft_day_id == id).all()
    prepared_data = [
        {'id': votation.id,
        'Tema': Proposal.query.get_or_404(votation.proposal_id).subject,
        'descripcion': Proposal.query.get_or_404(votation.proposal_id).description,
        'tipo de propuesta': Proposal.query.get_or_404(votation.proposal_id).proposal_type.value,
        'estado de la votacion': votation.state_votation.value,
        'usuario': User.query.get_or_404(Proposal.query.get_or_404(votation.proposal_id).user_id).username 
    } for votation in data_collection]
    return render_template("votation/list.html", all_items=prepared_data,innosoft_day_id= id,state=state)


@votation_bp.route("/votation/view/<int:id>")
def view(id):
    votation = Votation.query.get_or_404(id)
    votes_list = Vote.query.filter_by(votation_id = votation.id)
    votes = [
        {'id': vote.id,
        'username': User.query.get_or_404(vote.user_id).username,
        'description':vote.description
       
    } for vote in votes_list]  

        
    votation = {
        'id': votation.id,
        'theme': Proposal.query.get_or_404(votation.proposal_id).subject,
        'description': Proposal.query.get_or_404(votation.proposal_id).description,
        'type': Proposal.query.get_or_404(votation.proposal_id).proposal_type.value,
        'state': votation.state_votation.value,
        'user': User.query.get_or_404(Proposal.query.get_or_404(votation.proposal_id).user_id).username,
        "votes": votes
    } 
    profile = get_authenticated_user_profile()
    user_id = profile.user.id
    data_collection = Vote.query.filter_by(user_id=user_id,votation_id=id).all()
    can_vote = len(data_collection)==0 
    return render_template("votation/view.html", votation=votation,can_vote=can_vote)


@votation_bp.route("/votation/edit/<int:id>")
def edit(id):
    votation = Votation.query.get_or_404(id)
    return render_template("votation/edit.html", votation=votation)


@votation_bp.route("/votation/delete", methods=["POST"])
def delete():
    votation_id = request.form.get("id")

    if not votation_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(Votation, votation_id)

    return jsonify(result), status_code


@votation_bp.route("/votation/delete/bulk", methods=["POST"])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(Votation, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No votations found with provided IDs"}), status_code

    return jsonify(result), status_code
