from flask import Flask
from database import engine, Base, SessionLocal
from models import Campaign
import models  # important: ensures models are registered

def create_app():
    app = Flask(__name__)
    # For Production add (use dotenv and os package): app.secret_key = os.getenv("SECRET_KEY")

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Register routes
    from routes import main
    app.register_blueprint(main)

    return app


app = create_app()

@app.context_processor
def inject_campaigns():
    db = SessionLocal()
    campaigns = db.query(Campaign).all()
    db.close()
    return dict(campaigns=campaigns)

if __name__ == "__main__":
    app.run(debug=True)