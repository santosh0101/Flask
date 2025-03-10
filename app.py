from flask import Flask, request, jsonify
from database import db, init_db
from models import User
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# ✅ Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  

# ✅ Initialize Database
init_db(app)

# ✅ POST: Create a Single User
@app.route("/users/", methods=["POST"])
def create_user():
    try:
        data = request.get_json()  # ✅ Read JSON data

        # ✅ Validate required fields
        if not all(k in data for k in ("appid", "name", "email", "cluster")):
            return jsonify({"error": "Missing required fields"}), 400

        new_user = User(
            appid=data["appid"],
            name=data["name"],
            email=data["email"],
            cluster=data["cluster"]
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201  # ✅ Return created user

    except IntegrityError as e:
        db.session.rollback()  # ✅ Rollback failed transaction

        # ✅ Check if duplicate constraint failed
        if "UNIQUE constraint failed: users.name" in str(e):
            return jsonify({"error": "Name already exists"}), 400
        if "UNIQUE constraint failed: users.email" in str(e):
            return jsonify({"error": "Email already exists"}), 400
        if "UNIQUE constraint failed: users.appid" in str(e):
            return jsonify({"error": "App ID already exists"}), 400

        return jsonify({"error": "Database error"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ GET: Retrieve All Users or a Specific User by Query Parameter (appid)
@app.route("/users/", methods=["GET"])
def get_users():
    """Fetch all users or a specific user by App ID (via query param)."""
    appid = request.args.get("appid")

    if appid:
        try:
            appid = int(appid)  # ✅ Convert to integer
        except ValueError:
            return jsonify({"error": "Invalid appid format"}), 400

        user = User.query.filter_by(appid=appid).first()
        if user:
            return jsonify(user.to_dict())  # ✅ Return a single user
        return jsonify({"error": "User not found"}), 404  # If appid doesn't exist

    # ✅ If no appid is provided, return all users
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# ✅ Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
