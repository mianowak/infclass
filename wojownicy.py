import random

class Wojownik:



#tworzymy dane kazdego z przeciwnikow, które potem będą losowane w grze

    def __init__(

        self,
        imie,
        poziom,
        hp,
        obrazenia,
        bron,
        wyglad,
        opis

    ):



#zapisujemy dane

        self.imie = imie
        self.poziom = poziom
        self.hp = hp
        self.obrazenia = obrazenia
        self.bron = bron
        self.wyglad = wyglad
        self.opis = opis



#pokazujemy informacje o danym przeciwniku

    def pokaz_info(self):

        print("PRZECIWNIK")

        print(f"Imię: {self.imie}")
        print(f"Poziom: {self.poziom}")
        print(f"HP: {self.hp}")
        print(f"Obrażenia: {self.obrazenia}")
        print(f"Broń: {self.bron}")

        print("\nWygląd:")
        print(self.wyglad)

        print("\nOpis:")
        print(self.opis)




#poziom 1

raven = Wojownik(

    imie="Raven",

    poziom=1,

    hp=60,

    obrazenia=10,

    bron="Krótki nóż",

    wyglad="""
Niski chłopak w ciemnym kapturze.
Ma szarą bluzę i stare rękawice.
W ręku trzyma mały nóż.
""",

    opis="""
Raven jest szybki i zwinny.
Lubi atakować znienacka.
"""
)



korin = Wojownik(

    imie="Korin",

    poziom=1,

    hp=70,

    obrazenia=12,

    bron="Drewniana pałka",

    wyglad="""
Ma szerokie ramiona i krótkie włosy.
Nosi skórzaną kamizelkę.
W ręku trzyma ciężką pałkę.
""",

    opis="""
Korin nie jest bardzo inteligentny,
ale posiada dużą siłę.
"""
)

Torina = Wojownik(

    imie="Torina",

    poziom=1,

    hp=70,

    obrazenia=12,

    bron="Drewniana pałka",

    wyglad="""
Ma szerokie ramiona i krótkie włosy.
Nosi skórzaną kamizelkę.
W ręku trzyma ciężką pałkę.
""",

    opis="""
Torina nie jest bardzo inteligentna,
ale posiada dużą siłę.
"""
)


#poziom 2

drex = Wojownik(

    imie="Drex",

    poziom=2,

    hp=90,

    obrazenia=18,

    bron="Miecz",

    wyglad="""
Wysoki wojownik z blizną na twarzy.
Ma ciemną zbroję i czerwony płaszcz.
Trzeba na niego uwazac bo jest bardzo agresywny.
Przy pasie nosi długi miecz.
""",

    opis="""
Drex był dawniej żołnierzem.
Jest agresywny podczas walki.
Jest szybki i dobrze przewiduje ruchy przeciwnika.
"""
)



selric = Wojownik(

    imie="Selric",

    poziom=2,

    hp=100,

    obrazenia=20,

    bron="Topór",

    wyglad="""
Ogromny mężczyzna w ciężkiej zbroi.
Ma brodę i metalowe rękawice.
W rękach trzyma wielki topór.
""",

    opis="""
Selric jest powolny,
ale jego ataki są bardzo silne.
Jest trudny do pokonania, 
ponieważ jego zbroja chroni go przed większością ciosów.
"""
)



#poziom 3

nyro = Wojownik(

    imie="Nyro",

    poziom=3,

    hp=120,

    obrazenia=24,

    bron="Dwa sztylety",

    wyglad="""
Chudy wojownik ubrany na czarno.
Jego twarz zasłania maska.
W obu dłoniach trzyma sztylety.
""",

    opis="""
Nyro walczy niezwykle szybko.
Bardzo trudno go trafić.
szybko atakuje i równie szybko się wycofuje.
"""
)



valen = Wojownik(

    imie="Valen",

    poziom=3,

    hp=130,

    obrazenia=25,

    bron="Włócznia",

    wyglad="""
Ma długie blond włosy i srebrną zbroję.
Na plecach nosi włócznię.
""",

    opis="""
Valen utrzymuje przeciwników na dystans
i dobrze przewiduje ruchy wroga.
Jego włócznia jest bardzo szybka i precyzyjna.
"""
)



#poziom 4

kaelor = Wojownik(

    imie="Kaelor",

    poziom=4,

    hp=160,

    obrazenia=35,

    bron="Królewski miecz",

    wyglad="""
Kaelor nosi czarną zbroję ze złotymi znakami.
Ma długi płaszcz i zimne spojrzenie.
W ręku trzyma błyszczący miecz.
""",

    opis="""
Kaelor przez lata trenował walkę.
Jest jednym z najlepszych wojowników królestwa.
Jego ataki są szybkie i precyzyjne.
"""
)



varkos = Wojownik(

    imie="Varkos",

    poziom=4,

    hp=180,

    obrazenia=38,

    bron="Ogromny topór",

    wyglad="""
Bardzo wysoki wojownik z licznymi bliznami.
Ma ciężką metalową zbroję.
Nosi ogromny topór.
""",

    opis="""
Varkos posiada ogromną siłę.
Jeden cios może powalić przeciwnika.
Jest trudny do pokonania,
ponieważ jego zbroja chroni go przed większością ataków.
"""
)



#poziom 5
# Najtrudniejszy przeciwnik-boss


azrath = Wojownik(

    imie="Azrath",

    poziom=5,

    hp=300,

    obrazenia=50,

    bron="Czarny miecz",

    wyglad="""
Azrath nosi ciemną zbroję pokrytą srebrnymi znakami.
Jego oczy świecą czerwonym kolorem.
W dłoni trzyma długi czarny miecz.
""",

    opis="""
Azrath jest legendarnym wojownikiem.
Pokonał setki przeciwników.
Prawie nikt nie przeżył walki z nim.
"""
)



# lista przeciwników podzielona na poziomy trudności

poziom_1 = [raven, korin, Torina]

poziom_2 = [drex, selric]

poziom_3 = [nyro, valen]

poziom_4 = [kaelor, varkos]

poziom_5 = [azrath]



# Ta funkcja losuje wojownika

def losuj_wojownika(poziom):



    if poziom == 1:

        return random.choice(poziom_1)



    elif poziom == 2:

        return random.choice(poziom_2)



    elif poziom == 3:

        return random.choice(poziom_3)



    elif poziom == 4:

        return random.choice(poziom_4)



    elif poziom == 5:

        return random.choice(poziom_5)



    else:

        print("Nie ma takiego poziomu!")

        return None



print("LOSOWANIE PRZECIWNIKA")



poziom = int(input("Wybierz poziom od 1 do 5: "))


przeciwnik = losuj_wojownika(poziom)


if przeciwnik:

    przeciwnik.pokaz_info()
