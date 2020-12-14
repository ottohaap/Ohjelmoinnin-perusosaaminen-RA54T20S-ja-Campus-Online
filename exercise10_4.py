import json
file_handle = open("countries.json", "r")
content = file_handle.read()
file_handle.close()

# muutetaan JSON-tieto dict
countries = json.loads(content)

print("Kaikki maat ja pääkaupungit:")
for country in countries:

    print(f"{country['country']}: {country['capital']}")

print("")

# suodatetaan alkukirjaimen avulla
# kysytään alkukirjainta
letter = input("Minkä alkukirjaiment maat ja pääkaupungit tulostetaan?\n")

# käydään maat läpi
for country in countries:

    # verrataan annettua kirjainta maan alkukirjaimeet
    # jos sama, tulostetaan
    if country['country'][0] == letter:
        print(f"{country['country']}: {country['capital']}")
