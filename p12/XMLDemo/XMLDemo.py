import xml.etree.ElementTree as ET

document=ET.parse("names.xml")
print(document)
root=document.getroot()
for name in root:
    print(name.text)

print("-----------------")
print(root[0].text)
print(len(root))