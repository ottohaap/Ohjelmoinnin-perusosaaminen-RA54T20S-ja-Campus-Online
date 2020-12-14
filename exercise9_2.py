from functions import *

# pyydetään tunnit, minuutit ja sekunnit
hours = int(input("Anna tunnit:\n"))
minutes = int(input("Anna minuutit:\n"))
seconds = int(input("Anna sekunnit:\n"))

# laskee yhteen ja tulostaa
sum_seconds = count_seconds(hours, minutes, seconds)
print(sum_seconds)
