import datetime

from modules.database.settings import db

from sqlalchemy.sql import func
from marshmallow import fields, Schema


# Represent a User table
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __init__(self, data):
        """
        Class constructor
        """

        self.firstname = data.get('firstname')
        self.lastname = data.get('lastname')
        self.email = data.get('email')
        self.created_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'<User {self.firstname}>'


class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
