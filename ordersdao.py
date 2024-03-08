from entity.orders import Orders


class OrdersDao(Orders):
    def __init__(self):
        super().__init__()


    def perform_orders_actions(self):
        while True:
            print("(Orders) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")

            ch=int(input("Enter Choice: "))
            if ch==1:
                self.create_orders_table()
            elif ch==2:
                print(self.add_order())
            elif ch==3:
                print(self.update_order())
            elif ch==4:
                print(self.delete_order())
            elif ch==5:
                self.select_order()
            elif ch==0:
                break
            else:
                print("Invalid Choice")


    def create_orders_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Orders(
            order_id int primary key,
            customer_id int,
            order_date Date,
            total_price float,
            shipping_address varchar(255),
            foreign key (customer_id) references Customers(customer_id)
            )'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Cart Table created Successfully")
        except Exception as e:
            print(e)


    def add_order(self):
        try:
            self.open()
            self.order_id = int(input("Order ID: "))
            self.customer_id = int(input("Customer Id : "))
            self.order_date = input("Order Date : ")
            self.total_price = int(input("Total Price : "))
            self.shipping_address = input("Shipping Address : ")
            data = [(self.order_id,self.customer_id,self.order_date,self.total_price,self.shipping_address)]
            insert_str = '''INSERT into Orders(order_id,customer_id,order_date,total_price,shipping_address) 
            values(%s,%s,%s,%s,%s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def update_order(self):
        try:
            self.open()
            self.order_id = int(input("Order ID: "))
            self.customer_id = int(input("Customer Id : "))
            self.order_date = input("Order Date : ")
            self.total_price = int(input("Total Price : "))
            self.shipping_address = input("Shipping Address : ")
            data = [(self.order_id, self.customer_id, self.order_date, self.total_price, self.shipping_address)]
            update_str = '''Update Orders set order_id=%s,customer_id=%s,order_date=%s,
            total_price=%s,shipping_address=%s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def delete_order(self):
        try:
            self.open()
            order_id = input("Enter Order Id to be Deleted : ")
            delete_str = f'''Delete from Orders where order_id = {order_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_order(self):
        try:
            select_str = '''select * from Orders'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print("Records in Orders Table : ")
            for i in records:
                print(i)
        except Exception as e:
            print(e)

