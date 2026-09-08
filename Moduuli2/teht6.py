import random

# Ohjelma joka arpoo ja tulosstaa kaksi erilaista numeroluokan koodia

#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9
numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)
 
# Tulostetaan kolmenumeroinen koodi
print("Kolmenumeroinen koodi on:", numero1, numero2, numero3)
 
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6
numero1 = random.randint(1, 6)
numero2 = random.randint(1, 6)
numero3 = random.randint(1, 6)
numero4 = random.randint(1, 6)
 
# Tulostetaan nelinumeroinen koodi
print("Nelinumeroinen koodi on...:", numero1, numero2, numero3, numero4)