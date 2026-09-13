
# Kysytään käyttäjältä kuhan pituus ja muutetaan se
pituus = float(input("Anna kuhan pituus senttimetreinä: "))

# Tarkistetaan, onko pituus alle 37 cm 
if pituus < 37: 
   #lasketaan montako senttiä alamitasta puuttuu
   puuttuu = 37- pituus
   print("Kuha on alamittainen. Laske se takaisin järveen.")
   #tulostetaan puuttuva määrä
   print("pituudesta puuttuu", puuttuu,"cm")
else:
   # Kun kuha on 37 tai yli se on riittävän iso 
   print("Kuha on täysmittainen. Saat pitää sen")
