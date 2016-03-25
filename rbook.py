import json

f = open('book','r')
book = f.read()

b = json.loads(book)

print type(b)

keys = b.keys()

for a in keys:
	print a

print 'loading bids'

bids = b['bids']

print len(bids)

bid = bids[0]
print bid
