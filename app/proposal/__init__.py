from flask import Blueprint

proposal_bp = Blueprint('proposal', __name__, template_folder='templates')

from . import routes
