from flask import (render_template, redirect, url_for)
from flask_login import current_user, login_user, logout_user

from . import auth_bp
from .forms import SignupForm, LoginForm
from .models import User
from ..profile.models import UserProfile


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Intenta buscar al usuario por correo electrónico
        user = User.get_by_email(form.email.data)

        # Si no se encuentra por correo electrónico, intenta buscar por nombre de usuario
        if user is None:
            user = User.get_by_username(form.email.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('dashboard.index'))
        else:
            error = f'Invalid credentials'
            return render_template("auth/login_form.html", form=form, error=error)

    return render_template('auth/login_form.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('dashboard.index'))
