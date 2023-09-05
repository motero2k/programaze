import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import evidence_bp
from .models import Evidence
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@evidence_bp.route("/evidence")
@login_required
def index():
    logger.info('Access evidence index')

    return render_template("evidence/index.html")


@evidence_bp.route("/evidence/all")
def all():
    all_items = Evidence.query.all()
    return render_template("evidence/list.html", all_items=all_items)


@evidence_bp.route("/evidence/view/<int:id>")
def view(id):
    evidence = Evidence.query.get_or_404(id)
    return render_template("evidence/view.html", evidence=evidence)


@evidence_bp.route("/evidence/edit/<int:id>")
def edit(id):
    evidence = Evidence.query.get_or_404(id)
    return render_template("evidence/edit.html", evidence=evidence)


@evidence_bp.route("/evidence/delete", methods=["POST"])
def delete():
    evidence_id = request.form.get("id")

    if not evidence_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(Evidence, evidence_id)

    return jsonify(result), status_code


@evidence_bp.route("/evidence/delete/bulk", methods=["POST"])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(Evidence, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No evidences found with provided IDs"}), status_code

    return jsonify(result), status_code
