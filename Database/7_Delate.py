import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998", database="PythonDB3")
curser = myconn.cursor()

curser.execute("delete from Employee2 where names='lele'")
myconn.commit()
print("Record deleted !!!!!!!!!!!!!!")