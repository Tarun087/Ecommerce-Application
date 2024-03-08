from entity.orders import Orders
from entity.products import Products


class OrderItems(Orders,Products):
    def __init__(self):
        super().__init__()
        self.order_item_id = 0
        self.quantity = 0


    def get_order_item_id(self):
        return self.order_item_id

    def set_order_item_id(self,order_item_id):
        self.order_item_id=order_item_id

    def get_quantity(self):
        return self.quantity

    def set_quantity(self,quantity):
        self.quantity=quantity
