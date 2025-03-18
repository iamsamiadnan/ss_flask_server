from flask import Flask
from extensions import db
from routes import main

def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.priixfefmlsfneulxpna:yJ0aygmzdpNWiOy5@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'

    db.init_app(app)

    app.register_blueprint(main)


    return app

if __name__ == "__main__":
    app = create_app()
  
    with app.app_context():
        db.create_all()

    app.run(debug=True)
