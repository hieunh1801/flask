from flask import Flask, request, jsonify
from db_config import db, ma
from admin_config import admin
from api_config import api
from os import path

app = Flask(__name__)

# db config
DATABASE_NAME = "shoes.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_ECHO"] = False

# admin view config
app.config['FLASK_ADMIN_SWATCH'] = 'Flatly'

# return json
app.config['JSON_AS_ASCII'] = False

# screetkey for session
app.config["SECRET_KEY"] = "asdfawkjh"


db.init_app(app)
ma.init_app(app)
admin.init_app(app)
api.init_app(app)


@app.route("/")
def home():
    return "Welcome to Flask"


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
