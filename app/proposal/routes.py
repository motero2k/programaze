import logging
from flask import render_template, request, jsonify,flash,redirect,url_for
from flask_login import login_required
from . import proposal_bp
from .models import Proposal,State
from ..votation.models import Votation,StateVotation

from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@proposal_bp.route("/proposal")
@login_required 
def index():
    logger.info('Access proposal index')

    return render_template("proposal/index.html")


@proposal_bp.route("/proposal/all/<int:id>")
def all(id): 
    #proposals = Proposal.query.all()
    data_collection = Proposal.query.filter_by(innosoft_day_id=id).all()
    prepared_data = [{
        'id' : proposal.id,
        'description': proposal.description,
        'subject': proposal.subject,
        'proposal_type': proposal.proposal_type.value,  # Usar el valor en cadena
        'state': proposal.state.value,  # Usar el valor en cadena
        'innosoft_day_id': proposal.innosoft_day_id
        
        

    } for proposal in data_collection]


    return render_template("proposal/list.html", all_items=prepared_data,innosoft_day_id=id)

# Ruta para filtrar por estado
@proposal_bp.route('/proposal/all/<int:id>/filter_by_state/<state>')
def proposal_filter_by_state(id,state):
    # Lógica para mostrar propuestas filtradas por estado
    data_collection = Proposal.query.filter_by(innosoft_day_id=id,state= state).all()
    prepared_data = [{
        'id' : proposal.id,
        'description': proposal.description,
        'subject': proposal.subject,
        'proposal_type': proposal.proposal_type.value,  # Usar el valor en cadena
        'state': proposal.state.value  # Usar el valor en cadena
    } for proposal in data_collection]


    return render_template("proposal/list.html", all_items=prepared_data,innosoft_day_id=id)

@proposal_bp.route("/proposal/view/<int:id>")
def view(id):
    proposal = Proposal.query.get_or_404(id)
    return render_template("proposal/view.html", proposal=proposal)

@proposal_bp.route("/proposal/view/<int:id>/reject")
def reject(id):
    proposal = Proposal.query.get_or_404(id)
    proposal.state = State.REJECTED
    proposal.save()
    flash('La propuesta se ha cancelado', 'danger')
    
    
    return redirect("/proposal/all/"+str(proposal.innosoft_day_id)+"/filter_by_state/REJECTED")

@proposal_bp.route("/proposal/view/<int:id>/accept")
def accept(id):
    proposal = Proposal.query.get_or_404(id)
    proposal.state=State.PENDING_OF_ADMISION
    proposal.save()
    flash('La propuesta se ha aceptado con éxito', 'success')
    votation = Votation(state_votation=StateVotation.IN_PROGRESS,proposal_id=proposal.id)
    votation.save()
   

    return redirect("/proposal/all/"+str(proposal.innosoft_day_id)+"/filter_by_state/PENDING_OF_ADMISION")


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
