# Default functions

import request
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
		f = open('book','r')
		b = f.read()

		self.book = json.loads(b)

	def test(self):
		print self.book

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

	def getBook(self):
		url = 'https://api.exchange.coinbase.com/products/BTC-USD/book?level=3'
		response = requests.get(url)
		text = response.content

		f = open('book','w')
		f.write(text)

		#j = json.loads(response.content)

		#print len(j)
		#for p in j:
		#	print p['display_name']

		print 'Book loaded'

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
