from flask import Blueprint

file_bp = Blueprint('file', __name__, template_folder='templates')

from . import routes
