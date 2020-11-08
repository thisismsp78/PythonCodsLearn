import re
import requests

content=requests.get("https://en.isna.ir/rss").text
#print(content)
pattern="<title>(.*)</title>"
titles=re.findall(pattern,content)
for title in titles:
    print(title)
