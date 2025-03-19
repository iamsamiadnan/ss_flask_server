from flask import Flask
from extensions import db
from routes import main
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

    CORS(app, resources={r"/api/*": {"origins": os.getenv('CLIENT_URI')}},  supports_credentials=True)
    db.init_app(app)

    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    app = create_app()
  
    with app.app_context():
        db.create_all()

    app.run(debug=True)
