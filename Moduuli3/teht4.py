# Kysytään käyttäjältä vuosiluku ja muutetaan se kokonaisluvuksi
vuosi = int(input("Anna vuosiluku: "))

# Merkki % antaa jakojäännöksen.
# Jos jakojäännös on 0, luku on tasan jaollinen.

# Jaollinen 400 - aina karkausvuosi
if vuosi % 400 == 0:
    print(vuosi, "on karkausvuosi.")

# Jaollinen 100 - mutta ei 400 - ei karkausvuosi 
elif vuosi % 100 == 0:
    print(vuosi, "ei ole karkausvuosi.")

# Jaollinen 4 - karkausvuosi 
elif vuosi % 4 == 0:
    print(vuosi, "on karkausvuosi.")

# Kaikki muut vuodet
else:
    print(vuosi, "ei ole karkausvuosi.")