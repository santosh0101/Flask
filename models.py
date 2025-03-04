from database import db  # ✅ Import db from database.py


class Business(db.Model):
    __tablename__ = "businesses"  # ✅ Table name

    id = db.Column(db.Integer, primary_key=True)  # ✅ Unique ID for each business
    name = db.Column(db.String(200), nullable=False, unique=True)  # ✅ Business name (must be unique)
    industry = db.Column(db.String(100), nullable=False)  # ✅ Industry type
    location = db.Column(db.String(255), nullable=True)  # ✅ Optional location
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # ✅ Auto timestamp

    def to_dict(self):
        """Convert Business instance to dictionary format."""
        return {
            "id": self.id,
            "name": self.name,
            "industry": self.industry,
            "location": self.location,
            "created_at": self.created_at
        }


class User(db.Model):
    __tablename__ = "users"

    appid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cluster = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convert User instance to dictionary format."""
        return {
            "appid": self.appid,
            "name": self.name,
            "email": self.email,
            "cluster": self.cluster
        }


# ✅ New Table: AppCluster
class AppCluster(db.Model):
    __tablename__ = "app_cluster"

    appid = db.Column(db.Integer, primary_key=True)
    cluster = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convert AppCluster instance to dictionary format."""
        return {
            "appid": self.appid,
            "cluster": self.cluster
        }
