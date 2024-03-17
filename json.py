import json

data = '{"name": "TUNDSKY", "age": 19, "city": "City"}'
parsed_data = json.loads(data)
print(parsed_data)
