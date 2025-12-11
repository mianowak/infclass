
import random
from dictionaries import bohaterowie
from dictionaries import wrogowie
from dictionaries import mapa

print("""*******************************************************
          Witaj w Krainie Cieni!
*******************************************************

Od wieków w tej krainie panował spokój i dostatek. 
Jednak pewnej nocy mroczne siły pojawiły się w lasach i wioskach, 
zagrażając bezpieczeństwu mieszkańców.  

Ty, odważny bohater, stajesz przed wyborem swojej drogi: 
czy staniesz do walki z potworami, odkryjesz tajemnice starożytnych ruin 
czy pomożesz mieszkańcom w potrzebie?  

Twoja przygoda właśnie się zaczyna...
Przygotuj się na niebezpieczeństwa, tajemnice i wielkie wyzwania!

*******************************************************""")

def wybor_postaci():
    print("""
    **********************
        WYBÓR POSTACI
    **********************
        """)
    # tablica tymczasowa żeby wpisać klucze z typami bohaterów "Rycerz Herbowy", "Elfi łucznik", "Krasnoludzki młociarz"
    # nazwy są dlugie i wybieranie po nazwie jest meczące
    tabela_tymczasowa = []
    idx = 0
    for key, value in bohaterowie.items():
        # zapamietuje w tablicy tymczasowej klucze "Rycerz Herbowy", "Elfi łucznik", "Krasnoludzki młociarz"
        tabela_tymczasowa.append(key)
        idx += 1
        print(f"    {idx}:   {key}  {value['name']}  zdrowie:{value['hp']}, atak:{value['attack']}, obrona:{value['defence']}")

    while True:
        # tu oczekuję że gracz wpisze 1,2,3 jako wybor postaci
        idx_wybranej_postaci = int(input("\nWybierz jedną z postaci > "))
        
        # sprawdzam czy gracz wybral wiecej jak 0 al mniej lub rowne dlugosci tablicy tymczasowej
        # teraz tablica tymczasowa ma 3 elementy wiec  3 <= idx_wybranej_postaci > 0
        if idx_wybranej_postaci > 0 and idx_wybranej_postaci <= len(tabela_tymczasowa):
            # tablica zaczyna sie od indeksu 0 wiec jak gracz wpisze 1 to musimy pobrac klucz z indeksu 0, jak wpisze 2 to z indeksu 1 - dlatego odejmuje 1
            wybrana_postac = bohaterowie[tabela_tymczasowa[idx_wybranej_postaci - 1]]
            return wybrana_postac

def opis_postaci(postac):
    print(
        f"""
    *******************************
        {postac['name']}
    *******************************
        """)
    for key, value in postac.items():
        print(f"    {key}:  {value}")

def obsluga_pola(pole, postac):
    print("Jesteś", pole["pole"])
    if "zabudowa" in pole and pole["zabudowa"] != None:
        if pole["zabudowa"] == "Brama":
            print("przed Tobą", pole["zabudowa"])
        else:
            print("obok Ciebie stoi", pole["zabudowa"])
    if "postac" in pole and pole["postac"] != None:
        if pole["postac"] == "Wilki":
            print(f"Jest tu wataha Wilków")
        else:
            print(f"Jest tu {pole['postac']}")

def odmien(zabudowa):
    if zabudowa == "Karczma":
        return "KARCZMY"
    elif zabudowa == "Tajemniczy las":
        return "TAJEMNICZY LAS"
    elif zabudowa == "Stara zniszczona stodoła":
        return "STAREJ, ZNISZCZONEJ STODOŁY"
    elif zabudowa == "Chłopska chata":
        return "CHŁOPSKIEJ CHATY"
    elif zabudowa == "Zniszczona chłopska chata":
        return "ZNISZCZONEJ CHŁOPSKIEJ CHATY"
    elif zabudowa == "Jaskinia":
        return "JASKINI"

def obslug_karczmy(postac):
    print("""
    Straszny tu gwar,
    wszędzie pełno zapijaczonych wieśniaków,
    jest miejsce przy szynkwasie
    """)

    while True:
        trzezwosc = postac['hp'] / 2
        print("\n    Co robisz")
        print("    [b] - dawaj tu kufel piwa, [h] - podaj mi puchar miodu, [q] - wyjście")
        a = input("> ")
        if a == "b":
            trzezwosc -= 3
            if (trzezwosc <= 0):
                print("Upiłeś się... Wykopali Cię z karczmy")
        elif a == "h":
            trzezwosc -= 4
            if (trzezwosc <= 0):
                print("Upiłeś się... Wykopali Cię z karczmy")
        elif a == "q":
            break

