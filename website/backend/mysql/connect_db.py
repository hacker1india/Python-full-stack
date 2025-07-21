import mysql.connector
from datetime import date
# con = mysql.connector.connect(host="localhost",user="root",password="Password")
# print(con)
# print("connected successfully!")

# mycursur = con.cursor()
# mycursur.execute("create database lpu")
# print("database created successfully")
# mycursur.execute("show databases")
# for i in mycursur:
#     print(i)
con = mysql.connector.connect(host="localhost",user="root",password="Password" ,database="lpu")
mycursur = con.cursor()
# mycursur.execute("create table students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT,fee FLOAT,join_date DATE,is_active BOOLEAN)")
# print("table created successfully")

# query ="""
# insert into students(name,age,fee,join_date,is_active) values(%s,%s,%s,%s,%s)
# """
# data = ("Rahul",20,50000.0,date(2025,1,16),True)
# mycursur.execute(query,data)
# con.commit()
# print(mycursur.rowcount,"record inserted")

# query ="""
# insert into students(name,age,fee,join_date,is_active) values(%s,%s,%s,%s,%s)
# """
# data =[("Rayudu",20,50000.0,date(2025,1,16),False),
#        ("Rambabu",21,60000.0,date(2025,2,17),True),
#        ("Ramesh",22,70000.0,date(2025,3,18),False),
#        ("Rajesh",23,80000.0,date(2025,4,19),True),
#        ("Ramu",24,90000.0,date(2025,5,11),False),
#        ("Raju",25,40000.0,date(2025,6,12),True),
# ]
# mycursur.executemany(query,data)
# con.commit()
# print(mycursur.rowcount,"record inserted")

# mycursur.execute("select * from students")
# for i in mycursur:
#     print(i)

# mycursur.execute("select * from students where age=24")
# for i in mycursur:
#     print(i)

# mycursur.execute("select * from students limit 3")
# for i in mycursur:
#     print(i)

# mycursur.execute("select id,name from students")
# for i in mycursur:
#     print(i)

# mycursur.execute("select id,name from students where age=21")
# for i in mycursur:
#     print(i)


#update
# query = """
# update students set age=32 where age=25
# """
# mycursur.execute(query)
# con.commit()
# print(mycursur.rowcount,"updated")

# mycursur.execute("select * from students")
# mydata = mycursur.fetchall()
# for i in mydata:
#     print(i)

# mycursur.execute("select * from students")
# mydata = mycursur.fetchmany()
# for i in mydata:
#     print(i)

# mycursur.execute("select * from students")
# mydata = mycursur.fetchsets()
# for i in mydata:
#     print(i)

# mycursur.execute("select * from students")
# mydata = mycursur.fetchone()
# for i in mydata:
#     print(i)

# mycursur.execute("delete from students where age=32")
# print(mycursur.rowcount,"record deleted")

#ROLLBACK won't work in drop,alter,create 
#ROLLBACK will work in delete,update,insert

# mycursur.execute("drop table students")
# print("schema deleted")   