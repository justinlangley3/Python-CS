#
# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt write a script
# which will use that text to build a message using the received word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\n)
#
import re
import socket
import time

def fetchWord(nums, doc):
    word = ""
    nums = nums.split(",")
    
    # select paragraph
    p = doc[int(nums[0])-1]
    p = re.split(r"[\n]+", p)
    
    # select the sentence
    s = p[int(nums[1])-1]
    # strip punctuation
    s = re.sub(r"[,.!?\'\"]+", "", s)
    # split into words
    w = s.split()
    # select correct word
    word = w[int(nums[2])-1]
    return word

def buildMessage(numbers, document):
  code = ''
  for x in numbers:
    word = fetchWord(x, document)
    code += word
    code += "\n"
  return code

# store backdoor.txt
document = open("backdoor.txt", "r").read().split("\n\n")

# declarations
host = 'localhost'
port = 10000

# connect to host and retrieve data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send("letmein".encode())
time.sleep(0.0001)
data = s.recv(1024).decode().splitlines()

# build secret message
message = buildMessage(data, document).encode()
# send it
s.send(message)
time.sleep(0.0001)

# capture flag
flag = s.recv(1024).decode()
print(flag)

