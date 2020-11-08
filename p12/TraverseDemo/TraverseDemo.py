import xml.etree.ElementTree as ET
import requests

content=requests.get("https://en.isna.ir/rss").text
rss=ET.fromstring(content)
print(rss.findall("channel/item"))
"""
channel=rss[0]
for item in channel:
    if item.tag=="item":
        print(item[0].text)
"""