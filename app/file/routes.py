from flask import request, render_template, flash
from flask_login import login_required

from app.profile import profile_bp
from app.profile.forms import UserProfileForm
from .. import get_authenticated_user_profile

