

print('''
    Chcesz pracować z figurami czy bryłami
    a - Figury
    b - Bryły
    ...

    ''')


menu0 = input("a / b ? ")
if "a" == menu0:
    print('''
    wybierz co chcesz policzyć
    a - pp kwadatu
    b - pp prostokata
    c - pp trójkąta
    d - pp trapezu
    e - pp równolegloboku
    f - pp romb
    g - pp koło
    ...

    ''')
    inp = input("? ")

    if inp == "a":
        a_str = input("podaj długoś boku kwadratu a: ")
        a = float(a_str)
        print(f"Pole powierzchni kwadratu o boku {a} = {a**2}")
    elif inp == "b":
        a = input("Podaj boku a prostokąta: ")
        b = input("Podaj boku b prostokąta: ")
        print(f"Pole powierzchni kwadratu o bokach {a} i {b} = {float(a) * float(b)}")
    elif inp == "c":
        a = float(  input("podaj długoś podstawy trójkata (a): ")   )
        h = float(input("podaj długość wysokosci trójkata (h): "))
        ppt = a * h / 2
        print(f"Pole powierzchni trójkata o podstawie {a} i wysokosci {h} = {ppt}")
    elif inp == "d":
        a = b = 0

        a = float(input("podaj długośc podstawy (a): "))

        # while a == b:
            # a = float(input("podaj długośc podstawy (a): "))
            # b = float(input("podaj długosc podstawy (b): "))
        while True:
            b = float(input("podaj długosc podstawy (b): "))
            if a == b:
                print(f"Długości podstaw trapezu powinny być różne. Dla podstawy b proszę wpisać wartość różną od {a}")
            else:
                break

        h = float(input("podaj długosc wysokosci (h): "))
        pptrapezu = (a+b) * h / 2
        print(f"Pole powierzchni trapezu o podstawie {a} i {b} i wysokosci {h} = {pptrapezu}")
    elif inp == "e":
        a = float(input("podaj dlugosc boku (a): "))
        h = float(input("podaj dlugosc wysokosci (h): "))
        print(f"polo powierzchni równolegloboku o podstawie {a} i wysokosci {h} = {a*h}")
    else:
        print("tego nie obsługujemy")

elif "b" == menu0:
    print('''
    a - pp szescianu
    b - pp prostoadloscianu
    c - pp graniastoslup prosty 
    ...

    ''')
    inp = input("?")
    if inp == "a":
        a = float(input("a = "))
        print(f"ppSzecianu dla a={a} = {a**2*6}")  

    elif inp == "b":
        a = float(input("podaj dlugosc krawedzi (a):"))
        b = float(input("podaj dlugosc krawedzi (b):"))
        c = float(input("podaj dlugosc krawedzi (c):"))
        pcp = 2*(a*b + b*c + a*c)
        print(f"pole calkowite prostopadlocianu o krawedzi {a} i krawedzi {b} i krawedzi {c} = {pcp}")

    elif inp == "c":
        a = float(input("podaj dlugosc krawedzi (a): "))
        b = float(input("podaj dlugosc krawedzi (b):"))
        pcg = 2*a + b
        print(f"pole calkowitwe graniastoslupa o krawedzi {a} i krawedzi {b} = {pcg}")
else:
    print("Nie ma takiej komendy")
