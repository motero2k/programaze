from flask import Blueprint

lecturer_bp = Blueprint('lecturer', __name__, template_folder='templates')

from . import routes
