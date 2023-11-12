import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import votation_bp
from .models import Votation
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@votation_bp.route("/votation")
@login_required
def index():
    logger.info('Access votation index')

    return render_template("votation/index.html")


@votation_bp.route("/votation/all")
def all():
    all_items = Votation.query.all()
    return render_template("votation/list.html", all_items=all_items)


@votation_bp.route("/votation/view/<int:id>")
def view(id):
    votation = Votation.query.get_or_404(id)
    return render_template("votation/view.html", votation=votation)


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
