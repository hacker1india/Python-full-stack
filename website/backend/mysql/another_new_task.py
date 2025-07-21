import mysql.connector

# con = mysql.connector.connect(host = "localhost", user = "root", password = "Password")
# print(con)
# mycursor = con.cursor()
# mycursor.execute("create database ShopDB")
# con.commit()
# print('database created')
con = mysql.connector.connect(host = "localhost", user = "root", password = "Password", database = "ShopDB") 
mycursor = con.cursor()
# mycursor.execute("create table customers(cust_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100))")
# con.commit()
# print('customer table created')

# mycursor.execute("create table orders(order_id INT AUTO_INCREMENT PRIMARY KEY, cust_id INT, product_name VARCHAR(100), amount DECIMAL(10,2), order_date DATE, FOREIGN KEY(cust_id) REFERENCES customers(cust_id))")
# con.commit()
# print('order table created')

# query = """
# insert into customers(name, email) values(%s,%s)
# """
# data = [
#     ('Alice', 'alice@example.com'),
#     ('Bob', 'bob@example.com'),
#     ('Charlie', 'charlie@example.com')
# ]
# mycursor.executemany(query, data)
# con.commit()
# print('customers inserted')

query = """
insert into orders (cust_id, product_name, amount, order_date) VALUES(%s,%s,%s,%s)
"""
data = [
    (1, 'Laptop', 999.99, '2025-06-29'),
    (1, 'Mouse', 25.00, '2025-06-30'),
    (2, 'Keyboard', 45.00, '2025-06-30')
]
mycursor.executemany(query, data)
con.commit()
print('orders inserted')