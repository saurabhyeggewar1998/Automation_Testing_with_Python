import mysql.connector


def show_database():
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="29071998")
    curser = myconn.cursor()
    curser.execute("show databases")
    for db in curser:
        print(db)


show_database()
