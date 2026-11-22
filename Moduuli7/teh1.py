# Tehtävä 1: vuodenajat monikossa, indeksi = kuukausi - 1
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä",
              "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero: "))
print(vuodenajat[kuukausi - 1])