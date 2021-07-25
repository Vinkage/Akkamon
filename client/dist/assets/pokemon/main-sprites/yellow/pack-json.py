import json
from pathlib import Path

class PackEntry:
    def __init__(self, pathstring, key):
        self.url = pathstring
        self.key = key

    def __str__(self):
        return "entry={url: " + self.url + ", key: " + self.key + "}"

class Packer:

    def __init__(self, name, path, defaultType):
        self.json = { }
        self.name = name
        self.json[name] = {
                "files": [],
                "path": path,
                "defaultType": defaultType
                }

    def addEntry(self, entry):
        self.json[self.name]['files'].append(entry)

    def saveToJson(self):
        with open(f"./{self.name}.json", "w") as f:
            json.dump(self.json, f)

numberToPokemonName = {
        1: 'bulbasaur',
        2: 'ivysaur',
        3: 'venusaur',
        4: 'charmander',
        5: 'charmeleon',
        6: 'charizard',
        7: 'squirtle',
        8: 'wartortle',
        9: 'blastoise',
        10: 'caterpie',
        11: 'metapod',
        12: 'butterfree',
        13: 'weedle',
        14: 'kakuna',
        15: 'beedrill',
        16: 'pidgey',
        17: 'pidgeotto',
        18: 'pidgeot',
        19: 'rattata',
        20: 'raticate',
        21: 'spearow',
        22: 'fearow',
        23: 'ekans',
        24: 'arbok',
        25: 'pikachu',
        26: 'raichu',
        27: 'sandshrew',
        28: 'sandslash',
        29: 'nidoran♀',
        30: 'nidorina',
        31: 'nidoqueen',
        32: 'nidoran♂',
        33: 'nidorino',
        34: 'nidoking',
        35: 'clefairy',
        36: 'clefable',
        37: 'vulpix',
        38: 'ninetales',
        39: 'jigglypuff',
        40: 'wigglytuff',
        41: 'zubat',
        42: 'golbat',
        43: 'oddish',
        44: 'gloom',
        45: 'vileplume',
        46: 'paras',
        47: 'parasect',
        48: 'venonat',
        49: 'venomoth',
        50: 'diglett',
        51: 'dugtrio',
        52: 'meowth',
        53: 'persian',
        54: 'psyduck',
        55: 'golduck',
        56: 'mankey',
        57: 'primeape',
        58: 'growlithe',
        59: 'arcanine',
        60: 'poliwag',
        61: 'poliwhirl',
        62: 'poliwrath',
        63: 'abra',
        64: 'kadabra',
        65: 'alakazam',
        66: 'machop',
        67: 'machoke',
        68: 'machamp',
        69: 'bellsprout',
        70: 'weepinbell',
        71: 'victreebel',
        72: 'tentacool',
        73: 'tentacruel',
        74: 'geodude',
        75: 'graveler',
        76: 'golem',
        77: 'ponyta',
        78: 'rapidash',
        79: 'slowpoke',
        80: 'slowbro',
        81: 'magnemite',
        82: 'magneton',
        83: 'farfetch’d',
        84: 'doduo',
        85: 'dodrio',
        86: 'seel',
        87: 'dewgong',
        88: 'grimer',
        89: 'muk',
        90: 'shellder',
        91: 'cloyster',
        92: 'gastly',
        93: 'haunter',
        94: 'gengar',
        95: 'onix',
        96: 'drowzee',
        97: 'hypno',
        98: 'krabby',
        99: 'kingler',
        100: 'voltorb',
        101: 'electrode',
        102: 'exeggcute',
        103: 'exeggutor',
        104: 'cubone',
        105: 'marowak',
        106: 'hitmonlee',
        107: 'hitmonchan',
        108: 'lickitung',
        109: 'koffing',
        110: 'weezing',
        111: 'rhyhorn',
        112: 'rhydon',
        113: 'chansey',
        114: 'tangela',
        115: 'kangaskhan',
        116: 'horsea',
        117: 'seadra',
        118: 'goldeen',
        119: 'seaking',
        120: 'staryu',
        121: 'starmie',
        122: 'mr. mime',
        123: 'scyther',
        124: 'jynx',
        125: 'electabuzz',
        126: 'magmar',
        127: 'pinsir',
        128: 'tauros',
        129: 'magikarp',
        130: 'gyarados',
        131: 'lapras',
        132: 'ditto',
        133: 'eevee',
        134: 'vaporeon',
        135: 'jolteon',
        136: 'flareon',
        137: 'porygon',
        138: 'omanyte',
        139: 'omastar',
        140: 'kabuto',
        141: 'kabutops',
        142: 'aerodactyl',
        143: 'snorlax',
        144: 'articuno',
        145: 'zapdos',
        146: 'moltres',
        147: 'dratini',
        148: 'dragonair',
        149: 'dragonite',
        150: 'mewtwo',
        151: 'mew'
        }

frontPath = Path('.')
frontPacker = Packer("pokemon-yellow-front",
        "assets/pokemon/main-sprites/yellow/",
        "image")

backPath = Path('./back')
backPacker = Packer("pokemon-yellow-back",
        "assets/pokemon/main-sprites/yellow/back",
        "image")


for f in frontPath.glob("*.png"):
    entry = PackEntry(f.name, numberToPokemonName[int(f.stem)] + "-front")
    frontPacker.addEntry(entry.__dict__)

frontPacker.saveToJson()

for f in backPath.glob("*.png"):
    entry = PackEntry(f.name, numberToPokemonName[int(f.stem)] + "-back")
    backPacker.addEntry(entry.__dict__)

backPacker.saveToJson()
