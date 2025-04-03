from flask import Flask, request, jsonify
from config import Config
from database import db, init_db
from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Flask API Project!"}), 200

@app.route("/users/", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        appid=data["appid"],
        name=data["name"],
        email=data["email"],
        cluster=data["cluster"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route("/users/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

if __name__ == "__main__":
    app.run(debug=True)
