from util.DBconnection import DBConnection


class Customers(DBConnection):
    def __init__(self):
        super().__init__()
        self.customer_id = 0
        self.name = ''
        self.email = ''
        self.password = ''

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self,password):
        self.password = password


