import requests
import json

content=requests.get("https://gist.githubusercontent.com/keeguon/2310008/raw/bdc2ce1c1e3f28f9cab5b4393c7549f38361be4e/countries.json").text
content=content.replace("{name:","{\"name\":").replace("code:","\"code\":").replace("',","\",").replace(" '"," \"").replace("'}","\"}").replace("\\"," ")
#print(content)
data=json.loads(content)
for country in data:
    print(country["name"]," | ",country["code"])
