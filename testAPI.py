import hashlib
import hmac
import json
import requests

# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'a66ca0d2fc1ac708f5a6d470c081ea14'
API_SECRET = b'f4a407c8b19b71932776b574d48f2600'

def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
response = requests.get(API_HOST + '/api/servertime')
ts = int(response.text)
print('Server time: ' + response.text)

# check balances
header = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-BTK-APIKEY': API_KEY,
}



data = {
	'ts': ts,
}
signature = sign(data)
data['sig'] = signature

print('Payload with signature: ' + json_encode(data))

def balance():
    response = requests.post(API_HOST + '/api/market/balances', headers=header, data=json_encode(data))
    print('Balances: ' + response.text)

#GET Crypto Data
def symbol ():
    response = requests.get(API_HOST + '/api/market/symbols')
    print(response.text)

#GET Coin Prices
def ticker():
    response = requests.get(API_HOST + '/api/market/ticker' ,params='sym=THB_BTC')
    print(response.text)

#Get bid order
def bids():
    response = requests.get(API_HOST + '/api/market/bids' ,params='sym=THB_BTC&lmt=1')
    print(response.text)

def buy():
    response = requests.get(API_HOST + '/api/market/place-bid' ,params='sym=THB_BTC&lmt=1', data=json_encode(data))
    print(response.text)

#symbol()
# ticker()
buy()