import math
PI = math.pi
# pole plaskie
def p_kwadrat(a:float) -> float:
	feturn a**2

def p_prostokat(a:float,b:float)-> float:
	return a*b

def p_rownolegloboku(a:float,h:float)-> float:
	return a*h

def p_trojkata(a:float,h:float)->float:
	return a*h/2

def p_kolo(r:float)->float:
 	return PI*r**2
# pole calkowite bryl
def pc_szescianu(a:float )->float:
	return 6*a**2

def pc_prostopadloscian(a:float,b:float,c:float)->float:
	return 2*a*b+2*b*c+2*a*c

def pc_graniastoslup(Pp:float,Pb:float)->float:
	return 2*Pp+Pb

def pc_ostroslup(Pp:float,Pb:float)->float:
	return Pp+Pb

def pc_kula(r:float)->float:
	return 4*PI*r**2 

def pc_stozek(r:float,l:float)->float:
	return PI*r**2 + PI*r*l

def pc_walec(r:float,H:float)->float:
	return 2*PI*r**2 + 2*PI*r*H
	
	
	
