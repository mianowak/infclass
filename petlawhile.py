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