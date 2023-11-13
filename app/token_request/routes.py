import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import token_request_bp
from .models import Token_request
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
