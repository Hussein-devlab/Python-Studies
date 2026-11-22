# Tehtävä 3: lentoasemat sanakirjassa, avain = ICAO-koodi, arvo = nimi
lentoasemat = {}

while True:
    valinta = input("1 = uusi, 2 = hae, 3 = lopeta: ")
    if valinta == "1":
        koodi = input("ICAO-koodi: ")
        nimi = input("Nimi: ")
        lentoasemat[koodi] = nimi
    elif valinta == "2":
        koodi = input("ICAO-koodi: ")
        print(lentoasemat.get(koodi, "Ei löydy"))
    elif valinta == "3":
        break