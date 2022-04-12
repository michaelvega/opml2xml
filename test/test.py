import opml
from opyml import OPML, Outline

document = opml.parse('http://hosting.opml.org/dave/validatorTests/clean/subscriptionList.opml')


filenmame = "opmltest.opml"
path = "./res/"

# Throws exception
#with open(f'{path}{filenmame}', 'w') as file:
#    file.write(outline)

xml = document.to_xml()

print()
