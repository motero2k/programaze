from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from app import db

class TokenState(Enum):
    ACCEPTED = 'ACEPTADO'
    PENDING_OF_ACEPTATION = 'PENDIENTE DE ACEPTACIÓN'
    REJECTED = 'RECHAZADO'


class Token_request(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=False)
    num_token = db.Column(db.Integer,nullable=False)

    description = db.Column(db.String(300), nullable=False)
    token_state = db.Column(db.Enum(TokenState), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    