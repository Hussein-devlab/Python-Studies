# Tässä ohjelma joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina
leiviskat = int(input("Anna leiviskät.\n"))
naulat = int(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

# Muutetaan leiviskät nauloiksi ja lisätään naulat...
naulat_yhteensa = leiviskat * 20 + naulat
# Muutetaan naulat luodeiksi ja lisätään luodit.....
luodit_yhteensa = naulat_yhteensa * 32 + luodit
# Muutetaan luodit grammoiksi.....
grammat_yhteensa = luodit_yhteensa * 13.3
# Otetaan täydet kilot ja loput grammat......
kilot = int(grammat_yhteensa / 1000)
grammat = int(grammat_yhteensa - kilot * 1000)

# Kerrotaan tulos
print("Okei! Massa on", kilot, "kiloa ja", grammat, "grammaa")