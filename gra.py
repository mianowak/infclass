import random
# tworzymy postac 
postac = {
    "imie": "Bohater",
    "hp": 100,
    "atak": 25,
    "sila": 30,
    "leczenie": 20,
    "obrona": 10
}

#lista owocow ktore dodaja wartosci do sily i hp
owoce = {
    "jablko": {"sila": 5 , "hp": 5},
    "banan": {"sila": 7 , "hp": 7},
    "malina": {"sila": 6 , "hp":6},
    "czeresnie": {"sila": 2, "hp": 2}
}
#losujemy owoc ktory znajdzie postac
znaleziony_owoc = random.choice(owoce)
#dodawanie wartosci owocu do postaci
postac["sila"] += owoce[znaleziony_owoc]["sila"]
postac["hp"] += owoce[znaleziony_owoc]["hp"]
print(f"postac znalazla {znaleziony_owoc} i zwiekszyla swoja sile o {owoce[znaleziony_owoc]['sila']} oraz hp o {owoce[znaleziony_owoc]['hp']}")

# tworzymy goblina
goblin = {
    "imie": "goblin",
    "hp": 80,
    "sila": 15,
    "atak": "20",
    "leczenie": "15",
    "obrona": "5"
}
# walka
while postac["hp"] > 0 and goblin["hp"] > 0:
    #atak postaci
    akcja_postaci = input("wybierz akcje postaci: atak lub leczenie lub obrona:")
    if akcja_postaci == "atak":
        obrazenia = postac["atak"] - goblin["obrona"]
        goblin["hp"] -= obrazenia
        print(f"{postac["imie"]} zadaje {obrazenia} obrazen goblinowi. jego hp to {goblin["hp"]}")
    elif akcja_postaci == "leczenie":
        postac["hp"] += postac["leczenie"]
        print(f"{postac["imie"]} leczy sie o {postac["leczenie"]} punktow. jego hp to {postac["hp"]}")
    elif akcja_postaci == "obrona":
        postac["obrona"] += 5
        print(f"{postac["imie"] } zwieksza swoja obrone o 5. jego obrona to {postac["obrona"]}")
        if goblin["hp"] <= 0:
            print("postac wygrywa!")
    #atak goblina
    akcja_goblina = input("wybierz akcje goblina: atak lub leczenie lub obrona:")
    if akcja_goblina == "atak":
        obrazenia = goblin["atak"] - postac["obrona"]
        postac["hp"] -= obrazenia
        print(f"{goblin["imie"]} zadaje {obrazenia} obrazenia postaci. jego hp to {postac["hp"]}")
    elif akcja_goblina == "leczenie":
        goblin["hp"] += goblin["leczenie"]
        print(f"{goblin["imie"]} leczy sie o {goblin["leczenie"]} punktow. jego hp to {goblin["hp"]}")
    elif akcja_goblina == "obrona":
        goblin["obrona"] += 3
        print(f"{goblin["imie"]} zwieksza swoja obrone o 5. jego obrona to {goblin["obrona"]}")
        if postac["hp"] <= 0:
            print("goblin wygrywa!")