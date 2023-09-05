import re
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from app import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    name = db.Column(db.String(100), nullable=False)
    clean_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    clean_surname = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    updated_at = db.Column(DateTime, default=datetime.utcnow)

    avatar_id = db.Column(db.Integer, db.ForeignKey('avatar.id'), nullable=True)
    avatar = relationship('Avatar', back_populates='user_profile')

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def clean_string(self, input_str):
        # Convert to uppercase, remove accents, special characters, and hyphens
        cleaned_str = input_str.upper()
        cleaned_str = re.sub(r'[^\w\s]', '', cleaned_str)  # Remove special characters
        cleaned_str = cleaned_str.replace('-', '')  # Remove hyphens
        cleaned_str = re.sub(r'\s+', '', cleaned_str)  # Remove extra whitespace
        return cleaned_str

    def __init__(self, user_id, name, surname, dni):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.dni = dni
        self.updated_at = datetime.utcnow()
        self.avatar_id = None

        self.clean_name = self.clean_string(name)
        self.clean_surname = self.clean_string(surname)


class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)

    from app.file.models import File
    file = relationship('File')

    user_profile = relationship('UserProfile', back_populates='avatar')
