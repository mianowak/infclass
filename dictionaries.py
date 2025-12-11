
bohaterowie = {
    "Fairy": {
        "name": "Wrozka",
        "hp": 32,
        "attack": 11,
        "defence": 12,
        "description": "Wspaniały rycerz",
        "wallet": 10
    },
    "Elf": {
        "name": "Elf",
        "hp": 32,
        "attack": 16,
        "defence": 8,
        "description": "Szybkostrzelny łucznik",
        "wallet": 14
    },
    "Sorceres": {
        "name": "Czarodziejka",
        "hp": 32,
        "attack": 10,
        "defence": 15,
        "description": "Włada rozdzka",
        "wallet": 8
    },
    "Knight": {
         "name": "Rycerz",
        "hp": 32,
        "attack": 10,
        "defence": 15,
        "description": "Włada mieczem i tarcza",
        "wallet": 8
    },
        
    "Aladdin": {
        "name": "Aladyn",
        "hp": 32,
        "attack": 10,
        "defence": 15,
        "description": "Lata na dywanie",
        "wallet": 8
    },
    "Prince": {
        "name": "Książę",
        "hp": 32,
        "attack": 10,
        "defence": 15,
        "description": "Włada nozami",
        "wallet": 8
        
        
        
        
}

wrogowie = {
    "Goblin": {
        "name": "Goblin",
        "hp": 21,
        "attack": 7,
        "defence": 8,
        "description": "Obmierzła gadzina"
    },
    "Wolf": {
        "name": "Wilk",
        "hp": 19,
        "attack": 6,
        "defence": 6,
        "description": "Obmierzła gadzina"
    },
    "Orc": {
        "name": "Obrzydliwiec Mulisty",
        "hp": 20,
        "attack": 7,
        "defence": 8,
        "description": "Silna bestyja"
    },
    "Troll": {
        "name": "Zielony trol",
        "hp": 21,
        "attack": 9,
        "defence": 10,
        "description": "Wielgachna bestja"
    },
    "Nietoperz": {
        "name": "Krwiossak",
        "hp": 6,
        "attack": 1,
        "defence": 1,
        "description": "Paskudny gryzoń"
    },
    "Wampir": {
        "name": "Krwiopijca",
        "hp": 17,
        "attack": 7,
        "defence": 6,
        "description": "Wielce niebezpieczna istota"
    },
    "Dragon": {
        "name": "Złoty smok",
        "hp": 16,
        "attack": 6,
        "defence": 5,
        "description": "Piękny i niebezpieczny"
    }
}

mapa = [
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej polanie", "zabudowa": "Most", "postac": "Goblin" },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na skraj lasu", "zabudowa": "opuszczona dzungla", "postac": "Wolf" },
    { "pole": "na drodze do Dravorn", "zabudowa": None, "postac": None },
    { "pole": "na drodze do Dravorn", "zabudowa": "Karczma", "postac": None },
    { "pole": "na drodze do Dravorn", "zabudowa": None, "postac": None },
    { "pole": "u wejcia do Dravorn", "zabudowa": "Brama", "postac": None },
    { "pole": "w mieście Dravorn", "zabudowa": "tajemniczy las", "postac": "Orc },
    { "pole": "w mieście Dravorn", "zabudowa": "Karczma", "postac": None },
    { "pole": "wyjcie z Dravorn", "zabudowa": "Brama", "postac": Troll },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": None, "postac": None },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": None, "postac": None },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": "Stara zniszczona stodoła", "postac": "Nietoperze" },
    { "pole": "we wsi Lirwoda", "zabudowa": "Chłopska chata", "postac": None },
    { "pole": "we wsi Lirwoda", "zabudowa": "Zniszczona chłopska chata", "postac": "Wampir" },
    { "pole": "na drodze do lasu", "zabudowa": None, "postac": None },
    { "pole": "w gęstym lesie", "zabudowa": None, "postac": None },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej ścieżce", "zabudowa": "zniszczony krolewski zamek", "postac": "Dragon"},
]
