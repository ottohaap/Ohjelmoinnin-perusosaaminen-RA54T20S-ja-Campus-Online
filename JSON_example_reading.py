import json
file_handle = open("app_data.json", "r")
content = file_handle.read()
file_handle.close()

# muutetaan JSON-tieto dict
city = json.loads(content)

print(city)

print(city["name"])
print(city["population"])
print(city["county"])
