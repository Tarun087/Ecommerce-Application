from entity.customers import Customers
from entity.products import Products


class Cart(Customers,Products):
    def __init__(self):
        super().__init__()
        self.cart_id = 0
        self.quantity = ''

    def get_cart_id(self):
        return self.cart_id

    def get_quantity(self):
        return self.quantity

    def set_card_id(self,cart_id):
        self.cart_id=cart_id

    def set_quantity(self,quantity):
        self.quantity=quantity

