from dao.productsdao import ProductsDao
from dao.customersdao import CustomersDao
from dao.cartdao import CartDao
from dao.ordersdao import OrdersDao
from exception.Customer_not_FoundException import CustomerNotFoundException


class OrderProcessorRepository(CartDao,OrdersDao):
    def create_product(self) -> bool:
        p = ProductsDao()
        p.add_product()
        p.select_product()
        pass

    def create_customer(self) -> bool:
        c = CustomersDao()
        c.add_customer()
        c.select_customer()
        pass

    def delete_product(self) -> bool:
        p = ProductsDao()
        p.delete_product()
        p.select_product()
        pass

    def delete_customer(self) -> bool:
        c = CustomersDao()
        c.delete_customer()
        c.select_customer()

        pass

    def add_to_cart(self) -> bool:
        c = CartDao()
        c.add_cart()
        c.select_cart()
        pass

    def remove_from_cart(self) -> bool:
        c = CartDao()
        c.delete_cart()
        c.select_cart()
        pass

    def get_all_from_cart(self) -> bool:
        c = CartDao()
        c.select_cart()
        pass

    def place_order(self) -> bool:
        o = OrdersDao()
        o.add_order()
        o.select_order()
        return True

    def viewCustomerOrder(self, customer_id) -> bool:
        try:
            self.open()
            # customer_id = int(input("Enter customer ID: "))
            self.stmt.execute(f'''SELECT COUNT(*) FROM Orders WHERE customer_id = {customer_id}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                return CustomerNotFoundException(customer_id)
            else:
                self.stmt.execute(f'''SELECT * FROM Orders WHERE customer_id = {customer_id} ''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except CustomerNotFoundException as e:
            return e
        except Exception as e:
            return e