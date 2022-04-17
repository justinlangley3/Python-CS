#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#

import urllib.request
import urllib.parse

host    = "http://127.0.0.1:8082"
user    = "tweetbotuser"
key     = "tweetbotkeyv1"
status  = "alientest"

headers = {'x-api-key': key}

# buffer data in urlencoded format
data = urllib.parse.urlencode({"user": user, "status-update": status})
# cast buffered data to bytes as 'Request' will only accept an object in bytes
data = bytes(data.encode())

# create the POST request
req = urllib.request.Request(host, data=data, headers=headers)
# submit(open) the POST request, read, and decode the data
page = urllib.request.urlopen(req).read().decode()

# print data recieved
print(page)