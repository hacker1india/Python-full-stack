import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Password", database="studentsData")
# print(con)
mycursor=con.cursor()
# mycursor.execute("create table employee(id INT, name VARCHAR(255),dept_id INT)")
# print("table created")

# query="""
# insert into employee(id,name,dept_id) values(%s,%s,%s)
# """
# data = [
#     (1, 'John', 10),
#     (2, 'Anna', 20),
#     (3, 'Peter', 30),
#     (4, 'Linda', 40),
#     (5, 'Tom', 50)
# ]
# mycursor.executemany(query,data)
# con.commit()
# print(mycursor.rowcount,"data inserted")

# mycursor.execute("create table department(id INT, dept_name VARCHAR(255))")
# print("table created")

# query="""
# insert into department(id,dept_name) values(%s,%s)
# """
# data = [
#     (10, 'ENGR'),
#     (20, 'Sci'),
#     (30, 'Arts'),
#     (40, 'CSE'),
#     (50, 'ML')
# ]
# mycursor.executemany(query,data)
# con.commit()
# print(mycursor.rowcount,"data inserted")

#********** INNER JOIN ***********

# query = """
# select employee.name,department.dept_name from employee 
# inner join department on employee.dept_id = department.id
# """
# mycursor.execute(query)
# results=mycursor.fetchall()
# for i in results:
#     print(f"Employees:{i[0]} Departments:{i[1]}")

#********** LEFT JOIN ***********

# query = """
# select employee.name,department.dept_name from employee 
# left join department on employee.dept_id = department.id
# """
# mycursor.execute(query)
# results=mycursor.fetchall()
# for i in results:
#     print(f"Employees:{i[0]} Departments:{i[1]}")

#********** RIGHT JOIN ***********

# query = """
# select employee.name,department.dept_name from employee 
# right join department on employee.dept_id = department.id
# """
# mycursor.execute(query)
# results=mycursor.fetchall()
# for i in results:
#     print(f"Employees:{i[0]} Departments:{i[1]}")