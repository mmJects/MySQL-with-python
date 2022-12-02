import cs50

db = cs50.SQL("mysql://root:YES@localhost:3306/online_movie_rating")

# fav = input("Input : ")
# row = db.execute("select collection_in_mil from movies where title = ?",fav)
# row = db.execute("select title from movies where collection_in_mil in (?)",[2.4,3])
# row = db.execute("select release_year from movies where title = :title",title="Titanic")
# n = db.execute("update movies set title = :name where title = 'Titanic'",name="Titanics")
# row = db.execute("select * from movies where title like 'F%'")

row = db.execute("select release_year from movies where title like ?","F"+"%")
for data in row:
    print(data)


# Race Conditions Solution
# db.execute("Begin Transcation")
# row = db.execute("select likes from post where post_id = ?",post_id)
# likes = row[0]["likes"]
# db.execute("update posts set likes = ? where id = ?",likes+1,post_id)
# db.execute("commit")