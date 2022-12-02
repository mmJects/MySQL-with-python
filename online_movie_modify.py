from mysql.connector import connect,Error


movie_id = input("Movie ID : ")
reviewer_id = input("Reviewer ID : ")
new = input("New Rating : ")

query = """
    update ratings
    set raing = %s
    where movie_id = %s and reviewer_id = %s;

    select * from ratings 
    where movie_id = %s and reviewer_id = %s;

"""
val_tuple = (
    new,
    movie_id,
    reviewer_id,
    movie_id,
    reviewer_id
)

title = input("Movie name: ")

search_query = """
    select id from movies where title = %s 
"""

try:
    with connect(
        host = "localhost",
        username = "root",
        password = None,
        database = "online_movie_rating"
    ) as connection:
        with connection.cursor() as cursor:
        #     for result in cursor.execute(query,val_tuple,multi=True):
        #         if result.with_rows:
        #             print(result.fetchall())
        #     connection.commit()
            cursor.execute(search_query,(title,))
            result = cursor.fetchall()
            print(*result)
except Error as e:
    print(e)