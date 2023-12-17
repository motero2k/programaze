import os

from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app import db
from app.proposal.models import Proposal,ProposalType
from app.auth.models import User

test_routes = Blueprint('test_routes', __name__)


@test_routes.route('/test')
def test_route():
    return 'Test route'


@test_routes.route('/env')
def show_env():
    env_vars = {key: value for key, value in os.environ.items()}
    return jsonify(env_vars)


