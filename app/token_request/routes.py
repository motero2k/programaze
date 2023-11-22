import logging
from app import get_authenticated_user_profile
from app.auth.models import User
from app.config.role_access_manager import Role_access
from app.token_request.forms import Token_Request_Form
from flask import render_template, request, jsonify, redirect, flash, url_for
from flask_login import login_required
from . import token_request_bp
from .models import Token_request, Token_state

from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@token_request_bp.route("/token_request")
@login_required
def index():
    logger.info('Access token_request index')

    return render_template("token_request/index.html")


@token_request_bp.route("/token_request/all")
@login_required
def all():
    # Obtener el valor del parámetro de consulta 'state'
    state = request.args.get('state', None)
    
    if state:
        # Lógica para mostrar propuestas filtradas por estado
        all_items = Token_request.query.filter_by(token_state = state).all()
    else:
        # Lógica para mostrar todas las propuestas sin filtrar por estado
        all_items = Token_request.query.all()
    data_collection = [{
        'id': token_request.id,
        'user_id': token_request.user_id,
        'Usuario': User.get_by_id(token_request.user_id).name(),
        'Descripción': token_request.description,
        'nº token': token_request.num_token,
        'Estado' : token_request.token_state.value
        
    } for token_request in all_items]
    return render_template("token_request/list.html", all_items=data_collection, state=state)
 

@token_request_bp.route("/token_request/view/<int:id>")
@login_required
def view(id):
    if Role_access.user_not_allowed("token_request","public"):
        return Role_access.not_allowed_get_previous_page("token_request","public")
    token_request = Token_request.query.get_or_404(id)

    token_request_data = {
        'id': token_request.id,
        'user_id': token_request.user_id,
        'username': User.get_by_id(token_request.user_id).name(),
        'description': token_request.description,
        'num_token': token_request.num_token,
        'state' : token_request.token_state.value
        
    } 
    return render_template("token_request/view.html", token_request=token_request_data)





@token_request_bp.route("/token_request/create", methods=["GET","POST"])
def create():
    if Role_access.user_not_allowed("token_request","public"):
        return Role_access.not_allowed_get_previous_page("token_request","public")
    form = Token_Request_Form()
  
    if request.method == 'POST' and form.validate_on_submit():
        #show operation not succeded in flash message

        num_token = form.num_token.data
        description = form.description.data.strip()
        profile = get_authenticated_user_profile()
        user_id = profile.user.id

        data_collection = Token_request.query.filter_by(user_id=user_id,token_state= Token_state.PENDING_OF_ACEPTATION).all()
        if(len(data_collection)>0 ):
            
            flash('No se puede pedir más de una solicitud', 'danger')
            return render_template("token_request/create.html",form=form)
        if (num_token > 3):
            flash("No se puede pedir más de 3 tokens","danger")
            return render_template("token_request/create.html",form=form)
        token_request = Token_request(num_token=num_token,description=description,user_id=user_id,token_state=Token_state.PENDING_OF_ACEPTATION)

        token_request.save()
        flash("Solicitud creada","success")
        return redirect("/")
    else:
        
        return render_template("token_request/create.html",form=form)
    
@token_request_bp.route("/token_request/view/<int:id>/accept")
def accept(id):
    if Role_access.user_not_allowed("token_request","accept"):
        return Role_access.not_allowed_get_previous_page("token_request","accept")
    token_request = Token_request.query.get_or_404(id)
    token_request.token_state = Token_state.ACCEPTED

    token_request.save()
    flash('La solicitud de token se ha aceptado', 'success')
    return redirect("/token_request/all")

@token_request_bp.route("/token_request/view/<int:id>/reject")
def reject(id):
    if Role_access.user_not_allowed("token_request","reject"):
        return Role_access.not_allowed_get_previous_page("token_request","reject")
    token_request = Token_request.query.get_or_404(id)
    token_request.token_state = Token_state.REJECTED
    token_request.save()
    flash('La solicitud de token se ha rechazado', 'success')
    return redirect("/token_request/all")
