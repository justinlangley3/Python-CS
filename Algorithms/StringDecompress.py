#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send GET_KEY to download a string.
# The string is compressed with a common algorithm found in many
# websites. Uncompress the string and print it to get the flag.
#

import socket
import time
import zlib
  
host = "localhost"
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("GET".encode())
time.sleep(0.0001)

data = s.recv(1024)
print(data)
print("\n")

print(zlib.decompress(data, 16+zlib.MAX_WBITS))