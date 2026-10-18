luku = input("Luku: ")
pienin = float(luku)
suurin = float(luku)
while luku != "":
    x = float(luku)
    if x < pienin:
        pienin = x
    if x > suurin:
        suurin = x
    luku = input("Luku: ")
print("Pienin:", pienin)
print("Suurin:", suurin)