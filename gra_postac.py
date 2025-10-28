import random
# zapytaj sie jak gracz chce zeby nazywala sie jego postac
imie = input("podaj imie swojej postaci: ")

# dalsze tworzenie postaci 
postac = {
    "imie_postaci": imie,
    "hp_postaci": 100,
    "atak_postaci": 25,
    "sila_postaci": 30,
    "leczenie_postaci": 20,
    "obrona_postaci": 10,
    "pozycja_postaci": 0
}

print(imie, "rozpoczyna gre")

goblin = {
    "imie_goblina": "goblin",
    "hp_goblina": 60,
    "sila_goblina": 15,
    "atak_goblina": 20,
    "leczenie_goblina": 15,
    "obrona_goblina": 5,
    "pozycja_goblina": 10
}

#dobre owoce
dobre_owoce = ["banan","malina","mango","czeresnia","winogrono"]

# zle owoce
zle_owoce = ["greifrut", "cytryna","czarna porzeczka","sliwka","pomarancza"]

wartosc_dobrego_owocu = {
    "banan": 7,
    "malina": 5,
    "mango": 6,
    "czeresnia": 8,
    "winogrono": 4
}

wartosc_zlego_owocu = {
    "greifrut": -6,
    "cytryna": -3,
    "czarna porzeczka": -4,
    "sliwka": -7,
    "pomarancza": -2
}

while int(postac['hp_postaci']) > 0 and int(goblin['hp_goblina']) > 0:
    postac['pozycja_postaci'] += 1
    print("zmieniasz pozycje")

    # losujemy co przytrawi sie postaci
    wydarzenia = random.choice(["dobry owoc", "zly owoc", "nic"])

    if wydarzenia == "dobry owoc":
        owoc = random.choice(dobre_owoce)
        postac['hp_postaci'] += int(wartosc_dobrego_owocu[owoc])
        postac['sila_postaci'] += int(wartosc_dobrego_owocu[owoc])
        print("twoja postac znalazla " + owoc + " i zyskuje punkty zdrowia i sily.")
    elif wydarzenia == "zly owoc":
        owoc = random.choice(zle_owoce)
        postac["hp_postaci"] += int(wartosc_zlego_owocu[owoc])
        postac["sila_postaci"] += int(wartosc_zlego_owocu[owoc])
        print("twoja postac znalazla " + owoc + " i traci punkty zdrowia i sily.")
    else:
    # nic sie nie wydarzylo, twoja postac idzie dalej
        print("nic sie nie wydarzylo, twoja postac idzie dalej")

    # starcie goblina z postacia
    #atak postaci
    akcja_postaci = input("wybierz akcje postaci: atak lub leczenie lub obrona:")
    if akcja_postaci == "atak":
        obrazenia = postac['atak'] - goblin['obrona']
        goblin["hp"] -= obrazenia
        print(f"{postac['imie']} zadaje {obrazenia} obrazen goblinowi. jego hp to {goblin['hp']}")
    elif akcja_postaci == "leczenie":
        postac["hp"] += postac["leczenie"]
        print(f"{postac['imie']} leczy sie o {postac['leczenie']} punktow. jego hp to {postac['hp']}")
    elif akcja_postaci == "obrona":
        postac["obrona"] += 5
        print(f"{postac['imie']} zwieksza swoja obrone o 5. jego obrona to {postac['obrona']}")
        if goblin["hp"] <= 0:
            print("postac wygrywa!")
    #atak goblina
    akcja_goblina = input("wybierz akcje goblina: atak lub leczenie lub obrona:")
    if akcja_goblina == "atak":
        obrazenia = goblin['atak'] - postac['obrona']
        postac['hp'] -= obrazenia
        print(f"{goblin['imie']} zadaje {obrazenia} obrazenia postaci. jego hp to {postac['hp']}")
    elif akcja_goblina == "leczenie":
        goblin['hp'] += goblin['leczenie']
        print(f"{goblin['imie']} leczy sie o {goblin['leczenie']} punktow. jego hp to {goblin['hp']}")
    elif akcja_goblina == "obrona":
        goblin["obrona"] += 3
        print(f"{goblin['imie']} zwieksza swoja obrone o 5. jego obrona to {goblin['obrona']}")
        if postac["hp"] <= 0:
            print("goblin wygrywa!")




