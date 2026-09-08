# Tässä ohjelma joka kysyy suorakulmion kannan ja korkeuden ja tulostaa sen suorakulmion piirin ja pintalan 
kanta = float(input("Kuinka pitkä on suorakulmion kanta? "))
korkeus = float(input("entä kuinka korkea se on? "))

# Lasketaan piiri ja pinta-ala
piiri = 2 * kanta + 2 * korkeus
pinta_ala = kanta * korkeus

# Tässä ohjelma tulostaa arvot meille
print("Okei! suorakulmiosi piiri on", piiri)
print("Ja sen pinta-ala on", pinta_ala)