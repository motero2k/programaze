import logging

from flask import render_template
from flask_login import login_required

from . import dashboard_bp

logger = logging.getLogger(__name__)


@dashboard_bp.route("/")
@login_required
def index():
    logger.info('Access index')

    return render_template("dashboard/index.html")
