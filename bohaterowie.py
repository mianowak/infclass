# najpierw robimy klase zeby stworzyc bohaterów, a potem tworzymy gotowe postacie

class Bohater:


    def __init__(
        self,
        imie,
        wiek,
        bron,
        charakter,
        zycie,
        energia,
        ekwipunek,
        historia
    ):

        self.imie = imie
        self.wiek = wiek
        self.bron = bron
        self.charakter = charakter
        self.zycie = zycie
        self.energia = energia
        self.ekwipunek = ekwipunek
        self.historia = historia


    # FUNKCJA POKAZUJĄCA INFORMACJE O BOHATERZE
   

    def pokaz_informacje(self):

        print("INFORMACJE O BOHATERZE")

        print(f"Imię: {self.imie}")
        print(f"Wiek: {self.wiek}")
        print(f"Broń: {self.bron}")
        print(f"Charakter: {self.charakter}")
        print(f"Życie: {self.zycie}")
        print(f"Energia: {self.energia}")

        print("Ekwipunek:")


        # PĘTLA FOR
        # Przechodzi przez wszystkie przedmioty w liście ekwipunek.
       

        for rzecz in self.ekwipunek:
            print(f"- {rzecz}")

        print("\nHistoria:")
        print(self.historia)



# tworzymy postacie do wyboru dla gracza

paedyn = Bohater(

    imie="Paedyn Gray",

    wiek=18,

    bron="Sztylet",

    charakter="Sprytna, odważna, uparta",

    zycie=100,

    energia=100,

    ekwipunek=[
        "Sztylet",
        "Czarny płaszcz",
        "Mapa miasta",
        "Mała sakiewka monet",
        "Bandaże"
    ],

    historia="""
Paedyn od dzieciństwa musiała walczyć o przetrwanie.
Nie posiada żadnych mocy, dlatego ukrywa się przed
strażnikami i udaje osobę posiadającą zdolności.
Jest szybka, inteligentna i bardzo ostrożna.
Nie ufa łatwo ludziom.
"""
)


kai = Bohater(

    imie="Kai Azer",

    wiek=20,

    bron="Miecz",

    charakter="Spokojny, lojalny, inteligentny",

    zycie=120,

    energia=90,

    ekwipunek=[
        "Miecz",
        "Skórzana zbroja",
        "Bukłak z wodą",
        "Lina",
        "Rękawice"
    ],

    historia="""
Kai został wychowany wśród wojowników.
Nie lubi przemocy, ale potrafi walczyć.
Często analizuje sytuację zanim podejmie decyzję.
Jest lojalny wobec osób którym ufa.
"""
)



adena = Bohater(

    imie="Adena",

    wiek=19,

    bron="Łuk",

    charakter="Miła, szybka, sprytna",

    zycie=95,

    energia=110,

    ekwipunek=[
        "Łuk",
        "Kołczan strzał",
        "Peleryna",
        "Suszone jedzenie",
        "Mały nóż"
    ],

    historia="""
Adena uwielbia podróżować i poznawać nowe miejsca.
Potrafi bardzo dobrze strzelać z łuku.
Zawsze pomaga innym nawet jeśli sama wpada przez to
w niebezpieczeństwo.
"""
)



# LIAM

liam = Bohater(

    imie="Liam",

    wiek=21,

    bron="Topór",

    charakter="Silny, zabawny, odważny",

    zycie=140,

    energia=80,

    ekwipunek=[
        "Topór",
        "Metalowa tarcza",
        "Koc",
        "Pochodnia",
        "Torba podróżna"
    ],

    historia="""
Liam jest bardzo silny i dobrze radzi sobie
w walce wręcz.
Często żartuje nawet podczas niebezpiecznych sytuacji.
Nie poddaje się łatwo.
"""
)

juliette = Bohater(

    imie="Juliette",

    wiek=18,

    bron="Dwa sztylety",

    charakter="Cicha, sprytna, nieufna",

    zycie=95,

    energia=120,

    ekwipunek=[

        "Dwa sztylety",
        "Czarna peleryna",
        "Kompas",
        "Sakiewka monet",
        "Bandaże"

    ],

    historia="""
Juliette wychowała się na ulicach stolicy.
Od dziecka kradła jedzenie żeby przetrwać.
Nie ufa nikomu i zawsze planuje drogę ucieczki.
Mimo chłodnego charakteru potrafi chronić osoby
na których jej zależy.
"""
)


kenji = Bohater(

    imie="Kenji",

    wiek=21,

    bron="Włócznia",

    charakter="Pewny siebie, inteligentny, uparty",

    zycie=115,

    energia=100,

    ekwipunek=[

        "Włócznia",
        "Skórzana kurtka",
        "Monety",
        "Lina",
        "Mały notes"

    ],

    historia="""
Kenji przez wiele lat pracował jako posłaniec.
Zna niemal wszystkie drogi i sekrety miasta.
Uwielbia ryzyko i często podejmuje niebezpieczne decyzje.
Bardzo trudno zdobyć jego zaufanie.
"""
)

# Lista przechowuje wszystkich bohaterów
# Dzięki temu możemy później ich wyswietlic i zobaczyc w terminalu


lista_bohaterow = [
    paedyn,
    kai,
    adena,
    liam,
    juliette,
    kenji
]

#funkcja pokaze nam wszystkich bohaterów, pozwoli nam wybrać numer, zwroci wybraną postać



def wybierz_bohatera():

    
    print("WYBIERZ SWOJEGO BOHATERA")
    



    for numer, bohater in enumerate(lista_bohaterow, start=1):

        print(f"{numer}. {bohater.imie}")
        print(f"   Broń: {bohater.bron}")
        print(f"   Charakter: {bohater.charakter}")
        print(f"   Życie: {bohater.zycie}")
        print("")

    # tutah uzywamy int zeby zmienic takst a w tym przypadku bohatera na liczbe

    wybor = int(input("Wybierz numer bohatera: "))




    if wybor >= 1 and wybor <= len(lista_bohaterow):

        wybrany_bohater = lista_bohaterow[wybor - 1]

        print("Wybrano bohatera:")
        print(wybrany_bohater.imie)

        return wybrany_bohater

    else:

        print("Niepoprawny wybór!")

        return None
