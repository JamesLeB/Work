#!/usr/bin/python

import websocket

def on_message(ws, message):
	print message

def on_error(ws, error):
	print error

def on_close(ws):
	print "### closed ###"

def on_open(ws):
	ws.send('{"type": "subscribe","product_id": "BTC-USD"}')

ws=websocket.WebSocketApp("wss://ws-feed.exchange.coinbase.com",on_message = on_message, on_error = on_error, on_close = on_close)

ws.on_open = on_open

ws.run_forever()

print 'hello'

