from datetime import datetime
import json

try:

    # avataan tiedosto
    file_handle = open("guestbook.json", "r")
    # haetaan tiedoston sisältö
    content = file_handle.read()
    # suljetaan tiedosto
    file_handle.close()
    messages = json.loads(content)

    read_or_write = str(input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k)\n"))

    if read_or_write == "l":

        # käydään läpi listan sisältämät viesti-dictionaryt
        for message in messages:

            # tulostetaan viesti-dictionaryn tiedot
            message_text = message['message']
            date = message['date']
            time = message['time']
            print(f""""{message_text}", kirjoitettu {date}, klo {time}""")

    elif read_or_write == "k":

        # pvm ja aika
        now = datetime.now()
        # pvm
        date = now.strftime("%d.%m.%Y")
        # aika
        time = now.strftime("%H:%M:%S")

        write_input = input("Kirjoita uusi viesti:\n")

        # luodaan uusi viesti-dictionary
        new_message = {
            "message": write_input,
            "date": date,
            "time": time
        }

        # lisätään viesti-dict viestien listaan
        messages.append(new_message)
        # tallennetaan uusi lista tiedostoon
        # muunnetaan JSONiksi
        json_data = json.dumps(messages)
        file_handle = open("guestbook.json", "w")
        file_handle.write(json_data)
        file_handle.close()
        print("Viesti tallennettu vieraskirjaan.")

    else:
        print("Väärä muoto!")

except ValueError:
    print("Väärä muoto!")

