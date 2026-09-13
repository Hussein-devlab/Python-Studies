#Kysytään käyttäjän sukupuoli
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")

# Muutetaan syöte pieniksi kirjaimiksi jotta myös "Nainen" toimii
sukupuoli = sukupuoli.lower()

# Kysytään hemoglobiiniarvo ja muutetaan se desimaaliluvuksi
hb = float(input("Anna hemoglobiiniarvo (g/l): "))

#Naisen normaali arvo on 117-175 g/l
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

#Miehen normaali arvo on 134-195 g/l
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

#Jos syöte ei ollut nainen eikä mies
else:
    print("Virheellinen sukupuoli")