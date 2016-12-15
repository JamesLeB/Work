#!/usr/bin/python

import websocket
import json
import MySQLdb

import sys
#sys.path.append('class')
from james import *

out_file = open('out_file','w')

a = 1
j = james()


#db = MySQLdb.connect(host='localhost',user='james',passwd='sorcier',db='dev')
#cur = db.cursor()

def on_message(ws, message):
	global a
	global db
	global cur
	global j
	
	if a == 1:
		print 'First message recieved'

	if a == 10:
		print 'Stream running'
		#j.downloadbook()

	a += 1

	print str(a) + ' :: ' + message
	out_file.write(message+'\n')

	#j = json.loads(message)
	#mtype = j['type']

	#if mtype == 'open':
		#print str(a) + ' OPEN!!'
	#elif mtype == 'done':
		#print str(a) + ' DONE!!'
	#elif mtype == 'received':
		#print str(a) + ' RECEIVED!!'
	#elif mtype == 'match':
	#if mtype == 'match':
		#print str(a) + ' MATCH!!'
		#print message
		#dollar = float(j['price']) * float(j['size'])
		#print str(a) + ' ' + j['side'] + ' : ' + j['price'] + ' : ' + j['size'] + ' : ' + str(dollar)
		#print ''
		#out_file.write(message+'\n')

		#cur.execute("insert into trades (id,side,price,size,dollars) values (%d,'%s',%f,%f,%f)" % (a,j['side'],float(j['price']),float(j['size']),dollar))
		#db.commit()

	#else:
		#print str(a) +' Unknown!! ' + mtype
		#ws.close()
	
	#print ''

def on_error(ws, error):
	print error

def on_close(ws):
	print "### closed ###"

def on_open(ws):
	ws.send('{"type": "subscribe","product_id": "BTC-USD"}')

def s():
	ws=websocket.WebSocketApp("wss://ws-feed.gdax.com",on_message = on_message, on_error = on_error, on_close = on_close)

	ws.on_open = on_open

	ws.run_forever()

print "Init Script done"
s()
