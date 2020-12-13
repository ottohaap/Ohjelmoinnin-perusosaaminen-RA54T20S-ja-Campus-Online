from functions import box_volume, ball_volume, cylinder_volume

try:
    running = True

    while running:

        shape = int(input("Annan kappaleen muoto:\n"
                      "(1 = laatikko, 2 = pallo, 3 = putki."
                      " 0 = lopetetaan ohjelman käyttäminen)\n"))

        if shape == 0:
            print("Kiitos ohjelman käytöstä!")
            running = False

        elif shape == 1:
            width = float(input("Anna laatikon leveys (m):\n"))
            height = float(input("Anna laatikon korkeus (m):\n"))
            depth = float(input("Anna laatikon syvyys (m):\n"))

            box_volume(width, height, depth)

        elif shape == 2:

            radius = float(input("Anna pallon säde (m):\n"))

            ball_volume(radius)

        elif shape == 3:

            radius = float(input("Anna lieriön pohjan säde (m):\n"))
            lenght = float(input("Anna lieriön pituus (m): \n"))

            cylinder_volume(radius, lenght)

        else:
            print("Väärä muoto!")

except ValueError:
    print("Väärä muoto!")
