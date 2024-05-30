import xmltodict
import json

# Sample JSON string
json_string = '''
{
    "note": {
        "to": "Tove",
        "from": "Jani",
        "heading": "Reminder",
        "body": "Don't forget me this weekend!"
    }
}
'''

# Parse JSON to dictionary
json_dict = json.loads(json_string)

# Convert dictionary to XML string
xml_string = xmltodict.unparse(json_dict, pretty=True)
print(xml_string)
