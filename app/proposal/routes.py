import logging
from flask import render_template, request, jsonify, flash, redirect
from flask_login import login_required
from app import get_authenticated_user_profile

from app.config.role_access_manager import Role_access
from app.proposal.forms import Proposal_Form
from . import proposal_bp
from .models import Proposal,Proposal_State
from ..auth.models import User
from ..votation.models import Votation,StateVotation

from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)





@proposal_bp.route("/innosoft_days/<int:id>/proposals")
def all(id):
    # Obtener el valor del parámetro de consulta 'state'
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

    return render_template("proposal/list.html", all_items=prepared_data, innosoft_day_id=id, state=state)


@proposal_bp.route("/innosoft_days/<int:id>/proposal/create/", methods=["GET","POST"])
def create(id):
    
    if Role_access.user_not_allowed("proposal","public"):
        return Role_access.not_allowed_get_previous_page("proposal","public")
    form = Proposal_Form()
  
    if request.method == 'POST' and form.validate_on_submit():
        #show operation not succeded in flash message

        subject = form.subject.data.strip()
        description = form.description.data.strip()
        proposal_type = form.proposal_type.data

       
        profile = get_authenticated_user_profile()
        user_id = profile.user.id
        user = User.query.get_or_404(user_id)

     
        if user.token <= 0:
            
            flash('No se puede crear una solicitud de propuesta sin tokens', 'danger')
            return render_template("proposal/create.html",form=form,innosoft_day_id=id)
        
        proposal = Proposal()
        proposal.subject = subject
        proposal.description = description
        proposal.proposal_type = proposal_type
        proposal.innosoft_day_id = id
        proposal.state = Proposal_State.PENDING_OF_ADMISION
        proposal.user_id = user_id

        user.token -= 1
        proposal.save()
        user.save()

        

        proposal.save()
        flash("Solicitud de propuesta creada","success")
        return redirect("/innosoft_days/"+str(id)+"/proposals?state=PENDING_OF_ADMISION")
    else:
        
        return render_template("proposal/create.html",form=form,innosoft_day_id = id)

@proposal_bp.route("/proposal/view/<int:id>")
def view(id):
    proposal = Proposal.query.get_or_404(id)
    username = User.query.get_or_404(proposal.user_id).username
    return render_template("proposal/view.html", proposal=proposal, username=username)

@proposal_bp.route("/proposal/view/<int:id>/reject")
def reject(id):
    proposal = Proposal.query.get_or_404(id)
    votation = Votation.query.filter_by(proposal_id=proposal.id).first()

    if votation:
        votation.state_votation = StateVotation.REJECTED
        votation.save()

    proposal.state = Proposal_State.REJECTED
    proposal.save()
    flash('La propuesta se ha cancelado', 'success')
    return redirect("/innosoft_days/"+str(proposal.innosoft_day_id)+"/proposals?state=REJECTED")

@proposal_bp.route("/proposal/view/<int:id>/confirm")
def confirm(id):
    proposal = Proposal.query.get_or_404(id)
    proposal.state = Proposal_State.CONFIRMATED
    proposal.save()
    flash('La propuesta se ha confirmado', 'success')  
    return redirect("/innosoft_days/"+str(proposal.innosoft_day_id)+"/proposals?state=CONFIRMED")

@proposal_bp.route("/proposal/view/<int:id>/accept")
def accept(id):
    proposal = Proposal.query.get_or_404(id)
    proposal.state=Proposal_State.PENDING_OF_ACEPTATION
    proposal.save()
    flash('La propuesta se ha aceptado con éxito', 'success')
    votation = Votation(state_votation=StateVotation.IN_PROGRESS,proposal_id=proposal.id)
    votation.save()
    return redirect("/innosoft_days/"+str(proposal.innosoft_day_id)+"/proposals?state=PENDING_OF_ACEPTATION")


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
