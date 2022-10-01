import mysql.connector


def test_show_database():

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998")
    curser = myconn.cursor()
    curser.execute("show databases")
    for db in curser:
        print(db)

def test_create_database():
    import mysql.connector

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998")
    curser = myconn.cursor()
    curser.execute("create database PythonDB7")

def test_create_table():

    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998",database="PythonDB7")
    curser = myconn.cursor()
    curser.execute("create table Employee2(names varchar(20) not null, ids int(20) not null primary key, salarys float "
                   "not null, Dept_ids int not null)")


def test_insert_table():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998", database="PythonDB7")
    curser = myconn.cursor()

    sql = "insert into Employee2(names, ids, salarys, dept_ids) values (%s, %s, %s, %s)"

    records = [("lele", 117, 70000.00, 201),
               ("jile", 118, 80000.00, 205)]

    try:
        # inserting the values into the table
        curser.executemany(sql, records)

        # commit the transaction
        myconn.commit()

    except:
        myconn.rollback()

    print(curser.rowcount, "record inserted!")
    myconn.close()




def test_update():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998", database="PythonDB7")
    curser = myconn.cursor()

    curser.execute("update Employee2 set salarys=78000.00 where names='lele'  ")
    # myconn.commit()

def test_delete():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998", database="PythonDB6")
    curser = myconn.cursor()

    curser.execute("delete from Employee2 where names='lele'")
    myconn.commit()
    print("Record deleted !!!!!!")


