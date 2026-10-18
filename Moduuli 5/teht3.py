n = int(input("Anna kokonaisluku: "))
alkuluku = n > 1
for i in range(2, n):
    if n % i == 0:
        alkuluku = False
        break

print(f"{n} on alkuluku." if alkuluku else f"{n} ei ole alkuluku.")