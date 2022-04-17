from lxml import html
from xml.etree.ElementTree import parse
import urllib.request

speek_sess_id = ("speek_sess_id", None)
target = "http://www.wespeektogether.com/thedazman/status/74635478354"

for x in range (49, 50):
  headers = {'speek_sess_id': str(x)}
  req = urllib.request.Request(target, None, headers)
  
  with urllib.request.urlopen(req) as response:
    xmldoc = parse(response)
    page = response.read().decode('utf-8')
    print(xmldoc)
    user = xmldoc.xpath("/html/body/main/div[2]/div[2]/div[3]")
    print(x, user)