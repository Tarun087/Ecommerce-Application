from entity.customers import Customers


class Orders(Customers):
    def __init__(self):
        super().__init__()
        self.order_id = 0
        self.order_date = ''
        self.shipping_address=''
        self.total_price=0.0

    def get_order_id(self):
        return self.order_id

    def get_order_date(self):
        return self.order_date

    def get_shipping_address(self):
        return self.shipping_address

    def get_total_price(self):
        return self.total_price

    def set_order_id(self,order_id):
        self.order_id=order_id

    def set_order_date(self,order_date):
        self.order_date=order_date

    def set_shipping_address(self,shipping_address):
        self.shipping_address=shipping_address

    def set_total_price(self,total_price):
        self.total_price=total_price
