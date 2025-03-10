from database import db

class User(db.Model):
    """User model representing application users."""
    __tablename__ = "users"

    appid = db.Column(db.Integer, unique=True, primary_key=True)  # ✅ Unique App ID
    name = db.Column(db.String(100), unique=True, nullable=False)  # ✅ User Name
    email = db.Column(db.String(100), unique=True, nullable=False)  # ✅ Unique Email
    cluster = db.Column(db.String(50), nullable=False) 

    def to_dict(self):
        """Convert User instance to dictionary format."""
        return {
            "appid": self.appid,
            "name": self.name,
            "email": self.email,    
            "cluster": self.cluster
        }
