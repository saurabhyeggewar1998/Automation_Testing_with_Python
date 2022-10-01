import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='pythonDB3',
                                         user='root',
                                         password='29071998')
    cursor = connection.cursor()
    sql_Delete_query = """Delete from Employee2 where ids = %s"""
    # row to delete
    ids = 118
    cursor.execute(sql_Delete_query, (ids,))
    connection.commit()
    print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to Delete record from table: {}".format(error))
