from flask import Flask, request, jsonify
from db_config import db, ma
from admin_config import admin
from model.user import User, UserSchema

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SECRET_KEY"] = "asdfawkjh"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['FLASK_ADMIN_SWATCH'] = 'Flatly'
app.config['JSON_AS_ASCII'] = False


db.init_app(app)
ma.init_app(app)
admin.init_app(app)


@app.route("/")
def home():
    return "Welcome to Flask"


@app.route("/api/users", methods=["GET", "POST"])
def users_list():
    if request.method == "GET":
        users = User.query.all()
        data = UserSchema().dump(users, many=True)
        print(data)
        return jsonify(data)
    if request.method == "POST":
        return "user_post" + request.method


if __name__ == "__main__":
    app.run(debug=True)
