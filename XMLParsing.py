# Parsing XML
# Use of xml.etree.ElementTree
import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse('note.xml')
root = tree.getroot()

# Print the root element and its tag
print(root.tag)

# Iterate over child elements
for child in root:
    print(child.tag, child.text)