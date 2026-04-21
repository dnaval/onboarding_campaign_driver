from flask import Flask
from database import engine, Base
import models  # important: ensures models are registered

def create_app():
    app = Flask(__name__)

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Register routes
    from routes import main
    app.register_blueprint(main)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)