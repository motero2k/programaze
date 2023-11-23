from datetime import datetime
from sqlalchemy import DateTime
from app import db
from enum import Enum
from sqlalchemy import ForeignKey


class StateVotation(Enum):
    ACCEPTED = 'ACEPTADA' 
    REJECTED = 'RECHAZADA'
    IN_PROGRESS = 'EN CURSO'

class Votation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state_votation = db.Column(db.Enum(StateVotation), nullable=False)
    proposal_id = db.Column(db.Integer, ForeignKey('proposal.id'), nullable=False)
    

    #falta relación votos con votacion


    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    