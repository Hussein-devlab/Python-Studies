# Tehtävä 9: Tehtaan tuotannon simulointi (for + while + listat)
# Ohjelma kysyy, mitä tuotetta valmistetaan ja kuinka monta. Tuotteiden nimet ja
# määrät tallennetaan omiin listoihinsa. Ohjelma jatkaa kysymistä, kunnes
# käyttäjä vastaa "Ei". Lopuksi tulostetaan kaikki valmistetut tuotteet ja määrät.

tuotteet = []  # Tuotteiden nimet
maarat = []    # Tuotteiden määrät (samassa järjestyksessä kuin nimet)

jatketaan = "kyllä"

# Kysytään tuotteita niin kauan kuin käyttäjä vastaa "Kyllä"
while jatketaan.lower() == "kyllä":
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    # Tallennetaan nimi ja määrä omiin listoihinsa
    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaan = input("Jatketaanko tuotantoa? ")
    print()  # Tyhjä rivi selkeyden vuoksi

print("Tuotanto lopetettu!")
print()
print("Valmistetut tuotteet:")

# Käydään listat läpi for-silmukalla. range(len(tuotteet)) antaa indeksit 0, 1, 2, ...
# Samalla indeksillä saadaan sekä tuotteen nimi että sen määrä.
for i in range(len(tuotteet)):
    print(f"{tuotteet[i]}: {maarat[i]} kpl")