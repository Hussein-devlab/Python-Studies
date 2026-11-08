import random  # Tuodaan satunnaisluvut

# Funktio saa parametrina nopan tahkojen määrän
def heita(tahkot):
    return random.randint(1, tahkot)  # Palauttaa luvun 1-tahkot

maksimi = int(input("Anna maksimisilmäluku: "))  # Kysytään käyttäjältä
luku = 0  # Aloitusarvo
while luku != maksimi:  # Toistetaan, kunnes tulee maksimi
    luku = heita(maksimi)  # Heitetään noppaa
    print(luku)  # Tulostetaan tulos