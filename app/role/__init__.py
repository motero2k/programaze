from flask import Blueprint

role_bp = Blueprint('role', __name__, template_folder='templates')

from . import routes
