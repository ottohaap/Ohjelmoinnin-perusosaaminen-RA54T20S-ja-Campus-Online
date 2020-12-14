import json

# aukaistaan tieodsta ja muutetaan JSON-listaksi
file_handle = open("cities.json", "r")
content = file_handle.read()
file_handle.close()

cities = json.loads(content)

# käydään läpi kaupunki-dicts
for city in cities:
    print(city)
    # käydään läpi indexit (nimi, väkiluku tai maakunta
    print(f"{city['name']}, {city['county']}. Väkiluku: {city['population']}")
    # tulostetaan tyhjä teksti
    print("")

# pyydetään käyttäjältä uuden kaupungin tiedot muuttujiin
city_name = input("Anna lisättävän kaupungin nimi:\n")
city_county = input("Anna lisättävän kaupungin maakunta:\n")
city_population = input("Anna lisättävän kaupungin väkiluku:\n")

# rakennetaan muuttujista dictionary
new_city = {
"name": city_name,
"county": city_county,
"population": city_population
}
# lisätään uuden kaupungin dictionary tiedosto-listan
cities.append(new_city)

# tallennetaan uusi lista tiedostoon
# muunnetaan data JSON-formaattiin
json_data = json.dumps(cities)
file_handle = open("cities.json", "w")
file_handle.write(json_data)
file_handle.close()
print("Uusi kaupunki tallennettu.")