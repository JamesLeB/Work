
import requests
import json

#url = 'https://api.exchange.coinbase.com/products'
url = 'https://api.exchange.coinbase.com/products/BTC-USD/book?level=3'

response = requests.get(url)

text = response.content

f = open('book','w')
f.write(text)

#j = json.loads(response.content)

#print len(j)
#for p in j:
#	print p['display_name']

print 'Done :)'
