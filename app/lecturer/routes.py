import logging

import pandas as pd
from flask import render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required

from . import lecturer_bp
from .services import get_all_students
from .. import db
from ..auth.models import User, Role, user_roles
from ..profile.models import UserProfile

logger = logging.getLogger(__name__)


@lecturer_bp.route("/lecturer/users/manage")
@login_required
def users_manage():
    logger.info('Access lecturer index')

    users = get_all_students()

    data_collection = [{
        'id': user.id, 
        'Email': user.email,
        'Apellidos': user.surname(),
        'Nombre': user.name()
    } for user in users]

    return render_template('lecturer/users/manage.html', data_collection=data_collection)


@lecturer_bp.route("/lecturer/users/roles")
@login_required
def users_roles():
    logger.info('Access lecturer index')

    all_roles = Role.query.order_by(Role.name).all()

    roles_with_user_count = {}

    for role in all_roles:
        users = role.get_users_by_role()
        user_count = len(users)
        roles_with_user_count[role] = user_count

    return render_template("lecturer/users/roles.html", roles_with_user_count=roles_with_user_count)


@lecturer_bp.route("/lecturer/users/roles/<int:role_id>", methods=["GET", "POST"])
@login_required
def edit_role_users(role_id):
    logger.info('Edit role users')

    role = Role.query.get_or_404(role_id)

    if request.method == "POST":
        return redirect(url_for("lecturer_bp.view_role", role_id=role.id))

    users = role.get_users_by_role()

    data_collection = [{
        'id': user.id,
        'Email': user.email,
        'Apellidos': user.surname(),
        'Nombre': user.name(),
        'Unido el': user.get_role_creation_time(role.id)
    } for user in users]

    return render_template("lecturer/users/edit_role_users.html", role=role, data_collection=data_collection)


@lecturer_bp.route("/lecturer/users/upload", methods=['POST'])
@login_required
def upload_excel():
    if 'file' not in request.files:
        flash(f'No se encontró un archivo Excel en la solicitud', 'error')
        return redirect(url_for('lecturer.users_manage'))

    file = request.files['file']

    if file.filename == '' or not file.filename.endswith(('.xls', '.xlsx')):
        flash(f'Formato de archivo no válido', 'error')
        return redirect(url_for('lecturer.users_manage'))

    try:
        df = pd.read_excel(file)
    except Exception as e:
        flash(f'Error al leer el archivo Excel, {str(e)}', 'error')
        return redirect(url_for('lecturer.users_manage'))

    # Definición de encabezados conocidos
    column_headers = ['DNI', 'UVUS', 'NOMBRE', 'APELLIDOS', 'EMAIL']

    # Diccionario para mapear los nombres de las columnas a los campos del modelo de datos
    column_mapping = {
        'DNI': 'dni',
        'UVUS': 'username',
        'NOMBRE': 'nombre',
        'APELLIDOS': 'apellidos',
        'EMAIL': 'email'
    }

    for index, row in df.iterrows():
        user_data = {}

        # Itera a través de las columnas del DataFrame y mapea los datos al modelo de datos
        for header in column_headers:
            column_name = column_mapping.get(header, None)
            if column_name is not None:
                user_data[column_name] = str(row.get(header, '')).strip()  # Elimina espacios en blanco al principio y al final

        # Si los nombres y apellidos están en una sola columna, divídelos por la coma
        full_name = user_data.get('apellidos', '')
        if ',' in full_name:
            last_name, first_name = full_name.split(',', 1)
            user_data['nombre'] = first_name.strip()
            user_data['apellidos'] = last_name.strip()

        # Crea un nuevo usuario solo si se proporciona al menos un campo válido
        if any(user_data.values()):
            existing_user_email = User.query.filter_by(email=user_data['email']).first()
            existing_user_dni = UserProfile.query.filter_by(dni=user_data['dni']).first()
            existing_user_username = User.query.filter_by(username=user_data['username']).first()

            if existing_user_email or existing_user_dni or existing_user_username:
                continue

            new_user = User(username=user_data['username'], email=user_data['email'], password=user_data['dni'])

            student_role = Role.query.filter_by(name='STUDENT').first()
            if student_role:
                new_user.roles.append(student_role)

            db.session.add(new_user)
            db.session.flush()

            new_profile = UserProfile(
                user_id=new_user.id,
                name=user_data['nombre'],
                surname=user_data['apellidos'],
                dni=user_data['dni']
            )
            db.session.add(new_profile)

            db.session.commit()

    flash('Usuarios creados correctamente', 'success')

    return redirect(url_for('lecturer.users_manage'))

