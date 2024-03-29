from flask import Flask
from app.routes.menu_bp import menu_bp
from app.routes.client_bp import client_bp
from app.routes.login_bp import login_bp
from app.routes.address_bp import address_bp
from app.routes.cart_bp import cart_bp
from app.routes.credit_card_bp import credit_card_bp

def init_app(app:Flask):
    app.register_blueprint(menu_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(cart_bp) 
    app.register_blueprint(credit_card_bp)