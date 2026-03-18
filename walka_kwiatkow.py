from random import randint

class Kwiatek:
    def _init_ (self,imie):
        self.imie = imie
        self.zyje = True
        self.hp = 100
        self.fotosynteza = 10
        
    def inf(self):
        print(f"""
        imie = {self.imie}
        zyje = {self.zyje}
        hp = {self.hp}
        """)
        
    def czy_zyje(self)->bool:
        if self.hp>0:
            return True
        self.zyje = False
            return False
            
    def atak(self):
        return randint (1,20)
        
    def take_dps (self,a):
        self.hp -= a
        
        
    def heal(self):   
        self.hp += self.fotosynteza
        if self.hp > 100:
            self.hp = 100
        print(f"{self.imie} leczy się o {self.fotosynteza} 
        
k1 = Kwiatek("alepim cepq")
k2 = Kwiatek("tulipan")

 
while k1.czy_zyje() and k2.czy_zyje():

    
        print("Gracz 1 (a = atak, b = leczenie)")
        inp = input()

    if inp == "a":
        dmg = k1.atak()
        k2.take_dps(dmg)
        print(f"{k1.imie} zadaje {dmg} obrażeń!")

    elif inp == "b":
        k1.heal()
    
    if not k2.czy_zyje():
        break
        

    print("Gracz 2 (a = atak, b = leczenie)")
    inp = input()

    if inp == "a":
        dmg = k2.atak()
        k1.take_dps(dmg)
        print(f"{k1.imie} zadaje {dmg} obrażeń!")

    elif inp == "b":
        k2.heal
    
print("Koniec gry")

if k1.czy_zyje():
    print("Gracz 1 wygrywa")
else k2.czy_zyje():
    print("Gracz 2 wygrywa")

k1.inf()
k2.inf()

    
        
        
        