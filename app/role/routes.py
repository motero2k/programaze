import logging
from flask import render_template, request, jsonify
from flask_login import login_required
from . import role_bp
from ..auth.models import Role, User
from ..services import delete_entity, delete_entity_bulk
logger = logging.getLogger(__name__)


@role_bp.route("/role/<int:role_id>/user/<int:user_id>")
@login_required
def delete_user_from_role (role_id, user_id):
    role = Role.query.get_or_404(role_id)
    user = User.query.get_or_404(user_id)
    pass
