from flask import Blueprint

evidence_bp = Blueprint('evidence', __name__, template_folder='templates')

from . import routes
