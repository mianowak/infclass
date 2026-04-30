class Samochod:
    def __init__(self,imie,rok_powstania):
        self.imie = imie
        self.dt_powstania = rok_powstania
        
class Przedniekola:
    def __init__(self):
        pass

class Tylniekola:
    def __init__(self):
        pass
        
class Maska:
    def __init__(self):
        pass
        
class Bagaznik:
    def __init__(self):
        pass
        

class BMW(Samochód):
    def __init__(self, imie,rok_powstania):
        super().__init__(imie, rok_powstania)
        self.przedniekola = Przedniekola()
        self.tylniekola = Tylniekola()
        self.maska = Maska()
        self.bagażnik = Bagaznik()
    
kasia = BMW("kasia",2010)

    
    
    
    
