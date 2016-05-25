import MySQLdb

# Connect to Database
db = MySQLdb.connect(host='localhost',user='james',passwd='sorcier',db='dev')
cur = db.cursor()

# Drop table
cur.execute('drop table temp')

# Create table
cur.execute('create table temp (id int)')

# Insert
cur.execute('insert into temp (id) values (%d)' % 8)
db.commit()

# Select statement
cur.execute('select * from temp')

# View fetched data
for row in cur.fetchall():
	print row[0]

# Close connection
db.close()

