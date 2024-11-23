from database.db import db
from flask_login import UserMixin

class Usuarios(db.Model,UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username=db.Column(db.String(300), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    admin = db.Column(db.Boolean, nullable=False,default=False)

    