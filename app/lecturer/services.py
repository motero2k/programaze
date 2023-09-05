from app import db
from app.auth.models import Role, user_roles, User


def get_all_students():
    lecturer_role = Role.query.filter_by(name="LECTURER").first()
    if not lecturer_role:
        return "Role LECTURER not found", 500

    lecturer_users_ids = [user_role.user_id for user_role in
                          db.session.query(user_roles.c.user_id).filter(user_roles.c.role_id == lecturer_role.id).all()]

    users = User.query.filter(User.id.notin_(lecturer_users_ids)).all()

    return users
