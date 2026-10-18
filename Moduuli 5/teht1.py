import random

n = int(input("Montako arpakuutiota? "))
summa = 0
for _ in range(n):
    summa += random.randint(1, 6)
print("Silmälukujen summa:", summa)