import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998", database="PythonDB3")
curser = myconn.cursor()

# curser.execute("select name, id, salary, dept_id from Employee1 order by salary")
curser.execute("select names, ids, salarys, dept_ids from Employee2 order by salarys desc")

result = curser.fetchall()
# result=curser.fetchone()
print(" names,  ids,  salarys,  dept_ids")
for r in result:
    print(r)
