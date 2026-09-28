import random

plik = open("zad1.txt", "w")

for i in range(20):
    temperatura = random.randint(-30, -1)
    plik.write(str(temperatura) + "\n")

plik.close()



plik = open("zad1.txt", "r")

temperatury = []

for linia in plik:
    temperatury.append(int(linia))

plik.close()

temperatury.sort()

print("Trzy najniższe temperatury:")

for i in range(3):
    print(temperatury[i])
    
    
plik = open("zad3.txt", "r")
tekst = plik.read()
plik.close()

szyfr = ""

for znak in tekst:
    if znak.isalpha():
        szyfr = szyfr + chr(ord(znak) + 3)
    else:
        szyfr = szyfr + znak

plik = open("zad3_zaszyfrowany.txt", "w")
plik.write(szyfr)
plik.close()


#

plik = open("zad4.txt", "r")
# czyatmy co jest w tym pliku
tekst = plik.read() 
#zamykamy plik
plik.close()

odszyfrowany = ""

for znak in tekst:
    if znak.isalpha():
        odszyfrowany = odszyfrowany + chr(ord(znak) - 3)
    else:
        odszyfrowany = odszyfrowany + znak

print(odszyfrowany)

#mamy tutaj jakies 2 petle  kazda z nich jest od 1 do 10
plik = open("zad5.txt", "w")

for i in range(1, 11):
    for j in range(1, 11):
        wynik = i * j
        plik.write(str(wynik) + "\t")
    
    plik.write("\n")

plik.close()



