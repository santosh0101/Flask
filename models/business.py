from database import db
from models.base_model import BaseModel  # ✅ Import BaseModel

class Business(BaseModel):
    """Business model representing companies."""
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
