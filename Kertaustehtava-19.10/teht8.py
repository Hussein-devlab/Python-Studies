# Tehtävä 8: Valmistuskustannukset (for)
# Listassa on viiden tuotteen valmistuskustannukset. Ohjelma käy ne läpi
# for-silmukalla, tulostaa jokaisen ja laskee kokonaiskustannuksen.

kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

yhteensa = 0  # Tähän lasketaan kustannusten summa

# Käydään jokainen kustannus läpi
for kustannus in kustannukset:
    print(f"Tuotteen valmistuskustannus: {kustannus} €")
    # Lisätään kustannus summaan
    yhteensa += kustannus

# Tyhjä rivi ennen yhteenvetoa, kuten esimerkissä.
# round() pyöristää, jotta liukulukujen pienet virheet eivät näy (esim. 53.00000001)
print()
print(f"Valmistuskustannukset yhteensä: {round(yhteensa, 2)} €")