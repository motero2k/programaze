from datetime import datetime
from sqlalchemy import DateTime
from app import db


class Innosoft_day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    
    
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def __init__(self, description, subject, year):
        
        self.description = description
        self.subject = subject
        self.year = year
        
        
        