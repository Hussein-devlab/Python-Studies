# Kysytään käyttäjältä hyttiluokka 
luokka = input("Anna hyttiluokka (LUX, A, B, C): ")

#Muutetaan syöte isoiksi kirjaimiksi, jotta myös "lux" toimii
luokka = luokka.upper()

# Verrataan syötettä vuorotellen jokaiseen hyttiluokkaan
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    # Jos mikään yllä olevista ei täsmää, syötteessä oli virhe
    print("Virheellinen hyttiluokka")