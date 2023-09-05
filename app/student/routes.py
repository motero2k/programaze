import logging
from flask import render_template, jsonify, request
from flask_login import login_required
from . import student_bp
from .. import db
from ..auth.models import User
from ..services import delete_entity, delete_entity_bulk

logger = logging.getLogger(__name__)


@student_bp.route("/student")
@login_required
def index():
    logger.info('Access student index')

    return render_template("student/index.html")


@student_bp.route('/student/view/<int:id>')
def view(id):
    user = User.query.get_or_404(id)
    return render_template("student/index.html",
                           user=user)


@student_bp.route('/student/edit/<int:id>')
def edit(id):
    user = User.query.get_or_404(id)
    return render_template("student/edit.html", user=user)


@student_bp.route('/student/delete', methods=['POST'])
def delete():
    user_id = request.form.get('id')

    if not user_id:
        return jsonify({"message": "ID is required"}), 400

    result, status_code = delete_entity(User, user_id)

    return jsonify(result), status_code


@student_bp.route('/student/delete/bulk', methods=['POST'])
def delete_bulk():
    data = request.get_json()
    bulk_ids = data.get("bulkIds", "").split(",")

    if not bulk_ids:
        return jsonify({"message": "No IDs provided"}), 400

    result, status_code = delete_entity_bulk(User, bulk_ids)

    if status_code == 404:
        return jsonify({"message": "No users found with provided IDs"}), status_code

    return jsonify(result), status_code