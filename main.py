from bohaterowie import wybierz_bohatera
from wojownicy import losuj_wojownika
from historia import rozpocznij_historie
from zakonczenie import zakonczenie


print("BEZSILNA — RPG")



gracz = wybierz_bohatera()

if gracz:

    rozpocznij_historie(gracz)


    for poziom in range(1, 6):

        print(f"POZIOM {poziom}")



        przeciwnik = losuj_wojownika(poziom)


        if przeciwnik:

            przeciwnik.pokaz_info()

            print(f"""
{gracz.imie} wszedł na arenę.

Naprzeciwko stał:
{przeciwnik.imie}.

Przeciwnik trzymał:
{przeciwnik.bron}.

{przeciwnik.imie} wyglądał groźnie.

{przeciwnik.opis}

Publiczność obserwowała każdy ruch.

{gracz.imie}
mocniej chwycił swoją broń:
{gracz.bron}.

Walka właśnie się rozpoczęła.
""")


            print(f"""
Po długiej walce
{gracz.imie}
pokonał przeciwnika:
{przeciwnik.imie}.
""")



            input("Kliknij ENTER aby przejść dalej...")


    zakonczenie(gracz)



else:

    print("Gra została zakończona.")
