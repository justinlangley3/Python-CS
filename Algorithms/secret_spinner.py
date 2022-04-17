from bs4 import BeautifulSoup
import commands
import os
import re
import requests
import subprocess

codes_url = 'http://www.bulldoghax.com/secret/codes'
spinner_url = 'http://www.bulldoghax.com/secret/spinner'
timelock = ""

spinner_resp = requests.get(spinner_url)
spinner_soup = BeautifulSoup(spinner_resp.text, "html.parser")
spinner_tag = spinner_soup.findAll('p')[0]
timelock = str(spinner_tag.contents)
timelock = re.sub(r"[\[\'\]]+", "", timelock)

flag = commands.getstatusoutput("curl --cookie 'timelock=" + timelock + " " + codes_url)
print(flag)