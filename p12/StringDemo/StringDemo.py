import xml.etree.ElementTree as ET

names=ET.fromstring("<?xml version=\"1.0\" encoding=\"utf-8\"?><names><name>C++</name></names>")
print(len(names))
print(names[0].text)