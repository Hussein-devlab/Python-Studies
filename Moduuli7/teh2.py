# Tehtävä 2: nimet joukkoon, joukko pitää huolen ettei tule tuplia
nimet = set()

nimi = input("Anna nimi: ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    nimi = input("Anna nimi: ")

for n in nimet:
    print(n)