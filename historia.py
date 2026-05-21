def rozpocznij_historie(bohater):

    #rozpoczecie wejscie do gry, pokazanie historii swiata i bohatera

    print("HISTORIA")
    
     # wstep do swiata

    print(f"""
Królestwo Ilyria od wielu lat było podzielone.

Najsilniejsi mieszkańcy posiadali niezwykłe zdolności
i kontrolowali całe miasta.

Osoby bez mocy były ukrywane,
wyśmiewane
lub zabijane przez strażników.

W centrum stolicy znajdowała się ogromna arena.

To właśnie tam wojownicy walczyli
dla pieniędzy,
sławy
i rozrywki bogatych mieszkańców.

Każdy poziom areny był coraz trudniejszy.

Najgorsi przeciwnicy czekali na samym końcu.

Nikt nigdy nie pokonał ostatniego wojownika —
Azratha.
""")


#opis bohatera ktory zostal wybrany przez gracza
    print("TWÓJ BOHATER")



    print(f"""
Imię:
{bohater.imie}

Wiek:
{bohater.wiek}

Broń:
{bohater.bron}

Charakter:
{bohater.charakter}
""")



    print("Ekwipunek:")




    for rzecz in bohater.ekwipunek:

        print(f"- {rzecz}")



    print("Historia bohatera:")

    print(bohater.historia)



 

    print(f"""
Po wielu dniach podróży
{bohater.imie} dotarł do stolicy.

Miasto było pełne strażników,
dymu
i ludzi próbujących przetrwać.

Wszędzie można było usłyszeć rozmowy
o wojownikach areny.

Raven.
Drex.
Nyro.
Kaelor.

Każdy z nich pokonał dziesiątki przeciwników.

Jednak największy strach budził Azrath —
ostatni wojownik areny.

Mówiono,
że jego czarny miecz zakończył życie setek ludzi.

Mimo strachu
{bohater.imie}
postanowił wejść na arenę.

Tylko zwycięstwo mogło zmienić los królestwa.
""")

    print("ROZPOCZYNA SIĘ WALKA POMIEDZY TOBA A TWOIM PRZECIWNIKIEM")
