from flask import Blueprint

token_request_bp = Blueprint('token_request', __name__, template_folder='templates')

from . import routes
