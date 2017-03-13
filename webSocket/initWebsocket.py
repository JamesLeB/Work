#!/usr/bin/python

import websocket
import json
import MySQLdb
import re
import time

import sys
#sys.path.append('class')
from james import *

out_file = open('out_file','w')

a = 1
b = time.time()
print 'Call function to make james object'
j = james()


print 'Connect to database'
db = MySQLdb.connect(host='localhost',user='james',passwd='sorcier',db='dev')
cur = db.cursor()


print 'Create dabase tables'
j.dropMatchdb()
j.createMatchdb()


def on_message(ws, message):
	global a
	global b
	global db
	global cur
	global j
	
	if a == 1:
		print 'First message recieved'

	if a == 10:
		print 'Stream running'
		#j.downloadbook()

	a += 1

	#print str(a) + ' :: ' + message
	#out_file.write(message+'\n')

	js = json.loads(message)
	mtype = js['type']

	#if mtype == 'open':
		#print str(a) + ' OPEN!!'
	#elif mtype == 'done':
		#print str(a) + ' DONE!!'
	#elif mtype == 'received':
		#print str(a) + ' RECEIVED!!'
	#elif mtype == 'match':
	if mtype == 'match':
		print str(a) + ' MATCH!!'
		#print message
		dollar = float(js['price']) * float(js['size'])
		caltime = js['time']
		caltime = re.sub('T',' ',caltime)
		caltime = re.sub('\.\d{6}Z','',caltime)
		#print str(a) + ' ' + j['side'] + ' : ' + j['price'] + ' : ' + j['size'] + ' : ' + str(dollar)
		#print ''
		#out_file.write(message+'\n')

		elapsedTimeInt = time.time() - b
		c = time.asctime(time.localtime(b))
		d = time.asctime(time.localtime(time.time()))

		cur.execute("insert into matchs (mIndex,side,price,size,dollars,time,elapsedTime) values (%d,'%s',%f,%f,%f,'%s','%s')" % (a,js['side'],float(js['price']),float(js['size']),dollar,caltime,elapsedTimeInt))
		db.commit()

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

print "Open websocket"
s()
