import mysql.connector
import csv

path = "C:\\Users\\Lenovo\\OneDrive\\Documents\\Datas for ML\\cs_50.csv"

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = None,
    database = "test"
    )

cursor = db.cursor()

# cursor.execute("create table language (id int  auto_increment,lang varchar(255),primary key(id))")
# cursor.execute("create table problems(problem_id int,problem varchar(255),foreign key (problem_id) references language(id))")

with open(path,"r") as f:
    cols = csv.DictReader(f)
    for col in cols:
        language = col["language"].strip()
        query = "insert into language (lang) values (%s)"
        cursor.executemany(query,[(language,)])
        result = cursor.lastrowid
        for prob in col["problem"].split(", "):
            query = "insert into problems (problem_id,problem) values (%s,%s)"
            cursor.executemany(query,[(result,prob)])
    db.commit()
