from functions import *

# pyydetään numero
serial = input("Anna ISSN-sarjanumero:\n")

# tarkastetaan numero, tulostetaan vastaus
if magazine_serial_check(serial):
    print("Oikea ISSN.")

else:
    print("Väärä ISSN.")