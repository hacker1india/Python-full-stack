import mysql.connector

# con = mysql.connector.connect(host="localhost",user="root",password="Password")
# print(con)
# mycursor = con.cursor()
# mycursor.execute("create database Inventory")
# con.commit()
# print("Database created")

con = mysql.connector.connect(host="localhost",user="root",password="Password",database="Inventory")
mycursor=con.cursor()
# mycursor.execute("create table products(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),price FLOAT,stock INT)")    
# con.commit()
# print("Table created")
query="""
insert into products(name,price,stock) values(%s,%s,%s)
"""
data=[
    ("Apple",100,100),
    ("Banana",50,200),
    ("Cherry",70,300),
    ("Date",80,400),
    ("Elderberry",90,500)
]
mycursor.executemany(query,data)
con.commit()
print("Data inserted")