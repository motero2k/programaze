from datetime import datetime
from sqlalchemy import DateTime
from app import db


class Evidence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow)
