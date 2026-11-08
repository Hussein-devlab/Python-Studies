import random  # Tuodaan satunnaisluvut

# Funktio heittää noppaa
def heita():
    return random.randint(1, 6)  # Palauttaa luvun 1-6

luku = 0  # Aloitusarvo
while luku != 6:  # Toistetaan, kunnes tulee 6
    luku = heita()  # Heitetään noppaa
    print(luku)  # Tulostetaan tulos