from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
    print("Connection Done!")
except Exception as e:
    print(e)
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS Technocolabs
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")
    session.execute("""use Technocolabs;""")
    print("creating keyspace Done!")
except Exception as e:
    print(e)
query = "CREATE TABLE IF NOT EXISTS songs "
query = query + "(year int, artist_name text, song_title text, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
    print("Table Creation Done!")
except Exception as e:
    print(e)
query = "INSERT INTO songs (album_name, artist_name, year, single, song_title)" 
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, ("Across The Universe", "The Beatles", 1970, False, "Let It Be"))
    print("Row inserted!")
except Exception as e:
    print(e)
    
try:
    session.execute(query, ("The Beatles", "Think For Yourself", 1965, False, "Rubber Soul"))
    print("Row inserted!")
except Exception as e:
    print(e)
query = 'SELECT * FROM songs'
try:
    rows = session.execute(query)
    print("Rows insertion done!")
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)

query = "select * from songs WHERE YEAR=1970 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)

session.shutdown()
cluster.shutdown()
print("Done!")