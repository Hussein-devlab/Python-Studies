# Tehtävä 4: Neliöjuuret (while)
# Ohjelma kysyy kokonaislukuja:
#  - negatiivinen luku -> "Virheellinen numero"
#  - positiivinen luku -> tulostetaan luvun neliöjuuri
#  - nolla -> ohjelma lopettaa

# Tuodaan sqrt-funktio math-kirjastosta
from math import sqrt

# Kysytään ensimmäinen luku ennen silmukkaa
luku = int(input("Anna kokonaisluku (0 lopettaa): "))

# Silmukka jatkuu niin kauan kuin luku ei ole nolla
while luku != 0:
    if luku < 0:
        print("Virheellinen numero")
    else:
        # Lasketaan ja tulostetaan neliöjuuri
        print(f"Luvun {luku} neliöjuuri on {sqrt(luku)}")

    # Kysytään uusi luku molemmissa tapauksissa
    luku = int(input("Anna kokonaisluku (0 lopettaa): "))

print("Ohjelma päättyi.")