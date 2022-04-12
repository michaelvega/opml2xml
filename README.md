# opml2xml
Converts OPML files to XML. First converts OPML to JSON then JSON to XML. 

### Functions:
* ompl_to_json(path, filename) -> json
* json_to_xml(path, filename) -> xml

### Start Guide
```
from converter.opml2json import *
from converter.json2xml import *


ompl_to_json(path="./res/", filename="subscriptionList.opml")
json_to_xml(path="./res/", filename="temp.json")

print("done!")
```
