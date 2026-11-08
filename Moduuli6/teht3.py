# Funktio muuttaa gallonat litroiksi
def litroiksi(gallonat):
    return gallonat * 3.785  # Yksi gallona on 3,785 litraa

gallonat = float(input("Anna gallonat: "))  # Kysytään ensimmäinen luku
while gallonat >= 0:  # Jatketaan, kunnes luku on negatiivinen
    print(litroiksi(gallonat), "litraa")  # Tulostetaan litrat
    gallonat = float(input("Anna gallonat:"))  # Kysytään uusi luku