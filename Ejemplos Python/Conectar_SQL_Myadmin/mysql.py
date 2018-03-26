import MySQLdb

con=MySQLdb.connect(host="localhost",db="test")
cur = db.cursor()

cur.execute("SELECT * FROM hola")

con.close()
