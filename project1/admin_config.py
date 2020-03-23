from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.category import Category
from model.color import Color
from model.product import Product
from model.size import Size
from src.user.user_model import User

from db_config import db


admin = Admin(name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Color, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Size, db.session))
admin.add_view(ModelView(User, db.session))
