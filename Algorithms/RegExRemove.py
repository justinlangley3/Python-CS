#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#
import re

# remove characters that are not contained in the pattern
with open("/tmp/destroymoonbase.gif") as f:
  pattern = "[^a-zA-Z0-9]+"
  data = f.read()
  data = re.sub(pattern, '', data)
  print(data)
  f.close()