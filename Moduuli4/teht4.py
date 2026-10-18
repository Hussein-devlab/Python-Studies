import random
oikea = random.randint(1, 10)
arvaus = 0
while arvaus != oikea:
    teksti = input("Arvaa: ")
    if teksti.isdigit():
        arvaus = int(teksti)
        if arvaus > oikea:
            print("Liian suuri arvaus")
        elif arvaus < oikea:
            print("Liian pieni arvaus")
    else:
        print("Anna luku")
print("Oikein")