from flask import Flask
from app import routes
from app.configs import database, migration, enviroments

def create_app():
    app = Flask(__name__)
    
    enviroments.init_app(app)    
    database.init_app(app)
    migration.init_app(app)
    
    routes.init_app(app)

    return app