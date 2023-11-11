import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import innosoft_day_bp
from .models import Innosoft_day
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@innosoft_day_bp.route("/innosoft_day")
@login_required
def index():
    logger.info('Access innosoft_day index')

    return render_template("innosoft_day/index.html")


@innosoft_day_bp.route("/innosoft_day/all")
def all():
    all_items = Innosoft_day.query.all()
    return render_template("innosoft_day/list.html", all_items=all_items)


@innosoft_day_bp.route("/innosoft_day/view/<int:id>")
def view(id):
    innosoft_day = Innosoft_day.query.get_or_404(id)
    return render_template("innosoft_day/view.html", innosoft_day=innosoft_day)


@innosoft_day_bp.route("/innosoft_day/edit/<int:id>")
def edit(id):
    innosoft_day = Innosoft_day.query.get_or_404(id)
    return render_template("innosoft_day/edit.html", innosoft_day=innosoft_day)


@innosoft_day_bp.route("/innosoft_day/delete", methods=["POST"])
def delete():
    innosoft_day_id = request.form.get("id")

    if not innosoft_day_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(Innosoft_day, innosoft_day_id)

    return jsonify(result), status_code


@innosoft_day_bp.route("/innosoft_day/delete/bulk", methods=["POST"])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(Innosoft_day, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No innosoft_days found with provided IDs"}), status_code

    return jsonify(result), status_code
