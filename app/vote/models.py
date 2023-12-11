from datetime import datetime
from app.votation.models import StateVotation
from sqlalchemy import DateTime, ForeignKey  # Add ForeignKey import
from app import db


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    decision = db.Column(db.Boolean , nullable=False )
    description = db.Column(db.String(300), nullable=False)
    votation_id = db.Column(db.Integer, ForeignKey('proposal.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()