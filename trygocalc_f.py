import math
# wartosci liczby pi
pi = math.pi


## funkcja obsługująca obliczanie pól powierzchni figur płaskich
## jak ktos z menu głównego wybiera 'a'
def obsluga_pol_figur():
    print('''
    wybierz co chcesz policzyć
    a - pp kwadatu
    b - pp prostokata
    c - pp trójkąta
    d - pp trapezu
    e - pp równolegloboku
    f - pp romb
    g - pp koło
    ''')

    # pytam dla jakiej figury policzyć pole pow.
    inp = input("? ")

    # sprawdzam jaką figurę wybrał użytkownik - co wpisał w input()
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
        pptrapezu = (a+b) * h  / 2
        print(f"Pole powierzchni trapezu o podstawie {a} i {b} i wysokosci {h} = {pptrapezu}")
    elif inp == "e":
        a = float(input("podaj dlugosc boku (a): "))
        h = float(input("podaj dlugosc wysokosci (h): "))
        print(f"polo powierzchni równolegloboku o podstawie {a} i wysokosci {h} = {a*h}")
    else:
        print("tego nie obsługujemy")

## funkcja obsługująca obliczanie pól powierzchni brył
## jak ktos z menu głównego wybiera 'b'
def obsluga_pol_bryl():
    print('''
    a - pp szescianu
    b - pp prostoadloscianu
    c - pp graniastoslup prosty 
    d - pp ostroslup 
    e - pp walec
    f - pp stozek
    g - pp kula
    
    ''')

    # pytam dla jakiej fbryły policzyć pole pow.
    inp = input("? ")

    # sprawdzam co w input() wpisał użytkownik
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

    elif inp == "d":
        a = float(input("podaj dlugosc pola podstawy (a)"))
        b = float(input("podaj dlugodc pola bocznego (b)"))
        pco = a + b
        print(f"pole calkowite ostroslupa o polu podstawy {a} i polu bocznego {b} = {pco}")

    elif inp == "e":
        r = float(inp("podaj dlugosc promienia podstawy (r): "))
        H = float(input("podaj dlugosc wysokosci walca (H):"))
        pcw = 2 * pi * r * (r + H)
        print(f"podaj pole calkowite walca o promieniu podstawy {r} i wysokosci {H} = {pcw}")

    elif inp == "f":
        r = float(input("podaj dlugosc promienia podstawy (r):"))
        H = float(input("podaj dlugosc wysokosci stozka (H):"))
        pcs = pi * r**2 + pi * r * H
        print(f"podaj pole calkowite stozka o promieniu podstawy {r} i wysokosci {H} = {pcs}")

    elif inp == "g":
        r = float(input("podaj dlugosc promienia kuli (r):"))
        pk = 4/3 * pi * r**3
        print(f"podaj pole calkowite kuli o promieniu {r} = {pk}")
    else:
        print(f"Opcja niedostępna")

## funkcja obsługująca obliczanie obwodów figur
## jak ktos z menu głównego wybiera 'c'
def obsluga_obw_figur():
    print('''
    Wybierz figure:
    a - kwadrat
    b - prostokat
    c - trojkat
    d - trapez
    e - rownoleglobok
    f - romb
    g - kola''')
    
    # pytam dla jakiej figury policzyć obwód
    inp = input("? ")

    #sprawdzam co w input() wpisał użytkownik
    if inp == "a":
        a = float(input("podaj dlugosc boku kwadratu (a):"))
        print(f"obwod kwadratu o boku {a} = {4*a}")

    elif inp == "b":
        a = float(input("podaj dlugosc boku (a):"))
        b = float(input("podaj dlugosc boku (b):"))
        print(f"obwod prostokata o bokach {a} i {b} = {2*(a+b)}")
        
    elif inp == "c":
        a = float(input("podaj dligosc boku (a):"))
        b = float(input("podaj dlugosc boku (b):"))
        c = float(input("podaj dlugosc boku (c):"))
        print(f" obwod trojkata o bokach {a} i {b} i {c} = {a+b+c}")
        

    elif inp == "d":
        a = float(input("podaj dlugosc boku (a):"))
        b = float(input("podaj dlugosc boku (b):"))
        c = float(input("podaj dlugosc boku (c):"))
        d = float(input("podaj dlugosc boku (d):"))
        print(f"obwod trapezu o bokach {a} i {b} i {c} i {d} = {a+b+c+d}")

    elif inp == "e":
        a = float(input("podaj dlugosc boku (a):"))
        b = float(input("podaj dlugosc boku (b):"))
        print(f"obwod rownolegloboku o bokach {a} i {b} = {2*a + 2*b }")


    elif inp == "f":
        a = float(input("podaj dlugosc boku (a):"))
        b = float(input("podaj dlugosc boku (b):"))
        print(f"obwod rombu o bokach {a} i {b} = {4*a}")

    elif inp == "g":
        r = float(input("podaj dlugosc promienia (r):"))
        print(f"obwod kola o promieniu {r} = {2*pi*r}")
    else:
        print("zła komenda")

