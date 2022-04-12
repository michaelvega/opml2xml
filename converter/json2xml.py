import json
import dicttoxml


def json_to_xml(path, filename):
    path = str(path + filename)
    with open(path) as f:
        data = json.load(f)

    xml = dicttoxml.dicttoxml(data)

    filename = "output.xml"
    path = "./output/"
    with open(f"{path}{filename}", "wb") as f:
        f.write(xml)
    print(str(__name__) + " done")
