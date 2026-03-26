from random import randint, choice

class Uczen:
    def __init__(self, imie):
        self.leczenie = randint(1, 10)
        self.atak = randint(1, 20)
        self.hp = randint(50, 200)
        self.imie = imie
        self.math = []
        self.plecak = []

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


    def dodaj_item(self, item):
        self.plecak.append(item)
        print(f"{self.imie} dostał: {item}")

    #pokaz co mamy w plecaku
    def pokaz_plecak(self):
        print(f"plecak {self.imie}: {self.plecak}")

    
    def uzyj_item(self, item):
        if item in self.plecak:
            if item == "kanapka":
                self.hp += 20
                print(f"{self.imie} użył kanapki! +20 HP")

            elif item == "dlugopis":
                self.atak += 5
                print(f"{self.imie} użył dlugopisu! +5 ataku")

            elif item == "ksiazka":
                self.hp += 10
                print(f"{self.imie} użył ksiqzki! +10 HP")

            self.plecak.remove(item)
        else:
            print("Nie masz tego przedmiotu")



u1 = Uczen("Adam")
u2 = Uczen("Dawid")

# losujemy
itemy = ["dlugopis", "kanapka", "ksiazka"]

for _ in range(2):
    u1.dodaj_item(choice(itemy))
    u2.dodaj_item(choice(itemy))

u1.pokaz_plecak()
u2.pokaz_plecak()

#walka
while u1.czy_zyje() and u2.czy_zyje():
    print("\n--- NOWA TURA ---")

    # u1 atakuje
    dmg = u1.atakuje()
    u2.take_dps(dmg)
    print(f"{u1.imie} zadaje {dmg} dmg")

    # u1 czasem używa itemu
    if u1.placaj:
        u1.uzyj_item(u1.plecak[0])

    if not u2.czy_zyje():
        break

    # u2 atakuje
    dmg = u2.atakuje()
    u1.take_dps(dmg)
    print(f"{u2.imie} zadaje {dmg} dmg")

    # u2 używa itemu
    if u2.plecaj:
        u2.uzyj_item(u2.plecak[0])

print("\nKONIEC WALKI")
print(f"{u1.imie} HP: {u1.hp}")
print(f"{u2.imie} HP: {u2.hp}")