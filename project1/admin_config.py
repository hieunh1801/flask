from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from model.user import User
from db_config import db


admin = Admin(name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
