from flask import Blueprint

vote_bp = Blueprint('vote', __name__, template_folder='templates')

from . import routes
