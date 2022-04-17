#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

from zipfile import ZipFile
import itertools

# Function for extracting zip files
def extractFile(zf, password):
    try:
        zf.setpassword(pwd = bytes(password, 'utf-8'))
        zf.extractall()
        return True
    except Exception:
        pass

zipfilename = "C:/Users/justi/Desktop/trash.zip"
alphabet = '0123456789'
zf = ZipFile(zipfilename)

# Iterate through every possible 3 char combination
for c in itertools.product(alphabet, repeat=3):
    password = ''.join(c)
    print("Trying: " + password)
    
    if extractFile(zf, password):
        print('*' * 20)
        print('Password found: ' + password)
        print('Files extracted...')
        extractFile(zf, password)
        # Attempt to read extracted data
        with open('trash.txt', "r") as f:
          data = f.read()
          print(data)
          f.close()
        break