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