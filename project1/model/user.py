from db_config import db, ma
from sqlalchemy import Column, Integer, String, DateTime


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    full_name = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sessions = db.session
        fields = ("id", "username", "full_name", "address")
