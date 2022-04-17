#
# Setup server listening on ('localhost', 10000)
# receive data then send back XORed with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

import socket

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\n")

def bitwiseXOR(data):
  data = b(data)
  key = b("attackthehumans")
  value = key ^ b
  return value

host = 'localhost'
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    c, a = s.accept()
    with c:
        print('Connected by', a)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            data = bitwiseXOR(data)
            c.sendall(data)