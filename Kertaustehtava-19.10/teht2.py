# Tehtävä 2: Jaollisuus kolmella ja viidellä (if - elif - else)
# Ohjelma kysyy kokonaisluvun ja kertoo, onko se jaollinen kolmella, viidellä vai molemmilla.

# int() muuttaa syötteen kokonaisluvuksi
luku = int(input("Anna kokonaisluku: "))

# Jakojäännösoperaattori % kertoo jakolaskun jakojäännöksen.
# Jos jakojäännös on 0, luku on jaollinen.
# HUOM: "molemmilla" pitää tarkistaa ENSIN, muuten ohjelma pysähtyisi
# jo ensimmäiseen ehtoon (esim. 15 on jaollinen kolmella).
if luku % 3 == 0 and luku % 5 == 0:
    print("jaollinen molemmilla luvuilla!")
elif luku % 3 == 0:
    print("kolmella jaollinen")
elif luku % 5 == 0:
    print("viidellä jaollinen")
else:
    # Tehtävä ei vaadi tätä, mutta on hyvä kertoa myös, jos luku ei ole jaollinen kummallakaan
    print("ei jaollinen kolmella eikä viidellä")