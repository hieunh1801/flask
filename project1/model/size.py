from db_config import db, ma
from sqlalchemy import Column, Integer, String, DateTime


class Size(db.Model):
    __tablename__ = "size"
    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)
    type = Column(String)


class SizeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Size
        sessions = db.session
        fields = ("id", "size", "type")
