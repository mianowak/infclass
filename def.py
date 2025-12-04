from math import sqrt

def czy_pierwsza(m:int)->bool:
    if m < 2:
        return False
    elif m == 2 or m == 3 :
        return True
    elif m % 2 == 0:
        return False
    i = 3
    while i <= sqrt(m):
        if m % i == 0:
            return False
        i += 2
    return True

def ile_pierwszych(m:int)->int:
    ile = 0
    for i in range(m):
        if czy_pierwsza(i):
            ile += 1
    return ile

def lista_liczb_pierwszych(m:int)->int:
    lst = []
    for i in range(m):
        if czy_pierwsza(i):
            lst.append(i)
    return lst

def interation(lst:list)->None:
    for i , v in enumerate(lst):
        print(f"{i}-------{v}")
