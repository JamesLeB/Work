#!/usr/bin/python

import websocket
import json

import sys
sys.path.append('class')
from james import *

#out_file = open('out_file','w')

a = 1

def on_message(ws, message):
	global a
	a += 1

#	out_file.write(message+'\n')
#	print message

	j = json.loads(message)
	mtype = j['type']

	if mtype == 'open':
		print str(a) + ' OPEN!!'
	elif mtype == 'done':
		print str(a) + ' DONE!!'
	elif mtype == 'received':
		print str(a) + ' RECEIVED!!'
	elif mtype == 'match':
		print str(a) + ' MATCH!!'
	else:
		print str(a) +' Unknown!! ' + mtype
		ws.close()
	
	print ''

def on_error(ws, error):
	print error

def on_close(ws):
	print "### closed ###"

def on_open(ws):
	ws.send('{"type": "subscribe","product_id": "BTC-USD"}')

def s():
	ws=websocket.WebSocketApp("wss://ws-feed.exchange.coinbase.com",on_message = on_message, on_error = on_error, on_close = on_close)

	ws.on_open = on_open

	ws.run_forever()

print "Stating websocket?"

j = james()
#j.getBook()

#s()
