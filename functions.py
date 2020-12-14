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
def show_numbered_list(title, data):

    print("")

    # muutetaan käyttäjän antama teksti listaksi
    people = data.split(",")
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

        print("Aakkosjärjestyksesä etunimen perusteella:")

        # nimet aakkosjärjestykseen
        people = sorted(people)

        for p in people:
            print(f"{people.index(p) + 1}. {p}")

    else:

        print("Aakkosjärjestyksesä sukunimen perusteella:")

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
    print(f"Laatikon tilavuus: {volume} m3.\n")


# pallon tilavuus
def ball_volume(radius):
    volume = (4 * math.pi * math.pow(radius, 3)) / 3
    volume = round(volume, 2)
    print(f"Pallon tilavuus: {volume} m3.\n")


# lieriön tilavuus
def cylinder_volume(radius, length):
    volume = math.pi * math.pow(radius, 2) * length
    volume = round(volume, 2)
    print(f"Lieriön tilavuus: {volume} m3.\n")


# korvataan pilkut sisennyksillä tekstinkäsittelyssä
def replace_commas(string):
    print(string.replace(",", "\t"))

