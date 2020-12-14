import  math

# tulostaa henkilätiedot
def show_personal_info(name, city, profession):
    print(name)
    print(city)
    print(profession)


# laskee annetut tunnit, minuutit ja sekunnit yhteen
def count_seconds(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60
    sum_seconds = hours + minutes + seconds
    return sum_seconds


# tarkistaa onko ISSN-numero oikeassa muodossa
def magazine_serial_check(serial):
    good = True

    # onko pituus oikea ja keskellä vivia
    if len(serial) != 9 and serial[4] != "-":
        good = False

    # onko numeromuodossa pl. viiva
    serial = serial.replace("-", "")
    if serial.isnumeric() == False:
        good = False

    # onko oikeassa muodossa?
    # palauttaa Boolean
    if good:
        return True

    else:
        return False


# listataan nimet annetun otsikon mukaan
def show_numbered_list(title, people):

    print("")

    # muutetaan käyttäjän antama teksti listaksi
    people = people.split(",")
    #print(people)

    # otetaan nimistä ylimääräiset välilyönnit pois (nimen alusta ja lopusta)
    people = [p.strip() for p in people]
    #print(people)
    # people-muuttuja on tässä vaiheessa lista, joka koostuu henkilöiden kokonimistä

    # jos nimet pyydetään ilm.järjestyksessä
    if title == "number":

        print("Ilmoittautumisjärjestyksessä:")

        # tulostetaan numero ja nimi
        for p in people:
            print(f"{people.index(p) + 1}. {p}")

    elif title == "first_name":

        print("Aakkosjärjestys etunimen perusteella:")

        # nimet aakkosjärjestykseen
        people = sorted(people)

        for p in people:
            print(f"{people.index(p) + 1}. {p}")

    else:

        print("Aakkosjärjestys sukunimen perusteella:")

        # muutetaan listan henkilöt niin, että sukunimi tulee ennen etunimeä.
        # tämä on ns. list comprehension -ominaisuus Pythonissa.
        # Logiikka: jokainen nimi vuorollaan muutetaan listaksi
        # välilyönnin perusteella, eli tämän vuoksi jokainen nimi on lista,
        # jossa on kaksi elementtiä, etunimi ja sukunimi.
        # sitten elementtien järjestys muutetaan toisin päin käyttämällä
        # reversed-funktiota- lopuksi uusi järjestys muutetaan takaisin
        # kokonaiseksi nimeksi .join() -funktion avulla. Lopputuloksena
        # people lista koostuu nimistä, joissa sukunimi tulee ensin.
        people = [" ".join(reversed(p.split(" "))) for p in people]

        # nimet aakkosjärjestykseen
        people = sorted(people)

        for p in people:
            print(f"{people.index(p) + 1}. {p}")

# laatikon tilavuus
def box_volume(width, height, depth):
    volume = width * height * depth
    volume = round(volume, 2)
    return volume



# pallon tilavuus
def ball_volume(radius):
    volume = (4 * math.pi * math.pow(radius, 3)) / 3
    volume = round(volume, 2)
    return volume


# lieriön tilavuus
def pipe_volume(radius, length):
    volume = math.pi * math.pow(radius, 2) * length
    volume = round(volume, 2)
    return volume


# korvataan pilkut sisennyksillä tekstinkäsittelyssä
# Erillisen funktion käyttäminen on lisätehtävä.
# Jos haluat tehdä tämän lisätehtävän,
# muista että funktiossa pitää olla
# open, read/readline/readlines sekä close-kutsut.
# Muista myös kutsua omaa funktiotasi.
def get_artists():

    # avataan tiedosto
    file_handle = open("artists.txt", "r", encoding='utf-8')
    # haetaan tiedoston sisältö
    content = file_handle.read()
    file_handle.close()
    # tehdään lista, erotetaan \n
    lines = content.split("\n")

    for line in lines:
        artist_text = line.replace(",", "\t")
        print(artist_text)

