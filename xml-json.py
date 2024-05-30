import xmltodict
import json

# Sample XML string
xml_string = '''
<note>
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
</note>
'''

# Parse XML to OrderedDict
xml_dict = xmltodict.parse(xml_string)

# Convert OrderedDict to JSON string
json_string = json.dumps(xml_dict)
print(json_string)
