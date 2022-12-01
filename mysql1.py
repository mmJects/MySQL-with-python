import mysql.connector
from mysql.connector import errorcode

db = input("Plese type your using database : ")

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=None,
        database = db
        )
except mysql.connector.Error as err:
    print(err)
else:
    cursor = db.cursor()
    
sql_cmd = "select name,phone from customers "
cursor.execute(sql_cmd)

results = cursor.fetchall()

for row in results:
    print(row)