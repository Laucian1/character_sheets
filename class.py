from enum import Enum

class CoreClass(Enum):
    BARBARIAN = 1
    BARD = 2
    CLERIC = 3
    DRUID = 4
    FIGHTER = 5
    MONK = 6
    PALADIN = 7
    RANGER = 8
    ROGUE = 9
    SORCERER = 10
    WIZARD = 11

class BaseClass(Enum):
    ALCHEMIST = 1
    CAVALIER = 2
    GUNSLINGER = 3
    INQUISITOR = 4
    MAGUS = 5
    OMDURA = 6
    ORACLE = 7
    SHIFTER = 8
    SUMMONER = 9
    WITCH = 10
    VAMPIRE_HUNTER = 11
    VIGILANTE = 12

class HybridClass(Enum):
    ARCANIST = 1 # SORCERER, WIZARD
    BLOODRAGER = 2 # BARBARIAN, SORCERER
    BRAWLER = 3 # FIGHTER, MONK
    HUNTER = 4 # DRUID, RANGER
    INVESTIGATOR = 5 # ALCHEMIST, ROGUE
    SHAMAN = 6 # ORACLE, WITCH
    SKALD = 7 # BARBARIAN, BARD
    SLAYER = 8 # RANGER, ROGUE
    SWASHBUCKLER = 9 # FIGHTER, GUNSLINGER
    WARPRIEST = 10 # FIGHTER, CLERIC

class UnchainedClass(Enum):
    BARBARIAN = 1
    MONK = 2
    ROGUE = 3
    SUMMONER = 4

class OccultClass(Enum):
    KINETICIST = 1
    MEDIUM = 2
    MESMERIST = 3
    OCCULTIST = 4
    PSYCHIC = 5
    SPIRITUALIST = 6

class AlternateClass(Enum):
    ANTIPALADIN = 1
    NINJA = 2
    SAMURAI = 3

class NPCClass(Enum):
    ADEPT = 1
    ARISTOCRAT = 2
    COMMONER = 3
    EXPERT = 4
    WARRIOR = 5

