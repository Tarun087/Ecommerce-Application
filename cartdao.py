from entity.cart import Cart


class CartDao(Cart):
    def __init__(self):
        super().__init__()


    def perform_cart_actions(self):
        while True:
            print("(Cart) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")

            ch=int(input("Enter Choice: "))
            if ch==1:
                self.create_cart_table()
            elif ch==2:
                print(self.add_cart())
            elif ch==3:
                print(self.update_cart())
            elif ch==4:
                print(self.delete_cart())
            elif ch==5:
                self.select_cart()
            elif ch==0:
                break
            else:
                print("Invalid Choice")


    def create_cart_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Cart(
            cart_id int primary key,
            quantity varchar(50) not null,
            customer_id int,
            product_id int,
            foreign key (product_id) references Product(product_id),
            foreign key (customer_id) references Customers(customer_id)
            )'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Cart Table created Successfully")
        except Exception as e:
            print(e)


    def add_cart(self):
        try:
            self.open()
            self.cart_id=int(input("Cart ID: "))
            self.quantity=input("Quantity : ")
            self.customer_id = int(input("Customer Id : "))
            self.product_id = int(input("Product Id : "))
            data = [(self.cart_id,self.quantity,self.customer_id,self.product_id)]
            insert_str = '''INSERT into Cart(cart_id,quantity,customer_id,product_id) 
            values(%s,%s,%s,%s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def update_cart(self):
        try:
            self.open()
            self.cart_id = int(input("Cart ID: "))
            self.quantity = input("Quantity : ")
            self.customer_id = int(input("Customer Id : "))
            self.product_id = int(input("Product Id : "))
            data = [(self.cart_id, self.quantity, self.customer_id, self.product_id)]
            update_str = '''Update cart set cart_id=%s , quantity=%s,customer_id=%s,product_id=%s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def delete_cart(self):
        try:
            self.open()
            cart_id = input("Enter Cart Id to be Deleted : ")
            delete_str = f'''Delete from Cart where cart_id = {cart_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_cart(self):
        try:
            select_str = '''select * from Cart'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print("Records in Cart Table : ")
            for i in records:
                print(i)
        except Exception as e:
            print(e)

