kerrat = 1
tunnus = input("Tunnus: ")
salasana = input("Salasana: ")
while (tunnus != "kissa" or salasana != "1234") and kerrat < 5:
    tunnus = input("Tunnus: ")
    salasana = input("Salasana: ")
    kerrat = kerrat + 1
if tunnus == "kissa" and salasana == "1234":
    print("Tervetuloa")
else:
    print("Pääsy evätty")