# Tehtävä 1: Päiväpalkan laskeminen (if - else)
# Ohjelma kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän.
# Päiväpalkka = tuntipalkka * tunnit, paitsi sunnuntaina tuntipalkka on kaksinkertainen.

# Kysytään käyttäjältä tiedot. float() muuttaa syötteen desimaaliluvuksi.
tuntipalkka = float(input("Anna tuntipalkka (€): "))
tunnit = float(input("Anna tehdyt tunnit: "))
# lower() muuttaa tekstin pieniksi kirjaimiksi, jotta "Sunnuntai" ja "sunnuntai" toimivat samalla tavalla
paiva = input("Anna viikonpäivä: ").lower()

# Tarkistetaan, onko päivä sunnuntai
if paiva == "sunnuntai":
    # Sunnuntaina tuntipalkka on kaksinkertainen
    paivapalkka = tuntipalkka * 2 * tunnit
else:
    # Muina päivinä normaali palkka
    paivapalkka = tuntipalkka * tunnit

# Tulostetaan päiväpalkka kahden desimaalin tarkkuudella
print(f"Päiväpalkka: {paivapalkka:.2f} €")