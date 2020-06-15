sana = input("Sana: ")
merkki = input("Merkki: ")

pituus = len(sana)

i = 0

for i in range(0, pituus -1):
    if sana[i] == merkki:
        print(sana[i:i + 3])
