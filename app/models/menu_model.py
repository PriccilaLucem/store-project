from dataclasses import dataclass
from app.configs.database import db


@dataclass
class Menu(db.Model):
    id:int
    product_name:str
    product_description:str
    product_price:float
    
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(40), nullable=False)
    product_description = db.Column(db.String(200), nullable=True)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, default = 0, nullable=False)
    cart_relationship = db.relationship("Cart_Menu", back_populates="menu")

    @staticmethod
    def validate_args(**kwargs):
        if type(kwargs['product_name']) != str:
            raise TypeError
        if kwargs['product_description']:
            if type(kwargs['product_description']) != str:
                raise TypeError
        float(kwargs['product_price'])
        if 'product_quantity' in kwargs:
            if type(kwargs['product_quantity']) != int:
                raise TypeError
        
    @staticmethod
    def check_args(**kwargs):
        VALIDATED_ARGS = ['product_name', 'product_description', 'product_price', 'product_quantity']
        return {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}
