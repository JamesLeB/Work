# Default functions

import requests
import json

class james:
	book = ''
	book_cur = 0

	def __init__(self):
		f = open('book','r')
		b = f.read()

		self.book = json.loads(b)

	def test(self):
		print self.book

	def loadBook(self):
		bids = self.book['bids']
		asks = self.book['asks']
		print 'loading bids'
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
