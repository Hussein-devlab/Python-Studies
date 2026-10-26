# Tehtävä 7: Pitkien sanojen laskeminen (listarakenne)
# Ohjelma laskee, kuinka monessa listan sanassa on enemmän kuin 5 kirjainta.
# Sanan pituus tarkistetaan len()-funktiolla.

# Luodaan lista itse
sanat = ["omena", "banaani", "kissa", "tietokone", "auto", "ohjelmointi", "talo", "kirjasto"]

laskuri = 0  # Lasketaan pitkien sanojen määrä

# Käydään jokainen sana läpi
for sana in sanat:
    # len() palauttaa sanan kirjainten määrän
    if len(sana) > 5:
        laskuri += 1

print("Lista:", sanat)
print(f"Sanoja, joissa on enemmän kuin 5 kirjainta: {laskuri}")