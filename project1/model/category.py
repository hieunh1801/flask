from db_config import db, ma
from sqlalchemy import Column, Integer, String, DateTime


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    image_urls = Column(String(200), nullable=False)


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        sessions = db.session
        fields = ("id", "name", "description", "image_urls")
