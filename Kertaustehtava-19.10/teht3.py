# Tehtävä 3: Tuotantolinjan simulointi (while)
# Ohjelma tulostaa "Tuote valmistettu!" ja kysyy "Jatketaanko tuotantoa?"
# niin kauan, kunnes käyttäjä vastaa "Ei".

vastaus = ""

# Silmukka jatkuu niin kauan kuin vastaus EI ole "ei"
# (lower() hyväksyy myös "Ei", "EI" jne.)
while vastaus.lower() != "ei":
    print("Tuote valmistettu!")
    vastaus = input("Jatketaanko tuotantoa? ")

# Kun silmukka loppuu, tuotanto lopetetaan
print("Tuotanto lopetettu!")