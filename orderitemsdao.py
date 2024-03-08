from entity.orderitems import OrderItems
# from entity.orders import Orders
# from entity.products import Products


class OrderItemsDao(OrderItems):
    def __init__(self):
        super().__init__()


    def perform_orderitems_actions(self):
        while True:
            print("(OrdersItems) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")

            ch=int(input("Enter Choice: "))
            if ch==1:
                self.create_orderitems_table()
            elif ch==2:
                print(self.add_orderitem())
            elif ch==3:
                print(self.update_orderitem())
            elif ch==4:
                print(self.delete_orderitem())
            elif ch==5:
                self.select_orderitem()
            elif ch==0:
                break
            else:
                print("Invalid Choice")


    def create_orderitems_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS OrderItems(
            order_item_id int primary key,
            order_id int,
            product_id int,
            quantity int,
            foreign key (order_id) references Orders(order_id),
            foreign key (product_id) references Product(product_id)
            )'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Cart Table created Successfully")
        except Exception as e:
            print(e)


    def add_orderitem(self):
        try:
            self.open()
            self.order_item_id = int(input("Order Item ID: "))
            self.order_id= int(input("Order Id : "))
            self.product_id = int(input("Product Id : "))
            self.quantity = input("Quantity : ")
            data = [(self.order_item_id,self.order_id,self.product_id,self.quantity)]
            insert_str = '''INSERT into OrderItems(order_item_id,order_id,product_id,quantity) 
            values(%s,%s,%s,%s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def update_orderitem(self):
        try:
            self.open()
            self.order_item_id = int(input("Order Item ID: "))
            self.order_id = int(input("Order Id : "))
            self.product_id = int(input("Product Id : "))
            self.quantity = input("Quantity : ")
            data = [(self.order_item_id, self.order_id, self.product_id, self.quantity)]
            insert_str = '''Update OrderItems set order_item_id=%s,order_id=%s,product_id=%s,quantity=%s'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def delete_orderitem(self):
        try:
            self.open()
            order_item_id = input("Enter Order Item Id to be Deleted : ")
            delete_str = f'''Delete from OrderItems where order_item_id = {order_item_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_orderitem(self):
        try:
            select_str = '''select * from OrderItems'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print("Records in Orders Table : ")
            for i in records:
                print(i)
        except Exception as e:
            print(e)

