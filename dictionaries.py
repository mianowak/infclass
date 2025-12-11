
bohaterowie = {
    "Rycerz Herbowy": {
        "name": "Zbyszko Obłędny",
        "hp": 30,
        "attack": 11,
        "defence": 12,
        "description": "Wspaniały rycerz",
        "wallet": 10
    },
    "Elfi łucznik": {
        "name": "Leonidas Bystry",
        "hp": 24,
        "attack": 16,
        "defence": 8,
        "description": "Szybkostrzelny łucznik",
        "wallet": 14
    },
    "Krasnoludzki młociarz": {
        "name": "Gimli Przysadzisty",
        "hp": 32,
        "attack": 10,
        "defence": 15,
        "description": "Włada młotem",
        "wallet": 8
    }
}

wrogowie = {
    "Wilki": {
        "name": "Mordercza wataha",
        "hp": 21,
        "attack": 7,
        "defence": 8,
        "description": "Obmierzła gadzina"
    },
    "Goblin": {
        "name": "Parszywiec Bagienny",
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
    "Trol": {
        "name": "Plugawiec Plamisty",
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
        "name": "Magnus Krwiopijca",
        "hp": 17,
        "attack": 7,
        "defence": 6,
        "description": "Wielce niebezpieczna istota"
    },
    "Driada": {
        "name": "Daria Rudowłosa",
        "hp": 16,
        "attack": 6,
        "defence": 5,
        "description": "Piękna i niebezpieczna"
    }
}

mapa = [
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej polanie", "zabudowa": None, "postac": "Wilki" },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na skraj lasu", "zabudowa": None, "postac": "Goblin" },
    { "pole": "na drodze do Dravorn", "zabudowa": None, "postac": None },
    { "pole": "na drodze do Dravorn", "zabudowa": "Karczma", "postac": None },
    { "pole": "na drodze do Dravorn", "zabudowa": "Sklep", "postac": None },
    { "pole": "u wejcia do Dravorn", "zabudowa": "Brama", "postac": None },
    { "pole": "w mieście Dravorn", "zabudowa": "Sklep", "postac": None },
    { "pole": "w mieście Dravorn", "zabudowa": "Karczma", "postac": None },
    { "pole": "wyjcie z Dravorn", "zabudowa": "Brama", "postac": None },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": None, "postac": None },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": None, "postac": None },
    { "pole": "na drodze do wsi Lirwoda", "zabudowa": "Stara zniszczona stodoła", "postac": "Nietoperze" },
    { "pole": "we wsi Lirwoda", "zabudowa": "Chłopska chata", "postac": None },
    { "pole": "we wsi Lirwoda", "zabudowa": "Zniszczona chłopska chata", "postac": "Wampir" },
    { "pole": "na drodze do lasu", "zabudowa": None, "postac": None },
    { "pole": "w gęstym lesie", "zabudowa": None, "postac": "Driada" },
    { "pole": "na leśnej ścieżce", "zabudowa": None, "postac": None },
    { "pole": "na leśnej polanie", "zabudowa": "Jaskinia", "postać": "Trol" },
]