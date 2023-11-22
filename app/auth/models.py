from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import select, column, DateTime
from sqlalchemy.orm import aliased
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    token = db.Column(db.Integer, nullable=True, default = 0)
    


    profile = db.relationship('UserProfile', backref='user', lazy=True, uselist=False, cascade="all, delete-orphan")

    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    student = db.relationship('Student', backref='user', uselist=False, cascade="all, delete-orphan")
    coordinator = db.relationship('Coordinator', backref='user', uselist=False, cascade="all, delete-orphan")
    secretary = db.relationship('Secretary', backref='user', uselist=False, cascade="all, delete-orphan")
    event_manager = db.relationship('EventManager', backref='user', uselist=False, cascade="all, delete-orphan")
    reviewer = db.relationship('Reviewer', backref='user', uselist=False, cascade="all, delete-orphan")
    lecture = db.relationship('Lecturer', backref='user', uselist=False, cascade="all, delete-orphan")
    proposals = db.relationship('Proposal', backref='user', lazy=True)

    def __init__(self, username, email, password, token, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.token = token


    def name(self):
        return self.profile.name if self.profile else None

    def surname(self):
        return self.profile.surname if self.profile else None

    def get_role_creation_time(self, role_id):
        """ Returns the creation time when the role was assigned to the user. """

        # Create an alias for the user_roles table
        user_roles_alias = aliased(user_roles)

        # Query the user_roles table using the alias
        relation = db.session.query(user_roles_alias).filter(
            user_roles_alias.c.user_id == self.id,
            user_roles_alias.c.role_id == role_id
        ).first()

        # Return the created_at attribute if the relation exists
        return relation.created_at if relation else None

    @property
    def current_roles(self):
        roles = []

        if self.student:
            roles.append("Student")
        if self.coordinator:
            roles.append("Coordinator")
        if self.secretary:
            roles.append("Secretary")
        if self.event_manager:
            roles.append("EventManager")
        if self.reviewer:
            roles.append("Reviewer")

        return roles

    def get_roles(self):
        return self.roles

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return User.query.all()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow)

    VALID_ROLES = ['STUDENT', 'COORDINATOR', 'SECRETARY', 'REVIEWER', 'EVENT_MANAGER', 'LECTURER', 'DEVELOPER','PROGRAM_COORDINATOR',
                   'PRESIDENT']

    ROLES_MAPPING = {
        'STUDENT': 'Estudiante',
        'COORDINATOR': 'Coordinador',
        'SECRETARY': 'Secretario',
        'REVIEWER': 'Revisor',
        'EVENT_MANAGER': 'Manager de Eventos',
        'LECTURER': 'Profesor',
        'DEVELOPER': 'Desarrollador',
        'PRESIDENT': 'Presidente',
        'PROGRAM_COORDINATOR': 'Coordinador de Programa'
    }

    def __init__(self, name):
        if name not in self.VALID_ROLES:
            raise ValueError(f"The role '{name}' is not valid.")
        self.name = name

    def get_users_by_role(self):
        users = User.query.join(user_roles).filter(user_roles.c.role_id == self.id).all()
        return users

    @property
    def name_in_spanish(self):
        return self.ROLES_MAPPING.get(self.name, self.name)


user_roles = db.Table('user_roles',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
                      db.Column('created_at', db.DateTime, default=datetime.utcnow)
                      )


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Coordinator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Secretary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class EventManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


class President(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
