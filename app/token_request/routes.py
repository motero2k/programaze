import logging
from app import get_authenticated_user_profile
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
def all():
    all_items = Token_request.query.all()
    return render_template("token_request/list.html", all_items=all_items)


@token_request_bp.route("/token_request/view/<int:id>")
def view(id):
    token_request = Token_request.query.get_or_404(id)
    return render_template("token_request/view.html", token_request=token_request)


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
