#
# Find the valid png file in the /tmp directory. Using magic bytes.
# The code is hidden in this file.
#

import os
import re

# Function to search file tree and gather an array of file names
def createFileList(directory, files):
  for root, _, filenames in os.walk(directory, topdown=True):
    for filename in filenames:
      files.append(os.path.join(root, filename))
  return files

# Function to remove any files that are not PNGs
def removeBadFiles(files):
  # regex to match PNG files
  pattern = '^.*\.(png)$'
  
  # iterate and remove non-matches
  for file in files:
    if re.match(pattern, file):
      # do nothing
      pass
    else:
      # remove bad file
      files.remove(file)
      
  # return modified list
  return files

# function to probe file for matching magic bytes
def testMagicBytes(file):
  filename = file
  # png magic bytes
  magic_numbers = {'png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])}
  # maximum bytes to read, is the size (in bytes) of our magic_numbers object
  max_read_size = max(len(m) for m in magic_numbers.values())
  
  # open the file in read bytes mode
  with open(file, "rb") as f:
    file_head = f.read(max_read_size)
    if file_head.startswith(magic_numbers['png']):
      print("Found valid PNG: " + filename)
      return filename
  return None
  
directory = "/tmp"
files     = []

files = createFileList(directory, files)
files = removeBadFiles(files)

# Loop through list of files we've gathered
for file in files:
  # test each file for magic bytes matching a PNG
  testFile = testMagicBytes(file)
  if testFile is None:
    # if None is returned, the file is not a PNG, do nothin
    pass
  else:
    # file is a PNG, open in read byte mode
    with open(testFile, "rb") as f:
      # read byte data to see if there are any strings
      data = f.read()
      # print the data
      print(data)
      # close the file
      f.close()