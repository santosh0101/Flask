from flask_sqlalchemy import SQLAlchemy

# ✅ Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """Initialize the database within the Flask app context."""
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable unnecessary warnings
    db.init_app(app)

    with app.app_context():
        db.create_all()  # ✅ Creates tables if they don't exist
        print("✅ Database tables created.")
