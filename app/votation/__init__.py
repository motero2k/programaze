from flask import Blueprint

votation_bp = Blueprint('votation', __name__, template_folder='templates')

from . import routes
