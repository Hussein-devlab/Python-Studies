# Tehtävä 6: Arvojen lisääminen listaan (listarakenne)
# Ohjelma pyytää lukuja ja lisää ne listaan. Jokaisen lisäyksen jälkeen lista
# tulostetaan kahdella tavalla: lisäysjärjestyksessä ja pienimmästä suurimpaan.
# Ohjelma lopettaa, kun käyttäjä syöttää 0.

luvut = []  # Tyhjä lista, johon luvut lisätään

while True:
    luku = int(input("Anna luku (0 lopettaa): "))

    # Nolla lopettaa ohjelman, eikä sitä lisätä listaan
    if luku == 0:
        break

    # append() lisää luvun listan loppuun
    luvut.append(luku)

    # Tulostetaan lista lisäysjärjestyksessä
    print("Lisäysjärjestyksessä:", luvut)
    # sorted() palauttaa UUDEN järjestetyn listan, alkuperäinen lista ei muutu
    print("Pienimmästä suurimpaan:", sorted(luvut))

print("Ohjelma päättyi.")