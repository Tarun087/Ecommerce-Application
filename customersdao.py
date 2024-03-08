from entity.customers import Customers


class CustomersDao(Customers):
    def __init__(self):
        super().__init__()


    def perform_customer_actions(self):
        while True:
            print("(Customers) 1.CREATE 2.INSERT 3.UPDATE 4.DELETE 5.SELECT 0.EXIT")

            ch=int(input("Enter Choice: "))
            if ch==1:
                self.create_customer_table()
            elif ch==2:
                print(self.add_customer())
            elif ch==3:
                print(self.update_customer())
            elif ch==4:
                print(self.delete_customer())
            elif ch==5:
                self.select_customer()
            elif ch==0:
                break
            else:
                print("Invalid Choice")


    def create_customer_table(self):
        try:
            create_str = '''CREATE TABLE IF NOT EXISTS Customers(
            customer_id int primary key,
            name varchar(50) not null,
            email varchar(50),
            password varchar(50) not null
            )'''
            self.open()
            self.stmt.execute(create_str)
            self.close()
            print("Customers Table created Successfully")
        except Exception as e:
            print(e)


    def add_customer(self):
        try:
            self.open()
            self.customer_id=int(input("Customer ID: "))
            self.name=input("Customer Name : ")
            self.email = input("Email : ")
            self.password = input("Password : ")
            data = [(self.customer_id,self.name,self.email,self.password)]
            insert_str = '''INSERT into Customers(customer_id,name,email,password) 
            values(%s,%s,%s,%s)'''
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def update_customer(self):
        try:
            self.open()
            self.customer_id = int(input("Customer ID: "))
            self.name = input("Customer Name : ")
            self.email = input("Email : ")
            self.password = input("Password : ")
            data = [(self.customer_id, self.name, self.email, self.password)]
            update_str = '''Update Customers set customer_id=%s,name=%s,email=%s,password=%s'''
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            self.close()
            return True

        except Exception as e:

            return e

    def delete_customer(self):
        try:
            self.open()
            customer_id = input("Enter Customer Id to be Deleted : ")
            delete_str = f'''Delete from Customers where customer_id = {customer_id}'''
            self.stmt.execute(delete_str)
            self.conn.commit()
            self.close()
            return True
        except Exception as e:
            return e

    def select_customer(self):
        try:
            select_str = '''select * from Customers'''
            self.open()
            self.stmt.execute(select_str)
            records = self.stmt.fetchall()
            self.close()
            print("Records in Customers Table : ")
            for i in records:
                print(i)
        except Exception as e:
            print(e)