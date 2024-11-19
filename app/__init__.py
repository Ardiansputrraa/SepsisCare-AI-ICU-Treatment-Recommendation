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
    
    from .routes.vital_patient import vital_patient_
    app.register_blueprint(vital_patient_)
    
    from .routes.treatment_recommendation import treatment_recommendation_
    app.register_blueprint(treatment_recommendation_)
    
    from .routes.predict import predict_
    app.register_blueprint(predict_)
    
    from .routes.forecasting import forecasting_
    app.register_blueprint(forecasting_)
    
    from .routes.treatment_history import treatment_history_
    app.register_blueprint(treatment_history_)
    
    return app