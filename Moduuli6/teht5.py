# Funktio palauttaa uuden listan, jossa on vain parilliset luvut
def parilliset(lista):
    uusi = []  # Tyhjä lista tuloksille
    for luku in lista:  # Käydään lista läpi
        if luku % 2 == 0:  # Jos luku on parillinen
            uusi.append(luku)  # Lisätään uuteen listaan
    return uusi  # Palautetaan uusi lista

luvut = [1, 2, 3, 4, 5, 6, 7, 8]  # Alkuperäinen lista
print(luvut)  # Tulostetaan alkuperäinen
print(parilliset(luvut))  # Tulostetaan karsittu lista