import random

# avataan tiedosto
file_handle = open("wisewords.txt", "r", encoding='utf-8')

# haetaan tiedoston sisältö
content = file_handle.read()
#print(content)
# tehdään lista, erotetaan \n
lines = content.split("\n")

# satunnaismuuttuja
random_number = random.randint(0, (len(lines) - 1))

print(f"Päivän mietelause:\n{lines[random_number]}")