## funkcja obsługująca obliczanie objętości brył
## jak ktos z menu głównego wybiera 'd'
def obsluga_obj_bryl():
    print('''
    objetosci bryl
    a - o szescian
    b - o prostopadlocian
    c - o graniastoslup
    d - o ostroslup
    e - o walec
    f - o stozek
    g - kula''')

    # pytam dla jakiej bryły policzyć objętość 
    inp = input("? ")

    # sprawdzam co w input() wpisał użytkownik
    if inp == "a":
        a = float(input("podaj dlugosc krawedzi (a):"))
        print(f"objetosc szescianu o krawedzi {a} = {a**3}")

    elif inp == "b":
        a = float(input("podaj dlugosc krawedzi (a):"))
        b = float(input("podaj dlugosc krawedzi (b):"))
        c = float(input("podaj dlugosc krawedzi (c):"))
        print(f"objetosc prostopadlocianu o krawedzi {a} i krawedzi {b} i krawedzi {c} = {a*b*c}")

    elif inp == "c":
        a = float(input("podaj dlugosc krawedzi (a): "))
        b = float(input("podaj dlugosc krawedzi (b):"))
        H = float(input("podaj dlugosc wysokosci (H):"))
        print(f"objetosc graniastoslupa o krawedzi {a} i krawedzi {b} i wysokosci {H} = {a*b*H}")

    elif inp == "d":
        a = float(input("podaj dlugosc krawedzi (a): "))
        H = float(input("podaj dlugosc wysokosci (H):"))
        print(f"objetosc ostroslupa o krawedzi {a} i wysokosci {H} = {1/3*a**2*H}")

    elif inp == "e":
        r = float(input("podaj dlugosc promienia podstawy (r): "))
        H = float(input("podaj dlugosc wysokosci walca (H):"))
        print(f"objetosc walca o promieniu podstawy {r} i wysokosci {H} = {pi*r**2*H}")

    elif inp == "f":
        r = float(input("podaj dlugosc promienia podstawy (r):"))
        H = float(input("podaj dlugosc wysokosci stozka (H):"))
        print(f"objetosc stozka o promieniu podstawy {r} i wysokosci {H} = {1/3*pi*r**2*H}")

    elif inp == "g":
        r = float(input("podaj dlugosc promienia kuli (r):"))
        print(f"objetosc kuli o promieniu {r} = {4/3*pi*r**3}")
    else:
        print("tego jeszcze nie obsługujemy")



## tu zaczyna się wykonanie programu
## główna pętla
while True:
    print('''
        
        ### KALKULATOR TRYGONOMETRYCZNY ###
        
        Chcesz pracować z figurami czy bryłami
        a - Figury
        b - Bryły
        c - obwod figury
        d - obwod bryły

        q - wyjście
        ''')

    # menu główne - wybieramy co chcemy liczyć
    # w zalezności od tego co wybierzemy z menu głównego
    # odpalona zostanie zdefiniowana wczesniej funkcja

    menu0 = input("a / b / c / d ? ")

    if menu0 == "a":
        # odpalam funkcje która zapyta o typ figury a następnie policzy jej pole pow.
        obsluga_pol_figur() 

    elif menu0 == "b":
        # odpalam funkcje która zapyta o typ bryły a następnie policzy jej pole pow.
        obsluga_pol_bryl()

    elif menu0 == "c":
        # odpalam funkcje która zapyta o typ figury a następnie policzy jej obwód
        obsluga_obw_figur()

    elif menu0 == "d":
        # odpalam funkcje która zapyta o typ bryły a następnie policzy jej objętość
        obsluga_obj_bryl()
    
    elif menu0 == "q":
        # przerywam pętlę while True - kończę program
        print("dziekuję")
        break

    else:
        # jesli ktoś z menu głównego wybierze opcję której nie obsługuję (coś innego jak a, b, c, d)
        print("Nie ma takiej komendy")
