from database import db

class BaseModel(db.Model):
    """Base model with common methods."""
    __abstract__ = True  # ✅ Prevents table creation for this class

    def to_dict(self):
        """Convert model instance to dictionary format."""
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
