from enum import Enum

class CoreClass(Enum):
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WIZARD = "Wizard"

class BaseClass(Enum):
    ALCHEMIST = "Alchemist"
    CAVALIER = "Cavalier"
    GUNSLINGER = "Gunslinger"
    INQUISITOR = "Inquisitor"
    MAGUS = "Magus"
    OMDURA = "Omdura"
    ORACLE = "Oracle"
    SHIFTER = "Shifter"
    SUMMONER = "Summoner"
    WITCH = "Witch"
    VAMPIRE_HUNTER = "Vampire Hunter"
    VIGILANTE = "Vigilante"

class HybridClass(Enum):
    ARCANIST = "Arcanist" # SORCERER, WIZARD
    BLOODRAGER = "Bloodrager" # BARBARIAN, SORCERER
    BRAWLER = "Brawler" # FIGHTER, MONK
    HUNTER = "Hunter" # DRUID, RANGER
    INVESTIGATOR = "Investigator" # ALCHEMIST, ROGUE
    SHAMAN = "Shaman" # ORACLE, WITCH
    SKALD = "Skald" # BARBARIAN, BARD
    SLAYER = "Slayer" # RANGER, ROGUE
    SWASHBUCKLER = "Swashbuckler" # FIGHTER, GUNSLINGER
    WARPRIEST = "Warpriest" # FIGHTER, CLERIC

class UnchainedClass(Enum):
    BARBARIAN = "UC Barbarian"
    MONK = "UC Monk"
    ROGUE = "UC Rogue"
    SUMMONER = "UC Summoner"

class OccultClass(Enum):
    KINETICIST = "Kineticist"
    MEDIUM = "Medium"
    MESMERIST = "Mesmerist"
    OCCULTIST = "Occultist"
    PSYCHIC = "Psychic"
    SPIRITUALIST = "Spiritualist"

class AlternateClass(Enum):
    ANTIPALADIN = "Antipaladin"
    NINJA = "Ninja"
    SAMURAI = "Samurai"

class NPCClass(Enum):
    ADEPT = "Adept"
    ARISTOCRAT = "Aristocrat"
    COMMONER = "Commoner"
    EXPERT = "Expert"
    WARRIOR = "Warrior"

