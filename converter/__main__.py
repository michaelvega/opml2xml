from converter.opml2json import *
from converter.json2xml import *


ompl_to_json(path="./res/", filename="subscriptionList.opml")
json_to_xml(path="./res/", filename="temp.json")

print("done!")
