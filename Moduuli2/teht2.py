import math

# Tässä on ohjelmna joka kysyy ympyrän säde ja tulostaa sen pinta alan
sade = float(input("Kuinka pitkä on ympyrän säde? "))

# Lasketaan pinta-ala kaavalla pii kertaa säde toiseen
pinta_ala = math.pi * sade ** 2

# Tässä ohjelma kertoo pinta alan
print("Selvä! Ympyräsi pinta-ala on", pinta_ala)