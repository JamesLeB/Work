# Default functions

import requests
import json
import MySQLdb

'''
# Select statement
cur.execute('select * from temp')
# View fetched data
for row in cur.fetchall():
	print row[0]
'''

class james:
	book = ''
	book_cur = 0
	cur = ''
	db = ''

	def __init__(self):
		#f = open('book','r')
		#b = f.read()

		#self.book = json.loads(b)
		print 'From james class: finished __init__'

	def test(self):
		#print self.book
		print "this is a test"

	def openDB(self):
		# Connect to Database
		self.db = MySQLdb.connect(host='localhost',user='james',passwd='sorcier',db='dev')
		self.cur = self.db.cursor()

	def closeDB(self):
		# Close connection
		self.db.close()

	def createBookdb(self):
		self.openDB()
		# Create table
		self.cur.execute('create table book (id int)')
		self.closeDB()

	def dropBookdb(self):
		self.openDB()
		# Drop table
		self.cur.execute('drop table book')
		self.closeDB()

	def createMatchdb(self):
		self.openDB()
		# Create table
		self.cur.execute('create table matchs (ID int auto_increment primary key, mIndex int, time datetime, side varchar(10), price float, size float, dollars float, elapsedTime int)')
		#self.cur.execute('create table matchs (mIndex int, side varchar(10), price float, size float, dollars float)')
		self.closeDB()

	def dropMatchdb(self):
		self.openDB()
		# Drop table
		self.cur.execute('drop table matchs')
		self.closeDB()

	def loadBook(self):

		# Insert
		#cur.execute('insert into temp (id) values (%d)' % 8)
		#db.commit()

		bids = self.book['bids']
		asks = self.book['asks']
		print 'loading bids'
		for bid in bids:
			print bid

		print 'loading asks'

	def downloadbook(self):
		url = 'https://api.gdax.com/products/BTC-USD/book?level=3'
		response = requests.get(url)
		text = response.content
		f = open('book','w')
		f.write(text)
		print 'Book saved to disk'

	def readbook(self):
		print 'reading book'
		f = open('book','r')
		a = f.read()
		j = json.loads(a)

		keys = j.keys()
		for a in keys:
			print a

		print 'print keys'

		#bids = j['bids']
		#asks = j['asks']
		#sequence = j['sequence']

	def getBook(self):
		#url = 'https://api.exchange.coinbase.com/products/BTC-USD/book?level=3'
		#response = requests.get(url)
		#text = response.content

		# Write book to disk
		#f = open('book','w')
		#f.write(text)

		# Read book from disk
		#f = open('book','r')
		#a = f.read()
		#j = json.loads(a)
		#bids = j['bids']
		#asks = j['asks']
		#sequence = j['sequence']

		#print type(j)
		#print type(bids)

		#f1 = open('bids.csv','w')
		#for l in bids:
		#	ll = ','.join(l)
		#	f1.write(ll+"\n")
		#	print ll
		#f1.close()

		#f2 = open('asks.csv','w')
		#for l in asks:
		#	ll = ','.join(l)
		#	f2.write(ll+"\n")
		#	print ll
		#f2.close()

		#keys = bids.keys()
		#print keys

		# Write bids and asks to disk
		#f1 = open('bids.json','w')
		#f1.write(json.dumps(bids))
		#f2 = open('asks.json','w')
		#f2.write(json.dumps(asks))

		#print sequence

		#j = json.loads(response.content)

		#print len(j)
		#for p in j:
		#	print p['display_name']

		print 'Finished getting Book'
		return 'Return from getting book function'

	# Read book
	def rb(self):

		#keys = self.book.keys()
		#for a in keys:
		#	print a

		bids = self.book['bids']

		total = len(bids)

		bid = bids[self.book_cur]

		if self.book_cur == 0:
			print 'First bid!!'
		else:
			print 'Previous Bid '+str(self.book_cur-1)+" of "+str(total)+' :: '+str(bids[self.book_cur-1])

		print 'Current Bid '+str(self.book_cur)+" of "+str(total)+' :: '+str(bid)
		print 'Next Bid '+str(self.book_cur+1)+" of "+str(total)+' :: '+str(bids[self.book_cur+1])

		self.book_cur += 1

# Useful code

#print type(self.book)
