try:
    read_or_write = input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k)\n")

    if read_or_write == "l":

        # avataan tiedosto
        file_handle = open("guestbook.txt", "r", encoding='utf-8')
        # haetaan tiedoston sisältö
        content = file_handle.read()
        # tehdään lista, erotetaan \n
        lines = content.split("\n")

        # luetaan rivi kerrallaan
        for line in lines:
            print(line)

        # suljetaan tiedosto
        file_handle.close()


    elif read_or_write == "k":

        # avataan tiedosto, a = append
        file_handle = open("guestbook.txt", "a", encoding='utf-8')
        # pyydetään kirjoitettava viesti
        write_input = input("Kirjoita uusi viesti:\n")
        # kirjoitetaan viesti tiedostoon, lisätään rivinvaihto
        file_handle.write(write_input)
        file_handle.write("\n")

        print("Viesti tallennettu vieraskirjaan.")
        # suljetaan tiedosto
        file_handle.close()

    else:
        print("Väärä muoto!")



except ValueError:
    print("Väärä muoto!")