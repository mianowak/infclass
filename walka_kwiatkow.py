from random import randint

class Kwiatek:
    def _init_ (self,imie):
        self.imie = imie
        self.zyje = True
        self.hp = 100
        self.fotosynteza = 
        
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
        
k1 = Kwiatek("alepim cepq")
k2 = Kwiatek("tulipan")

while k1.czy_zyje() and k2.czy_zyje():
    print("gracz1")
    inp = input()
    if inp == "a":
        pass
    elif inp == "b":
        pass
    print("gracz2")
    if inp == "a":
        pass
    elif inp == "b":
        pass
        
print("wygral")

k1.inf()
k2.inf()

    
        
        
        