def obslug_sklepu(postac):
    print("""
    Wszędzie rozchodzi się smród ziół 
    i ostra woń eliksirów,
    za stołem kupiec
    """)

    while True:
        print(f"\n    Co robisz  [sakiewka: {postac['wallet']}$]")
        print("    [z] -  kupuje Small Health Potion (3$), [a] - kupuję Big Health Potion (4$), [b] - Small Attack Potion, [c] - Big attack Potion, [q] - wyjście")
        a = input("> ")
        if a == "z":
            if postac["wallet"] >= 3:
                postac["wallet"] -= 3
                postac["hp"] += random.randint(2, 5)
                
                print(F"Twoje zdrowie wzrosło do: {postac['hp']}")
            else:
                print(f"Nie masz pieniedzy... zostało Ci {postac['wallet']}$")
        elif a == "a":
            if postac["wallet"] >= 4:
                postac["wallet"] -= 4
                postac["attack"] += random.randint(1, 4)
                
                print(F"Siła Twojego ataku wzrosła do: {postac['attack']}")
            else:
                print(f"Nie masz pieniedzy... zostało Ci {postac['wallet']}$")
        elif a == "q":
            break
        
def obsluga_zabudowy(postac, zabudowa):
    print(
        f"""
    *************************************
        WSZEDŁEŚ DO: {odmien(zabudowa)}
    *************************************
        """)
    
    if zabudowa == "Karczma":
        obslug_karczmy(postac)
    if zabudowa == "Sklep":
        obslug_sklepu(postac)
    
    
def obsluga_walki(postac, wrog):
    print(
        f"""
    *************************************
        WALKA Z: {wrog['name']}
    *************************************
        """)
    {opis_postaci(wrog)}
    while True:
        print(f"\n    Co robisz  Twoje zdrowie:{postac['hp']},  zdrowie wroga:{wrog['hp']}")
        print("    [a] - atakuje, [u] - uciekam")
        a = input("> ")
        if a == "u":
            break
    
        print("Ataaaak...")
        # atakuje bohater
        r = postac["attack"] - wrog["defence"]
        if r > 0:
            print(f"    wróg traci {r} hp")
            wrog['hp'] -= r
        
        # oddaje potwor
        print("Zasłona...")
        if wrog['hp'] > 0:
            r = wrog["attack"] - postac["defence"]
            if r > 0:
                print(f"    tracisz {r} hp")
                postac['hp'] -= r
        
        if postac['hp'] < 8:
            print(f"UWAGA! Niski poziom zdrowia: {postac['hp']}")

def glowna_petla(postac):
    # m - to znacznik pozycji na mapie
    # m zwieksza sie kiedy bohater idzie naprzód
    m = 0;
    while True:
        # obsluga_pola to prosta funkcja która wypisuje opis pola na którym stoi gracz
        obsluga_pola(mapa[m], postac)
        print("\n    Co robisz")
        print("    [p] - ide naprzód, [w] - wchodzę, [a] - atakuję, [q] - wyjście")
        a = input("> ")
        if a == "p":
            m += 1
        elif a == "w":
            # jesli na polu jest brama to mozna wejsc ale wejscie do bramy oznacza wejscie do miasta albo wyjscie z miasta
            # dlatego klawisz 'w' w przypadku bramy obsługiwany jest jak "Ide naprzód"
            if mapa[m]["zabudowa"] == "Brama":
                m+= 1
            else:
                # jesli to nie brama tylko sklep albo karczma to wchodzimy do środka
                # i sterowanie przejmuje obsluga_zabudowy
                obsluga_zabudowy(postac, mapa[m]["zabudowa"])
        elif a == "a":
            if mapa[m]["postac"] == None:
                print("    Na tym polu nie masz przeciwnika...")
            else:
                obsluga_walki(postac, wrogowie[mapa[m]["postac"]])
        elif a == "q":
            break
    


def main():
    print("Gra RPG")
    # odpalam funkcje wyporu postaci i zapamietuje wybor w zmiennej wybrana_postac
    wybrana_postac = wybor_postaci()
    # wypisuje parametry postaci
    opis_postaci(wybrana_postac)
    print("Wchodzisz do gry...")
    #odpalam główną pętlę gry, któ jest w funkcji glowna_petla
    glowna_petla(wybrana_postac)

# tu sie wszystko zaczyna - odpalamy główną funkcję
main()
