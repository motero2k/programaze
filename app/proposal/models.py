from datetime import datetime
from sqlalchemy import DateTime
from app import db
from enum import Enum
from sqlalchemy import ForeignKey

class ProposalType(Enum):
    TALK = 'CHARLA' 
    ACTIVITY = 'ACTIVIDAD'
    STAND = 'STAND'

class State(Enum):
    PENDING_OF_ADMISION = 'PENDIENTE DE ADMISIÓN'
    PENDING_OF_ACEPTATION = 'PENDIENTE DE ACEPTACIÓN'
    ON_PREPARATION = 'EN PREPARACIÓN'
    CONFIRMATED = 'CONFIRMADO'
    REJECTED = 'RECHAZADO'
    CLOSED = 'CERRADO'

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    proposal_type = db.Column(db.Enum(ProposalType), nullable=False)
    state = db.Column(db.Enum(State), nullable=False)
    innosoft_day_id = db.Column(db.Integer, ForeignKey('innosoft_day.id'), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    

    