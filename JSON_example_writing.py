import json

# dictionary, puhelimen tidot
phone = {
    "name": "Nokia 3310",
    "release_year": 2000,
    "battery": "1000mAh",
    "camera": False,
    "weight": 133
}

# muutetaan JSOn dictionaryksi json-dumps()
content = json.dumps(phone)

# avataan tiedosto & JSON sinne; w, ei a
file_handle = open("phone.json", "w")
file_handle.write(content)
file_handle.close()
print("Phone was saved.")