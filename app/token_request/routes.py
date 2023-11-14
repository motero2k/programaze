import logging
from app import get_authenticated_user_profile
from app.auth.models import User
from app.config.role_access_manager import Role_access
from app.token_request.forms import Token_Request_Form
from flask import render_template, request, jsonify, redirect, flash
from flask_login import login_required
from . import token_request_bp
from .models import Token_request, TokenState

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
    all_items = Token_request.query.filter_by(token_state = TokenState.PENDING_OF_ACEPTATION).all()
    data_collection = [{
        'id': token_request.id,
        'user_id': token_request.user_id,
        'Usuario': User.get_by_id(token_request.user_id).name(),
        'Descripción': token_request.description,
        'nº token': token_request.num_token,
        'Estado' : token_request.token_state.value
        
    } for token_request in all_items]
    return render_template("token_request/list.html", all_items=data_collection)


@token_request_bp.route("/token_request/view/<int:id>")
@login_required
def view(id):
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

@token_request_bp.route("/token_request/view/<int:id>/accept")
@login_required
def accept(id):
    if Role_access.user_not_allowed("token_request","accept"):
        return Role_access.not_allowed_get_previous_page("token_request","accept")

    flash("aceptado","success")
    return Role_access.get_previous_page()


@token_request_bp.route("/token_request/view/<int:id>/reject")
@login_required
def reject(id):
    pass


@token_request_bp.route("/token_request/edit/<int:id>")
def edit(id):
    token_request = Token_request.query.get_or_404(id)
    return render_template("token_request/edit.html", token_request=token_request)

@token_request_bp.route("/token_request/create", methods=["GET","POST"])
def create():
    form = Token_Request_Form()
    if request.method == 'POST' and form.validate_on_submit():
        
        num_token = form.num_token.data
        description = form.description.data.strip()
        profile = get_authenticated_user_profile()
        user_id = profile.user.id

        data_collection = Token_request.query.filter_by(user_id=user_id,token_state= TokenState.PENDING_OF_ACEPTATION).all()
        if(len(data_collection)>0 ):
            flash('No se pueden pedir más de una solicitud', 'danger')
           
        if (num_token > 3):
            flash("No se pueden pedir más de 3 tokens","danger")
            return redirect("/token_request/create")
        token_request = Token_request(num_token=num_token,description=description,user_id=user_id,token_state=TokenState.PENDING_OF_ACEPTATION)

        token_request.save()
        return redirect("/")
    else:
        return render_template("token_request/create.html",form=form)



@token_request_bp.route("/token_request/delete", methods=["POST"])
def delete():
    token_request_id = request.form.get("id")

    if not token_request_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(Token_request, token_request_id)

    return jsonify(result), status_code


@token_request_bp.route("/token_request/delete/bulk", methods=["POST"])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(Token_request, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No token_requests found with provided IDs"}), status_code

    return jsonify(result), status_code
