from functions import show_numbered_list

# pyydetään numerot yhtenä tekstinä käyttäjältä
people = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:\n")

# pyydetään nimet ja tulostetaan seuraavassa järjestyksessä:
# 1. ilm.jär:ssä
# 2. aakkosjär:ssä etunimen mukaan
# 3. aakkosjär:ssä sukunimen mukaan
for x in range(3):

    if x == 0:
        title = "number"

    elif x == 1:
        title = "first_name"

    else:
        title = "surname"

    show_numbered_list(title, people)
