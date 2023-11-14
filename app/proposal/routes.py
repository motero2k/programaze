import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import proposal_bp
from .models import Proposal
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@proposal_bp.route("/innosoft_day/<int:id>/proposal")
@login_required 
def index():
    logger.info('Access proposal index')

    return render_template("proposal/index.html")


@proposal_bp.route("/innosoft_days/<int:id>/proposals")
def all(id): 
    
    data_collection = Proposal.query.filter_by(innosoft_day_id=id).all()
    prepared_data = [{
        'id' : proposal.id,
        'descripcion': proposal.description,
        'tema': proposal.subject,
        'tipo de propuesta': proposal.proposal_type.value,  # Usar el valor en cadena
        'estado': proposal.state.value,  # Usar el valor en cadena
        'innosoft_day_id': proposal.innosoft_day_id
        
        

    } for proposal in data_collection]


    return render_template("proposal/list.html", all_items=prepared_data,innosoft_day_id=id)

# Ruta para filtrar por estado
@proposal_bp.route('/innosoft_days/<int:id>/proposals?state=<state>')
def proposal_filter_by_state(id,state):
    # Lógica para mostrar propuestas filtradas por estado
    data_collection = Proposal.query.filter_by(innosoft_day_id=id,state= state).all()
    prepared_data = [{
        'id' : proposal.id,
        'tema': proposal.subject,
        'tipo de propuesta': proposal.proposal_type.value,  # Usar el valor en cadena
        'estado': proposal.state.value,  # Usar el valor en cadena
        'innosoft_day_id': proposal.innosoft_day_id
    } for proposal in data_collection]


    return render_template("proposal/list.html", all_items=prepared_data,innosoft_day_id=id)

@proposal_bp.route("/proposal/view/<int:id>")
def view(id):
    proposal = Proposal.query.get_or_404(id)
    return render_template("proposal/view.html", proposal=proposal)


@proposal_bp.route("/proposal/edit/<int:id>")
def edit(id):
    proposal = Proposal.query.get_or_404(id)
    return render_template("proposal/edit.html", proposal=proposal)


@proposal_bp.route("/proposal/delete", methods=["POST"])
def delete():
    proposal_id = request.form.get("id")

    if not proposal_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(Proposal, proposal_id)

    return jsonify(result), status_code


@proposal_bp.route("/proposal/delete/bulk", methods=["POST"])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(Proposal, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No proposals found with provided IDs"}), status_code

    return jsonify(result), status_code
