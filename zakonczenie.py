def zakonczenie(bohater):

    print("OSTATNIA WALKA")
    
    print(f"""
Po przejściu wszystkich poziomów areny
{bohater.imie}
stanął naprzeciwko Azratha.

Walka była brutalna.

Czarny miecz Azratha
wielokrotnie omal nie zakończył walki.

Arena ucichła,
gdy ostatni cios powalił wojownika na ziemię.

Azrath był pokonany.

Publiczność obserwowała każdy ruch.

Strażnicy czekali na decyzję zwycięzcy.

Los całego królestwa zależał teraz
od jednej decyzji.
""")

# gracz wybiera sobie zakonczenie

    print("Wybierz zakończenie:\n")

    print("1 - Zabij Azratha")
    print("2 - Oszczędź go i wybierz pokój")




    wybor = input("Wpisz 1 lub 2: ")


#1 zakonczenie

    if wybor == "1":



        print("ZAKOŃCZENIE — KRWAWY TRON")



        print(f"""
{bohater.imie}
powoli podniósł broń.

Arena była całkowicie cicha.

Po chwili ostrze przecięło powietrze,
kończąc życie Azratha.

Publiczność zaczęła krzyczeć,
a strażnicy uklękli przed nowym zwycięzcą.

Od tamtego dnia
{bohater.imie}
stał się najpotężniejszą osobą w królestwie.

Arena nadal działała.

Walki nigdy się nie skończyły.

Ludzie zaczęli bać się nowego władcy,
tak samo jak kiedyś bali się Azratha.

Królestwo przetrwało —
ale nadal było pełne przemocy.
""")

# 2 zakonczenie

    elif wybor == "2":

        print("ZAKOŃCZENIE — NOWY POCZĄTEK")

        print(f"""
{bohater.imie}
opuścił broń.

Azrath spojrzał na arenę w milczeniu.

Publiczność nie rozumiała,
dlaczego zwycięzca oszczędził przeciwnika.

Po raz pierwszy od wielu lat
arena nie zakończyła się śmiercią.

Wieść o tej decyzji szybko rozeszła się
po całym królestwie.

Ludzie zaczęli wierzyć,
że świat może się zmienić.

Walki na arenie zostały zakończone,
a strażnicy stracili władzę nad mieszkańcami.

{bohater.imie}
stał się symbolem nadziei
i pokoju.
""")


#bledny wybor
    else:

        print("Niepoprawny wybór.")
