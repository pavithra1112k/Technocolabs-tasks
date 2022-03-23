import psycopg2
try: 
    conn = psycopg2.connect("host=localhost port=5432 dbname=studentdb user=postgres password=Ram@123")
    print("Database connection Done")
except psycopg2.Error as e: 
    print("Error: Could not make connection to the Postgres database")
    print(e)
try: 
    cur = conn.cursor()
    print("Connection to curser Done")
except psycopg2.Error as e: 
    print("Error: Could not get curser to the Database")
    print(e)
conn.set_session(autocommit=True)
print("Done")
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS music_library (album_name varchar, artist_name varchar, year int);")
    print("Table creation Done")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
try: 
    cur.execute("select count(*) from music_library")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)
    
print(cur.fetchall())
try: 
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                 VALUES (%s, %s, %s)", \
                 ("Let It Be", "The Beatles", 1970))
    print("Row insertion Done")
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO music_library (album_name, artist_name, year) \
                 VALUES (%s, %s, %s)", \
                 ("Rubber Soul", "The Beatles", 1965))
    print("Row insertion Done")
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
try: 
    cur.execute("SELECT * FROM music_library;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
   print(row)
   row = cur.fetchone()
try: 
    cur.execute("DROP table music_library")
    print("deleting the table Done!")
except psycopg2.Error as e: 
    print("Error: Dropping table")
    print (e)
cur.close()
conn.close()
print("Closing cursor and connection Done!")