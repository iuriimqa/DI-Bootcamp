import psycopg2
connection = psycopg2.connect(host='localhost', user='postgres', password='admin', dbname='restaurant')
cursor = connection.cursor()

class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # method to delete position from database
    def save(self):
        query = f"insert into menu (name, price) values ('{self.name}',{self.price});"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            # connection.close()

    def delete(self):
        query = f"delete from menu where name = '{self.name}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            # connection.close()

    def update(self,name,price):
        query = f"update menu set name ='{name}', price={price} where name ='{self.name}' and price = {self.price}"
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()


    def all(cls):
        query = f"select* from menu"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = print(cursor.fetchall())
        return result

    def get_by_name(name):
        query = f"select * from menu where name = '{name}'"
        cursor.execute(query)
        result= cursor.fetchall()
        if result:
            return print(result)
        else:
            return print(None)

        connection.close()

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all(MenuItem)

# MenuItem.get_by_name('Burger')


