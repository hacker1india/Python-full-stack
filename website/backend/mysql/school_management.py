import mysql.connector

# con = mysql.connector.connect(host="localhost", user="root",password="Password")
# print(con)
# print("connected successfully")
# mycursor = con.cursor()
# mycursor.execute("create database studentsData")
# print("database created")

con = mysql.connector.connect(host="localhost", user="root",password="Password",database="studentsData")
mycursor = con.cursor()
# mycursor.execute("create table students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT, email VARCHAR(255))")
# print("tabel1 created")
# query = """
# insert into students(name,age,email) values (%s,%s,%s)
# """
# data = [
#     ("Rahul",21,"rahul@gmail.com"),
#     ("Rohan",21,"rohan@gmail.com"),
#     ("Raju",22,"raju@gmail.com"),
#     ("Ramu",22,"ramu@gmail.com"),
# ]
# mycursor.executemany(query,data)
# con.commit()
# print("Commited success")
# mycursor.execute("select * from students")
# for i in mycursor:
#     print(i)
# mycursor.execute("create table courses(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),course VARCHAR(255))")
# print("tabel2 created")
# query = """
# insert into courses(name,course) values (%s,%s)
# """
# data = [
#     ("Rahul","CSE"),
#     ("Rohan","ECE"),
#     ("Raju","EEE"),
#     ("Ramu","MECH"),
# ]
# mycursor.executemany(query,data)
# con.commit()
# print("Commited success")
# mycursor.execute("select * from courses")
# for i in mycursor:
#     print(i)

# mycursor.execute("create table grades(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),course VARCHAR(255),avarage FLOAT, grade VARCHAR(10))")
# print("tabel3 created")
# query = """
# insert into grades(name,course,avarage,grade) values (%s,%s,%s,%s)
# """
# data = [
#     ("Rahul","CSE",79.9,"A"),
#     ("Rohan","ECE",69.9,"B"),
#     ("Raju","EEE",88.8,"A+"),
#     ("Ramu","MECH",90.0,"O"),
# ]
# mycursor.executemany(query,data)
# con.commit()
# print("Commited success")
# mycursor.execute("select * from grades")
# for i in mycursor:
#     print(i)
