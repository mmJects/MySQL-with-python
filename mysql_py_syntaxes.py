# This project follows along with https://realpython.com/python-mysql/

import mysql.connector

try:
    with mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = None,
        database = "online_movie_rating"
        ) as connection:
        # query = "create database online_movie_rating"
        # query = "show databases"
        # query = """
        #     create table movies(
        #         id int auto_increment primary key,
        #         title varchar(255),
        #         releae_year Year(4),
        #         genre varchar(255),
        #         collection_in_mil int
        #     )
        # """
        # query = "desc movies"
        # query = """
        #     create table reviewers(
        #         id int auto_increment primary key,
        #         first_name varchar(255),
        #         last_name varchar(255)
        #     )
        # """
        # query = """
        #     create table ratings(
        #         movie_id int,
        #         reviewer_id int,
        #         raing decimal(2,1),
        #         foreign key(movie_id) references movies(id),
        #         foreign key(reviewer_id) references reviewers(id),
        #         primary key(movie_id,reviewer_id)
        #     )
        # """
        # show_tables_query = "desc movies"
        # query = "alter table movies modify column collection_in_mil decimal(4,1)"
        # query = """
        #     insert into movies (title,releae_year,genre,collection_in_mil)
        #     values 
        #     ("Forrest Gump", 1994, "Drama", 330.2),
        #     ("3 Idiots", 2009, "Drama", 2.4),
        #     ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
        #     ("Good Will Hunting", 1997, "Drama", 138.1),
        #     ("Skyfall", 2012, "Action", 304.6),
        #     ("Gladiator", 2000, "Action", 188.7),
        #     ("Black", 2005, "Drama", 3.0),
        #     ("Titanic", 1997, "Romance", 659.2),
        #     ("The Shawshank Redemption", 1994, "Drama",28.4),
        #     ("Udaan", 2010, "Drama", 1.5),
        #     ("Home Alone", 1990, "Comedy", 286.9),
        #     ("Casablanca", 1942, "Romance", 1.0),
        #     ("Avengers: Endgame", 2019, "Action", 858.8),
        #     ("Night of the Living Dead", 1968, "Horror", 2.5),
        #     ("The Godfather", 1972, "Crime", 135.6),
        #     ("Haider", 2014, "Action", 4.2),
        #     ("Inception", 2010, "Adventure", 293.7),
        #     ("Evil", 2003, "Horror", 1.3),
        #     ("Toy Story 4", 2019, "Animation", 434.9),
        #     ("Air Force One", 1997, "Drama", 138.1),
        #     ("The Dark Knight", 2008, "Action",535.4),
        #     ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
        #     ("The Lion King", 1994, "Animation", 423.6),
        #     ("Pulp Fiction", 1994, "Crime", 108.8),
        #     ("Kai Po Che", 2013, "Sport", 6.0),
        #     ("Beasts of No Nation", 2015, "War", 1.4),
        #     ("Andadhun", 2018, "Thriller", 2.9),
        #     ("The Silence of the Lambs", 1991, "Crime", 68.2),
        #     ("Deadpool", 2016, "Action", 363.6),
        #     ("Drishyam", 2015, "Mystery", 3.0)
        # """
        # query = """
        #     insert into reviewers (first_name,last_name)
        #     values(%s,%s)
        # """
        # query_records = [
        #     ("Chaitanya", "Baweja"),
        #     ("Mary", "Cooper"),
        #     ("John", "Wayne"),
        #     ("Thomas", "Stoneman"),
        #     ("Penny", "Hofstadter"),
        #     ("Mitchell", "Marsh"),
        #     ("Wyatt", "Skaggs"),
        #     ("Andre", "Veiga"),
        #     ("Sheldon", "Cooper"),
        #     ("Kimbra", "Masters"),
        #     ("Kat", "Dennings"),
        #     ("Bruce", "Wayne"),
        #     ("Domingo", "Cortes"),
        #     ("Rajesh", "Koothrappali"),
        #     ("Ben", "Glocker"),
        #     ("Mahinder", "Dhoni"),
        #     ("Akbar", "Khan"),
        #     ("Howard", "Wolowitz"),
        #     ("Pinkie", "Petit"),
        #     ("Gurkaran", "Singh"),
        #     ("Amy", "Farah Fowler"),
        #     ("Marlon", "Crafford"),
        # ]
        # query = """
        #         INSERT INTO ratings
        #         (raing, movie_id, reviewer_id)
        #         VALUES ( %s, %s, %s)
        # """
        # query_records = [
        #         (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
        #         (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
        #         (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
        #         (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
        #         (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
        #         (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
        #         (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
        #         (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
        #         (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
        #         (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
        #         (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
        #         (9.8, 13, 1)
        # ]
        # query = "select title from movies where collection_in_mil > 200 order by collection_in_mil desc limit 5"
        # query_concat = """
        #     select concat(title,"(",releae_year,")"),collection_in_mil
        #     from movies order by collection_in_mil desc limit 5
        # """
        # query_join = """
        #       select title,avg(raing) as average_rating from ratings
        #       inner join movies on movies.id = ratings.movie_id
        #       group by movie_id order by average_rating asc limit 5
        # """
        select_query = """
                select concat(first_name," ",last_name),count(*) as num from reviewers
                inner join ratings on reviewers.id = ratings.reviewer_id
                group by reviewer_id order by num desc limit 5
        """
        with connection.cursor() as cursor:
            # cursor.execute(query)
            # cursor.executemany(query,query_records)
            # connection.commit()
            # cursor.execute(query_concat)
            # cursor.execute(query_join)
            cursor.execute(select_query)
            result = cursor.fetchall()
            for i in result:
                print(i)
except mysql.connector.Error as e:
    print(e)

# cursor = db.cursor()
# prob = input("")
# mysql_cmd = ("select * from favorite where problem = (%s) limit 10",prob)
# mysql_cmd = ("select * from favorite where problem = 'Mario' limit 10")
# cursor.execute(mysql_cmd)

# for data in cursor:
#     print(data[1])