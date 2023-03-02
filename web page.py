import json
import requests
import urllib.request
import urllib.parse
import http.client
print("Enter the City name : ", end = ' ')
query = input()
print("Enter the State or Region : ",end = ' ')
region = input()
r = requests.get("https://api.qwant.com/api/search/images",
                 params={
                     'count': 50,
                     'q': query,
                     't': 'images',
                     'safesearch': 1,
                     'locale': 'en_US',
                     'uiv': 4
                 },
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                 }
                 )

response = r.json().get('data').get('result').get('items')
urls = [r.get('media') for r in response]

conn = http.client.HTTPConnection('api.positionstack.com')
parameters = urllib.parse.urlencode({
        'access_key': 'd1e4e5547bceef63abb78812f825d3fc',
        'query': query,
        'region': region,
        'limit': 1, })

conn.request('GET', '/v1/forward?{}'.format(parameters))
result = conn.getresponse()
data = result.read()
data = data.decode('utf-8')
data = json.loads(data)
data = data['data']
data = data[0]
print("County :{}".format(data['county']))
print("Region : {}".format(data['region']))
print("Country: {}".format(data['country']))
print("Continent : {}".format(data['continent']))
print("Latitude : {}".format(data['latitude']))
print("Longitude : {}".format(data['longitude']))