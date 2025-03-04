from flask import Flask, request, jsonify
from config import Config  # ✅ Import configuration
from database import db, init_db  # ✅ Import database
from models import User, AppCluster, Business  # ✅ Import models

app = Flask(__name__)
app.config.from_object(Config)  # ✅ Load configuration

# ✅ Initialize Database
init_db(app)

# ✅ Function to Lookup App ID from Cluster
def get_appid_from_cluster(cluster):
    """Looks up the App ID based on the given cluster."""
    cluster_entry = AppCluster.query.filter_by(cluster=cluster).first()
    return cluster_entry.appid if cluster_entry else None

# ✅ POST (Create a new user) with App ID Lookup
@app.route("/users/", methods=["POST"])
def create_user():
    """Create a new user with optional App ID lookup."""
    data = request.json

    # ✅ Validate input data
    if not all(k in data for k in ("name", "email", "cluster")):
        return jsonify({"error": "Missing required fields"}), 400

    # ✅ Check if email or cluster already exists in User table
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400
    if User.query.filter_by(cluster=data["cluster"]).first():
        return jsonify({"error": "Cluster already exists"}), 400

    # ✅ Get App ID (either from request or by lookup)
    appid = data.get("appid")

    if not appid:  # If no App ID provided, perform lookup
        appid = get_appid_from_cluster(data["cluster"])
        if appid is None:
            return jsonify({"error": "No matching App ID found for given cluster"}), 400

    # ✅ Create new user with the looked-up or provided App ID
    new_user = User(appid=appid, name=data["name"], email=data["email"], cluster=data["cluster"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

# ✅ GET all users
@app.route("/users/", methods=["GET"])
def get_all_users():
    """Fetch all users."""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# ✅ GET user by appid
@app.route("/users/<int:appid>", methods=["GET"])
def get_user_by_id(appid):
    """Fetch a user by their App ID."""
    user = User.query.get(appid)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

# ✅ GET all app clusters
@app.route("/app_clusters/", methods=["GET"])
def get_all_app_clusters():
    """Fetch all app clusters."""
    clusters = AppCluster.query.all()
    return jsonify([cluster.to_dict() for cluster in clusters])


# ✅ POST (Create a new app cluster)
@app.route("/app_clusters/", methods=["POST"])
def create_app_cluster():
    """Create a new app cluster."""
    data = request.json

    # ✅ Validate input data
    if not all(k in data for k in ("appid", "cluster")):
        return jsonify({"error": "Missing required fields"}), 400

    # ✅ Check if appid or cluster already exists
    if AppCluster.query.filter_by(appid=data["appid"]).first():
        return jsonify({"error": "App ID already exists"}), 400
    if AppCluster.query.filter_by(cluster=data["cluster"]).first():
        return jsonify({"error": "Cluster already exists"}), 400

    # ✅ Create new app cluster
    new_cluster = AppCluster(appid=data["appid"], cluster=data["cluster"])
    db.session.add(new_cluster)
    db.session.commit()

    return jsonify(new_cluster.to_dict()), 201

@app.route("/businesses/", methods=["POST"])
def create_business():
    """Create a new business."""
    data = request.json

    # ✅ Validate input data
    if not all(k in data for k in ("name", "industry")):
        return jsonify({"error": "Missing required fields"}), 400

    # ✅ Check if business name already exists
    if Business.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Business name already exists"}), 400

    # ✅ Create new business
    new_business = Business(
        name=data["name"],
        industry=data["industry"],
        location=data.get("location")  # Optional field
    )
    db.session.add(new_business)
    db.session.commit()

    return jsonify(new_business.to_dict()), 201


# ✅ Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
