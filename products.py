from util.DBconnection import DBConnection


class Products(DBConnection):
    def __init__(self):
        super().__init__()
        self.product_id = 0
        self.name = ''
        self.price = 0.0
        self.description = ''
        self.stockQuantity = 0

    def get_product_id(self):
        return self.product_id

    def set_product_id(self,product_id):
        self.product_id = product_id

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_stockQuantity(self):
        return self.stockQuantity

    def set_stockQuantity(self,stockQuantity):
        self.stockQuantity = stockQuantity