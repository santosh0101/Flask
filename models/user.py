from database import db

class User(db.Model):
    __tablename__ = "users"

    appid = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cluster = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "appid": self.appid,
            "name": self.name,
            "email": self.email,
            "cluster": self.cluster
        }
