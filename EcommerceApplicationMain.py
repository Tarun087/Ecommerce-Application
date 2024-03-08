from util.DBconnection import DBConnection
from dao.cartdao import CartDao
from dao.ordersdao import OrdersDao
from dao.productsdao import ProductsDao
from dao.customersdao import CustomersDao
from dao.orderitemsdao import OrderItemsDao
from dao.OrderProcessorRepository import OrderProcessorRepository
from exception.Order_not_FoundException import OrderNotFoundException
from exception.Product_not_FoundException import ProductNotFoundException
from exception.Customer_not_FoundException import CustomerNotFoundException


class EcommerceApplicationMain:


    @staticmethod
    def main():
        dbconnection = DBConnection()

        try:
            dbconnection.open()
            print("Database Connected")
        except Exception as e:
            print(e)

        try:
            print("_" * 30)
            print("Ecommerce Application")
            print("_" * 30)
            print("Welcome to Ecommerce Application!")

            order_processor = OrderProcessorRepository()

            while True:
                print("1.Products 2.Customers 3.Orders 4.OrderItems 5.Cart 0.EXIT")
                ch = int(input("Enter choice: "))
                if ch == 1:
                    p = ProductsDao()
                    p.perform_product_actions()
                elif ch == 2:
                    c = CustomersDao()
                    c.perform_customer_actions()
                elif ch == 3:
                    e = OrdersDao()
                    e.perform_orders_actions()
                elif ch == 4:
                    o = OrderItemsDao()
                    o.perform_orderitems_actions()
                elif ch == 5:
                    u = CartDao()
                    u.perform_cart_actions()

                elif ch == 0:
                    break
                else:
                    print("Invalid choice")

            while True:
                print("=" * 10)
                print("---Main Menu---")
                print("=" * 10)
                print('''
                1.Create Product
                2.Create Customer
                3.Delete Product
                4.Delete Customer
                5.Add to Cart
                6.Remove from Cart
                7.Get All Products
                8.Place Order
                9.View Customer Order
                0.EXIT''')
                ch = int(input("Enter choice: "))
                if ch == 1:
                    print(f'Product Created : {order_processor.create_product()}')
                elif ch == 2:
                    print(f'Customer Created : {order_processor.create_customer()}')
                elif ch == 3:
                    print(f'Product Deleted : {order_processor.delete_product()}')
                elif ch == 4:
                    print(f'Customer Deleted : {order_processor.delete_customer()}')
                elif ch == 5:
                    print(f'Added to Cart : {order_processor.add_to_cart()}')
                elif ch == 6:
                    print(f'Removed from Cart{order_processor.remove_from_cart()}')
                elif ch == 7:
                    print(f'All from Cart : {order_processor.get_all_from_cart()}')
                elif ch == 8:
                    print(f'Order Placed : {order_processor.place_order()}')
                elif ch == 9:
                    print(f'Customer Orders : {order_processor.viewCustomerOrder(int(input("Enter Customer Id : ")))}')
                elif ch == 0:
                    break
                else:
                    print("Invalid choice")



        except CustomerNotFoundException as e:
            print(e)

        except OrderNotFoundException as e:
            print(e)

        except ProductNotFoundException as e:
            print(e)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    EcommerceApplicationMain.main()