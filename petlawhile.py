from random import randint 

#wylosuj 10 liczb 1-50, wypisz srednia oraz ile jest podzielnych przez 5
i = 0
ile_podzielnych = 0
s = 0
while i < 10:
    r  = randint(1,50)
    s += r
    if r % 5 == 0:
        ile_podzielnych += 1
        i += 1
        print(ile_podzielnych)
        print(s/10)

#wczytaj k. losuj liczby 1-100 az trafisz liczbe podzielna przez k zlicz pruby
k = int(input("podaj liczbe k:"))
ile = 0
r = 101
while r % k != 0:
    r = randint(1,100)
    ile += 1
print(ile)

#podaj ile cyfr ma liczba dodatnia n bez zamiany na string
n = int(input("podaj liczbe n:"))
ile_cyfr = 0
while n > 0:
    n //= 10
    ile_cyfr += 1
print(ile_cyfr)

#policz n!petla while. dla n<0 wypisz blad
n = int(input("podaj liczbe n:"))
if n < 0:
    print("blad")
else:
    silnia = 1
    while n > 1:
        silnia *= n
        n -= 1
    print(silnia)

    #wczytaj n i sprawdz czy jest podzielna 2, dzielac n przez 2 dopuki n%2==0
    n = int(input("podaj liczbe n :"))
    if n<= 0:
        print("blad")
    else:
        while n % 2 == 0:
            n //= 2
            if n == 1:
                print("tak")
            else:
                print("nie")

    #wypisz liczby od 1-10
    i = 1
    while i <= 10:
        print(i)

    #wypisz liczby od 10-1
    i = 10
    while i >= 1:
        print(i)
        i -= 1

    #wypisz wszystkie liczby parzyste   od 1-100          
    i = 1
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1

    #wypisz wszystkie liczby nieparzyste od 1-100
    i = 1 
    while i <= 100:
        if i % 2 != 0:
            print(i)
            i += 1

    # wypisz liczby podzielne przez 7 od 1-100
    n = 1
    while n<=100:
        if n % 7 == 0:
            print(n)
            n += 1

    #napisz program ktory pyta uzytkownika o liczbe n a nastepnie oblicza silnie tej liczby 
    n = int(input("podaj liczbe n :"))
    if n < 0:
        print("blad")
    else:
        silnia = 1
        while n > 1:
            silnia *= n
            n -= 1
            print(silnia)

 # znajdz maksymalny element w lisci liczb


x = [3,4,6,5,8,2,1]
if len(x) == 0:
    print("lista pusta")
else:
    max_liczba = x[0]
    for i  in range(len(x)):
        if x[i] > max_liczba:
            max_liczba = x[i]
    print(max_liczba)
    print(max(x))
    
    # wyswietl z pomoca for wszystkie indeksy i wartosci elementow listy
    x = [5,6,5,6,6,7,8,9]
    for i, v in enumerate(x):
       print("Indeks:", i, "Wartosc:", v)
 # usuwaj elementy z listy az lista bedzie pusta
    x = [8,9,0,3,4,4,5,5]
    while len(x) > 0:
        print("Usuwam:", x[0])
        x.pop(0)
    print("Lista pusta")

    x = [5,6,6,7,8,2,3]
unikatowe = []
for el in x:
    if el not in unikatowe:
        unikatowe.append(el)
x = unikatowe
print(x)
print(list(set(x)))
# wygeneruj liste n-elementowa liste liczb calkowitych z przedzialu od a do b
from random import randint
n = int(input("podaj liczbe n:"))
a = int(input("podaj liczbe a:"))
b = int(input("podaj liczbe b:"))
los = []
for _ in range(n):
    los.append(randint(a,b))
print(los)


#podaj ile razy podana liczba wystepuje w liscie
x = [5,5,6,6,7,7,7,8,3]
ile = 0
liczba= int(input("podaj liczbe:"))
while ile < len(x):
    if x[ile] == liczba:
        ile += 1
    else:
        ile += 1
print(ile)

# oblicz srednia arytmetyczna liczb w liscie
x = [5,6,7,8,9,10]
if not x:
    print("lista pusta")
else:
    s = 0
    i = 0
    while i < len(x):
        s += x[i]
        i += 1
print(s / len(x))

n = int(input())
for i in range (n + 1):
    print(f"2^{i} == {2**i}")

ccc = [1,2,3,4,5,5]
i = 0
while i < len (ccc):
    print(f"pod ind {i} ---- {ccc[i]}
    i += 1
for el in ccc:
print(el)

inp = int(input())
for el in ccc:
    if inp == el:
        print("jest taki element")
        cz_jest = True
        break
if cz_jest:
    print ("jest")
else:
    print("nie ma")

i = 0
while i < len (ccc):
    for inp == ccc[i]:
    cz_jest = True
    break
i += 1

if cz_jest:
    print("jest")

else:
    print("nie ma")

    




