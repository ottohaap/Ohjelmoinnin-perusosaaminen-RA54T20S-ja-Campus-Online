from functions import replace_commas

# avataan tiedosto
file_handle = open("artists.txt", "r", encoding='utf-8')

# haetaan tiedoston sisältö
content = file_handle.read()

# tehdään lista, erotetaan \n
lines = content.split("\n")

for line in lines:
    replace_commas(line)

file_handle.close()