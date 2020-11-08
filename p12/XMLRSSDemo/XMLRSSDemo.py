import xml.etree.ElementTree as ET
import requests

content=requests.get("https://en.isna.ir/rss").text
rss=ET.fromstring(content)
#print(rss)
channel=rss[0]
#print(channel)
for item in channel:
    #print(item)
    if item.tag=="item":
        print(item[0].text)