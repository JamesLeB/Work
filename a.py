#!/usr/bin/python

import websocket

out_file = open('out_file','w')

def on_message(ws, message):
	out_file.write(message+'\n')
	print message
	print 

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

print "Well now what?"

s()
