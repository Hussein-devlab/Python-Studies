# Tässä ohjelma kysyy käyttäjältä kolme kokonaislukua...
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# Lasketaan summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# Kerrotaan tulokset ohjelmalle
print("Ok! Lukujen summa on..", summa)
print("Lukujen tulo on..", tulo)
print("Ja lukujen keskiarvo on..", keskiarvo)