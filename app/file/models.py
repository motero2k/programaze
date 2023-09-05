from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import relationship
from app import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    size_in_bytes = db.Column(BigInteger, nullable=False)

    folder_id = db.Column(db.Integer, db.ForeignKey('file_folder.id'), nullable=False)

    folder = relationship('FileFolder', back_populates='files')

    def human_readable_size(self):
        size = self.size
        suffixes = ['B', 'KB', 'MB', 'GB']
        i = 0
        while size >= 1024 and i < len(suffixes) - 1:
            size /= 1024.0
            i += 1
        return f"{size:.2f} {suffixes[i]}"


class FileFolder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    parent_folder_id = db.Column(db.Integer, db.ForeignKey('file_folder.id'))

    files = relationship('File', back_populates='folder')

    parent_folder = relationship('FileFolder', remote_side=[id], backref='child_folders', uselist=False)

    def add_file(self, name, size, file_type):
        file = File(name=name, size=size, file_type=file_type, folder=self)
        db.session.add(file)
        db.session.commit()

    def get_files(self):
        return self.files
