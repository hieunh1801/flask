from db_config import db, ma
from sqlalchemy import Column, Integer, String, DateTime


class Color(db.Model):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hex_value = Column(String(10))


class ColorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Color
        sessions = db.session
        fields = ("id", "name", "hex_value")
