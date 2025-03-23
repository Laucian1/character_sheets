from enum import Enum

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