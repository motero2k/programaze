from flask import Blueprint

innosoft_day_bp = Blueprint('innosoft_day', __name__, template_folder='templates')

from . import routes
