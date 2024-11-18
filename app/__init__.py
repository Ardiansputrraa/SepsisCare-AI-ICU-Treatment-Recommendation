from flask import Flask
from config import Config
from pymongo import MongoClient



def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # MONGODB
    client = MongoClient(app.config['MONGODB_URI'])
    app.db = client[app.config['DBNAME']]
    
    from .routes.auth import auth_
    app.register_blueprint(auth_)
    
    from .routes.bed_selection import dashboard_
    app.register_blueprint(dashboard_)
    
    from .routes.profile import profile_
    app.register_blueprint(profile_)
    
    return app