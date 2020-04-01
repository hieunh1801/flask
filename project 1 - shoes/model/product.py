from db_config import db, ma
from sqlalchemy import Column, Integer, String, DateTime


class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    image_urls = Column(String, nullable=False)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        sessions = db.session
        fields = ("id", "name", "description", "image_urls")
