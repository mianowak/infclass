from random import randint, choice

class Uczen:
    def __init__(self, imie):
        self.leczenie = randint(1, 10)
        self.atak = randint(1, 20)
        self.hp = randint(50, 200)
        self.imie = imie
        self.math = []
        self.ekwipunek = []

    def dodaj_ocena(self, ocena: int) -> None:
        self.math.append(ocena)

    def atakuje(self) -> int:
        return self.atak

    def czy_zyje(self):
        if self.hp <= 0:
            self.zyje = False
            return False
        return True

    def take_dps(self, dps) -> bool:
        self.hp -= dps
        if self.hp <= 0:
            self.zyje = False
            return False
        return True

    def dodaje_hp(self) -> int:
        self.hp += self.leczenie
        return self.hp

    # dodajemy item y
    def dodaj_item(self, item):
        self.ekwipunek.append(item)
        print(f"{self.imie} dostał: {item}")

    # robimy tak zeby pokazal nam ekwipunek
    def pokaz_eq(self):
        print(f"Ekwipunek {self.imie}: {self.ekwipunek}")

    # uzywamy itemow
    def uzyj_item(self, item):
        if item in self.ekwipunek:
            if item == "kanapka":
                self.hp += 20
                print(f"{self.imie} użył kanapki! +10HP")

            elif item == "dlugopis":
                self.atak += 5
                print(f"{self.imie} użył dlugopisu! +5 ataku")

            elif item == "ksiazka":
                self.hp += 10
                print(f"{self.imie} użył ksiazki! +5 HP")

            self.ekwipunek.remove(item)
        else:
            print("Nie masz tego przedmiotu")



# rodzaje uczniow do wyboru
class Kreatywny(Uczen):
    def __init__(self, imie):
        super().__init__(imie)
        self.atak += 10
        self.hp += 30

class Pilny(Uczen):
    def __init__(self, imie):
        super().__init__(imie)
        self.leczenie += 10

class Spokojny(Uczen):
    def __init__(self, imie):
        super().__init__(imie)
        self.hp += 60
        self.atak -= 5

class Aktywny(Uczen):
    def __init__(self, imie):
        super().__init__(imie)
        self.atak += 5

    def atakuje(self):
        # szansa na podwójny strzał
        if randint(1, 3) == 1:
            print("Podwójny strzał!")
            return self.atak * 2
        return self.atak
# wybor swojej postaci
print("Wybierz ucznia:")
print("1 - Kreatywny")
print("2 - Pilny")
print("3 - Spokojny")
print("4 - Aktywny")

wybor = input("Twój wybór: ")

if wybor == "1":
    u1 = Kreatywny("Gracz")
elif wybor == "2":
    u1 = Pilny("Gracz")
elif wybor == "3":
    u1 = Spokojny("Gracz")
elif wybor == "4":
    u1 = Aktywny("Gracz")
else:
    u1 = Uczen("Gracz")
    
klasy = [Kreatywny, Pilny, Spokojny, Aktywny]
u2 = choice(klasy)("Bot")


# losowanie jaki item wyciagnie z plecaka
itemy = ["dlugopis", "kanapka", "ksiazka"]

for _ in range(2):
    u1.dodaj_item(choice(itemy))
    u2.dodaj_item(choice(itemy))

u1.pokaz_eq()
u2.pokaz_eq()

# walka
while u1.czy_zyje() and u2.czy_zyje():
    print("Tura")

    # u1 atakuje
    dmg = u1.atakuje()
    u2.take_dps(dmg)
    print(f"{u1.imie} zadaje {dmg} dmg")


    # teraz losujemy o ile leczy swoje hp uczen 1
    if randint(1, 3) == 1:
        u1.dodaje_hp()


        
    # u1 czasem używa itemu
    if u1.ekwipunek:
        u1.uzyj_item(u1.ekwipunek[0])

    if not u2.czy_zyje():
        break

    # u2 atakuje
    dmg = u2.atakuje()
    u1.take_dps(dmg)
    print(f"{u2.imie} zadaje {dmg} dmg")


    # teraz losujemy o ile ulepszy swoje hp uczen 2
    if randint(1, 3) == 1:
        u1.dodaje_hp()


print("KONIEC WALKI")
print(f"Uczen HP: {u1.hp}")
print(f"Bot HP: {u2.hp}")