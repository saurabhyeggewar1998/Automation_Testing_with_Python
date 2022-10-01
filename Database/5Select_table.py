import mysql.connector

db=mysql.connector.connect(host="localhost", user="root", passwd="29071998",database="PythonDB3")

cursor=db.cursor()

cursor.execute("select * from Employee2")

for table_name in cursor:
   print(table_name)