
import sqlite3

# connect to database
con= sqlite3.connect('Nitin.db')

#create a cursor
c=con.cursor()

# #create a table
c.execute("""CREATE TABLE movies(
            movie_name text,
            actor_name text,
            actress_name text,
            director_name text,
            year of release integer
    )""" )

many_entries =[
                ('Iron Man','Robert Downey Jr','Gwyneth Paltrow','Jon Favreau','2008'),
                ('Avatar','Sam Worthington','Zoe Saldana','James Cameron','2009'),
                ('The Godfather','Marlon Brando','Diane Keaton','Francis Ford Coppola','1972'),

            ]

c.executemany("INSERT INTO movies VALUES(?,?,?,?,?)",many_entries)




# #query the database
c.execute("SELECT * FROM movies")
it=c.fetchall()

for item in it:
    print(item)


c.execute("SELECT * FROM movies WHERE actor_name ='Robert Downey Jr'")
print("\n\n")
print(c.fetchall())

#commit command
con.commit()

#close connection
con.close()