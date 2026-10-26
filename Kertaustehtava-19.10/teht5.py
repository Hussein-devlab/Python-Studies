# Tehtävä 5: Tarinan kirjoittaminen (while)
# Ohjelma pyytää sanoja ja lisää ne tarinaan. Kun käyttäjä kirjoittaa "loppu",
# ohjelma tulostaa tarinan ja lopettaa.
# Bonus: silmukka loppuu myös, jos käyttäjä syöttää saman sanan kahdesti peräkkäin.

tarina = ""          # Tähän kerätään tarinan sanat
edellinen_sana = ""  # Muistetaan edellinen sana bonusta varten

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    # Jos sana on "loppu", lopetetaan silmukka
    if sana == "loppu":
        break

    # Bonus: jos sana on sama kuin edellinen, lopetetaan silmukka
    if sana == edellinen_sana:
        break

    # Lisätään sana tarinaan. Sanojen väliin tulee välilyönti
    # (paitsi ensimmäisen sanan eteen).
    if tarina == "":
        tarina = sana
    else:
        tarina = tarina + " " + sana

    # Tallennetaan sana seuraavaa kierrosta varten
    edellinen_sana = sana

# Tulostetaan valmis tarina
print(tarina)