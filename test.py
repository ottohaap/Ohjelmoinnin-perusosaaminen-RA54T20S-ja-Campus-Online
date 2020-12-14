# avataan tiedosto
file_handle = open("weekdays.txt", "r")

# haetaan tiedoston sisältö
content = file_handle.read()

#print(content)

lines = content.split("\n")
print(lines)

for line in lines:
    print(line)