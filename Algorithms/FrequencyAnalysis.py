#
# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#


import socket
import string


# Letter occurence frequencies, values are from Oxford English Dictionary
letterValidity = dict(zip(string.ascii_uppercase,
                          [.0850,.0207,.0454,.0338,.1116,.0181,.0247,
                           .0300,.0754,.0197,.0110,.0549,.0301,.0654,
                           .0716,.0318,.0196,.0758,.0574,.0695,.0363,
                           .0100,.0129,.0290,.0178,.0272]))

# Translating of characters from one to another, all uppercase from A to Z
chars_tables = [str.maketrans(string.ascii_uppercase,
                              string.ascii_uppercase[i:]+string.ascii_uppercase[:i])
                for i in range(26)]

# Returns validity (the likely correctness, of all chars in msg)
def Validity(msg):
  return sum(letterValidity.get(char, 0) for char in msg)

'''
Function for the deciphering of caesar cipher messages,
based on the frequency letters commonly occur in English

Converts to uppercase,
Makes call to chars_tables for character conversions,

Yields a validity sum of all chars in message,
and yields the deciphered text in the form:
(V, 'Message') - a list containing two elements

Called as:  max(Decipher(msg))[0 or 1]

 [0 or 1] is optional:
  0 returns the Validity sum 
  1 returns the string element
  if not specified (no brackets), returns both
'''
def Decipher(msg):
  msg = msg.upper()
  for chars_table in chars_tables:
    txt = msg.translate(chars_table)
    yield Validity(txt), txt


# Declarations
buff  = 1024                                                # Buffer size
host  = ('localhost', 10000)                                # Host ip, port
s     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP Socket

# Connect to host, initiate request
s.connect(host)
s.send('GET'.encode())

'''
Retrieve data and format:
Strip garbage from head and tail of message
Split into separate lines for deciphering
'''
data = s.recv(buff)[79:-1].splitlines()

for line in data:
  line = line.decode().strip()
  print(line)
print("\n")

'''
For each received message, strip the message of line returns,
call Decipher() to decipher the line message, return only the string
value returned by Decipher(), and append to out with a newline
'''
out = ''
for line in data:
  line  = line.decode().strip()
  out += str(max(Decipher(line))[1]) + "\n"

print(out)
# Transmit deciphered messages back to host
s.send(out.encode())
data = s.recv(1024)
print(data.decode())

# Terminate connection to host
s.close()