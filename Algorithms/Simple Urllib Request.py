import urllib.request

#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout if this occurs try narrowing
# down your search
#

site = "http://127.0.0.1:8082"

for x in range (5500, 5601):
  headers = {'x-api-key': str(x)}
  req = urllib.request.Request(site, None, headers)
  
  with urllib.request.urlopen(req) as response:
    page = response.read()
    print(page)