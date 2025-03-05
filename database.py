from flask_sqlalchemy import SQLAlchemy

# ✅ Initialize SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """Initialize the database within the Flask app context."""
    db.init_app(app)  # ✅ Bind SQLAlchemy to Flask app

    with app.app_context():
        from models import User, AppCluster, Business # ✅ Import both models
        db.create_all()
        print("✅ Database tables created.")
