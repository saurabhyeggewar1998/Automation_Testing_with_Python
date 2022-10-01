import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="29071998",
  database="PythonDB3"
)

mycursor = mydb.cursor()

sql = "UPDATE Employee2 SET salarys = 8200.0 WHERE salarys = 70000.0"

mycursor.execute(sql)

mydb.commit()

print("Successful Updated")