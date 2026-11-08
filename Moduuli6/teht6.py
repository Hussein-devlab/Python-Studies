# Funktio laskee yksikköhinnan (€ per neliömetri)
def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2 / 100  # Säde metreinä
    ala = 3.14 * sade * sade  # Pinta-ala
    return hinta / ala  # Hinta per neliömetri

# Kysytään pizzojen tiedot
h1 = float(input("Pizza 1 halkaisija (cm): "))
p1 = float(input("Pizza 1 hinta (€): "))
h2 = float(input("Pizza 2 halkaisija (cm): "))
p2 = float(input("Pizza 2 hinta (€): "))

yh1 = yksikkohinta(h1, p1)  # Pizzan 1 yksikköhinta
yh2 = yksikkohinta(h2, p2)  # Pizzan 2 yksikköhinta

# Pienempi yksikköhinta on parempi
if yh1 < yh2:
    print("Pizza 1 on parempi")
else:
    print("Pizza 2 on parempi")