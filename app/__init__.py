import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()
metadata = db.metadata

def create_app():
    app = Flask(__name__)
    load_dotenv()

    db_parameters = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASSWORD'),
        "host": os.getenv('DB_HOST', 'localhost'),
        "port": os.getenv('DB_PORT', '5433'),
        "dbname": os.getenv('DB_NAME')
    }
        

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_RECORD_QUERIES'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['dbname']}"

    
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.resources import statistic
    app.register_blueprint(statistic, url_prefix='/sportiq/v1/statistics/')
    
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app