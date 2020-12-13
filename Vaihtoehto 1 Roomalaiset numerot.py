import math

# dict, jossa arabialaisia numeroita vastaavat
# roomalaiset numerot
roman_numerals = {
    1: "I",
    4: "IV",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

# tyhjä tekstimuuttuja summan tulostamista varten
text = ""

# muuttuja summan laskemista varten
sum_number = 0

# laskuri lukujen tarkistamista varten
counter = 1

# boolean-muuttuja ohjelman pysäyttämiseksi,
# jos annettaan luku väärässä muodossa
good_number = True

number = input("Anna numero:\n"
               "(arabialaiseten numeroiden oltava välillä 1-3999, "
               "roomalaiset numerot annettava isoina kirjaimina)\n")

# tarkastetaan onko input numeromuodossa eli
# INPUT ARABIALAINEN NUMERO
if number.isnumeric():
    number = int(number)

    # tarkastetaan, että luku on oikean suuruinen
    # tarvittaessa tulostetaan virheviesti ja lopetetaan ohjelma
    if not 0 < number < 4000:
        print("Luku liian suuri tai pieni!")
        good_number = False

    if good_number:

        # LASKETAAN TUHANSIEN, SATASTEN, KYMPPIEN JA YKKÖSTEN LUKUMÄÄRÄ
        # -------------------------------------------------------------
        # selvitetään tuhansien lukumäärä luvussa
        # jaetaan luku tuhannella ja poistetaan desimaalit
        # (esim. 1234 / 1000 = 1,234 -> 1)
        number_thous = math.trunc(number / 1000)

        # selvitetään sataset
        # miinustetaan alkuperäisestä numerosta tuhannet
        # (esim. 1234 - 1000 = 234)
        # jaetaan sataset sadalla ja poistetaan desimaalit
        # jäljelle jää satasten lukumäärä
        # (234 / 100 = 2,34 -> 2)
        number_hunds = math.trunc((number - (number_thous * 1000)) / 100)

        # selvitetään kympit
        number_tens = math.trunc((number - (number_thous * 1000) - (number_hunds * 100)) / 10)

        # selvitetään ykköset
        number_ones = math.trunc((number - (number_thous * 1000) - (number_hunds * 100) - (number_tens * 10)))

        # MUUTETAAN ANNETUT TUHANNET, SATASET YMS. ROOMALAISIKSI NUMEROIKSI
        # -----------------------------------------------------------------
        # TUHANSIEN MUUTTAMINEN
        # lisätään tekstimuuttujaan tuhansien määrä
        # roomalaisina numeroina
        text = text + number_thous * roman_numerals[1000]

        # SATASTEN MUUTTAMINEN
        # jos satasia 0-3
        if number_hunds <= 3:
            # lisätään tekstiin satasien määrä
            # roomalaisina numeroina
            text = text + number_hunds * roman_numerals[100]

        # jos satasia 4
        elif number_hunds == 4:
            roman_hunds = roman_numerals[100] + roman_numerals[500]
            text = text + roman_hunds

        # jos satasia 5
        elif number_hunds == 5:
            roman_hunds = roman_numerals[500]
            text = text + roman_hunds

        # jos satasia 6-8
        elif 6 <= number_hunds <= 8:
            roman_hunds = roman_numerals[500] + (number_hunds - 5) * roman_numerals[100]
            text = text + roman_hunds

        # jos annettu satanen on 900
        else:
            text = text + roman_numerals[100] + roman_numerals[1000]

        # KYMPPIEN MUUTTAMINEN
        # jos kymppejä 0-3
        if number_tens <= 3:
            text = text + number_tens * roman_numerals[10]

        # jos kymppejä 4
        elif number_tens == 4:
            roman_tens = roman_numerals[10] + roman_numerals[50]
            text = text + roman_tens

        # jos kymppejä 5
        elif number_tens == 5:
            roman_tens = roman_numerals[50]
            text = text + roman_tens

        # jos kymppejä 6-8
        elif 6 <= number_tens <= 8:
            roman_tens = roman_numerals[50] + (number_tens - 5) * roman_numerals[10]
            text = text + roman_tens

        # jos annettu kymppi on 90
        else:
            text = text + roman_numerals[10] + roman_numerals[100]

        # YKKÖSTEN MUUTTAMINEN
        # jos ykkösiä 0-3
        if number_ones <= 3:
            text = text + number_ones * roman_numerals[1]

        # jos ykkösiä 4
        elif number_ones == 4:
            roman_ones = roman_numerals[1] + roman_numerals[5]
            text = text + roman_ones

        # jos ykkösiä 5
        elif number_ones == 5:
            roman_ones = roman_numerals[5]
            text = text + roman_ones

        # jos ykkösiä 6-8
        elif 6 <= number_ones <= 8:
            roman_ones = roman_numerals[5] + (number_ones - 5) * roman_numerals[1]
            text = text + roman_ones

        # jos annettu ykkönen on 9
        else:
            text = text + roman_numerals[1] + roman_numerals[10]

        # tulostetaan roomalaisina numeroina
        print(f"Roomalaisina numeroina:\n{text}")

# INPUT ROOMALAINEN NUMERO
else:
    # tehdään inputista lista ja käännetään
    # se toisinpäin yhteenlaskun helpottamiseksi
    number = list(number)
    number.reverse()

    # tyhjä lista roomalaisten numeroiden
    # järjestyksen tarkistamista varten
    chk_list = []

    # Roomalaisia numeroita voidaan muuttaa arabialaisiksi
    # summaamalla numeroita aloittaen viimeisestä:
    # 123 = CXXIII = I+I+I+X+X+C = 1+1+1+10+10+100 = 123.
    # Ongelmaksi muodustuvat neloset ja ysit;
    # 4 (IV) ja 9 (IX), 40 (XL) ja 90 (XC) sekä 400 (CD) ja 900 (CM);
    # jos esimerkiksi IV:n (4) tai IX:n (9) summaa (I+ V tai I + X), vastaukseksi tulee 6 ja 11.
    # RATKAISU:
    if len(number) > 1:

        # 4
        # käydään luku läpi silmukassa
        for n in number:

            # jos listassa "VI" (lista käännetty toisin päin),
            # poistetaan I ja V, lisätään summamuuttujaan 4
            if n == "I" and number[number.index(n) - 1] == "V":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 4

        # 9
        for n in number:

            if n == "I" and (number.index(n) - 1) >= 0 and number[number.index(n) - 1] == "X":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 9

        # 40
        for n in number:

            if n == "X" and (number.index(n) - 1) >= 0 and number[number.index(n) - 1] == "L":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 40

        # 90
        for n in number:

            if n == "X" and (number.index(n) - 1) >= 0 and number[number.index(n) - 1] == "C":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 90

        # 400
        for n in number:

            if n == "C" and (number.index(n) - 1) >= 0 and number[number.index(n) - 1] == "D":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 400

        # 900
        for n in number:

            if n == "C" and (number.index(n) - 1) >= 0 and number[number.index(n) - 1] == "M":
                del number[number.index(n) - 1]
                del number[number.index(n)]
                sum_number = sum_number + 900

    # muutetaan roomalaiset numerot arabialaisiksi
    # käydään annetut numerot läpi ja summataan ne
    for n in number:

        # tarkastetaan, ovatko kaikki annetut roomalaiset
        # numerot listassa, eli onko kirjoitettu oikein
        if n in roman_numerals.values():
            # etsitään listasta annettua roomalaista numeroa
            # vastaava arabialainen numero ja lisätään se
            # summaan sekä tarkistuslistaan
            for x, y in roman_numerals.items():
                if y == n:
                    sum_number = sum_number + x
                    chk_list.append(x)
        else:
            good_number = False
            # lopetetaan silmukka ensimmäisen virheen kohdalla
            break

    # tarkistetaan ovatko luvut järjestyksessä
    # pienimmästä suurimpaan, mikäli numeroita on
    # enemmän kuin yksi ja numero on oikeassa muodossa
    if len(chk_list) > 1 and good_number:

        # käydään läpi tarkistuslista
        # numero kerrallaan
        for c in chk_list:

            # tarkistetaan onko silmukan numero
            # listan seuraavaa numeroa pienempi
            # virheviesti, jos numero suurempi
            if c > chk_list[counter]:
                good_number = False
                # lopetetaan silmukka ensimmäisen virheen kohdalla
                break

            # lisätään laskuriin yksi, mikäli ei olla silmukan lopussa
            if (counter + 1) < len(chk_list):
                counter = counter + 1

    # jos numero on sopiva, tulostetaan se
    if good_number:
        print(f"Arabialaisina numeroina:\n{sum_number}")
    else:
        print("Vääränlainen luku!")
