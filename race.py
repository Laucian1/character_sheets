from enum import Enum

class CoreRace(Enum):
    DWARF = "Dwarf"
    ELF = "Elf"
    GNOME = "Gnome"
    HALF_ELF = "Half Elf"
    HALF_ORC = "Half Orc"
    HALFLING = "Halfling"
    HUMAN = "Human"

class StandardRace(Enum):
    CATFOLK = "Catfolk"
    DUERGAR = "Duergar"
    GNOLL = "Gnoll"
    GRIPPLI = "Grippli"
    GOBLIN = "Goblin"
    HOBGOBLIN = "Hobgoblin"
    IFRIT = "Ifrit"
    KOBOLD = "Kobold"
    LIZARDFOLK = "Lizardfolk"
    MONKEY_GOBLIN = "Monkey Goblin"
    ORC = "Orc" 
    OREAD = "Oread"
    RATFOLK = "Ratfolk"
    SKINWALKER = "Skinwalker"
    SYLPH = "Sylph"
    TRIAXIAN = "Triaxian"
    UNDINE = "Undine"
    VANARA = "Vanara"

class AdvancedRace(Enum):
    AASIMAR = "Aasimar"
    ANDROID = "Android"
    DHAMPIR = "Dhampir"
    DROW_COMMON = "Drow (Common)"
    FETCHLING = "Fetchling"
    GATHLAIN = "Gathlain"
    GHORAN = "Ghoran"
    KASAATHA = "Kasatha"
    LASHUNTA = "Lashunta"
    SHABTI = "Shabti"
    SYRINX = "Syrinx"
    SULI = "Suli"
    TENGU = "Tengu"
    TIEFLING = "Tiefling"
    VISHKANYA = "Vishkanya"
    WYRWOOD = "Wyrwood"
    WYVARAN = "Wyvaran"

class MontrousRace(Enum):
    SVIRFNEBLIN = "Svirfneblin"

class VeryPowerfulRace(Enum):
    DROW_NOBLE = "Drow (Noble)"
    DRIDER = "Drider"
    GARGOYLE = "Gargoyle"
    TROX = "Trox"

class UnknownRace(Enum):
    AQUATIC_ELF = "Aquatic Elf"
    ASTOMOI = "Astomoi"
    CALIGNI = "Caligni"
    CHANGELING = "Changeling"
    DEEP_ONE_HYBRID = "Deep One Hybrid"
    GANZI = "Ganzi"
    GILLMEN = "Gillmen"
    KITSUNE = "Kitsune"
    KURU = "Kuru"
    MERFOLK = "Merfolk"
    MUNAVRI = "Munavri"
    NAGAJI = "Nagaji"
    ORANG_PENDAK = "Orang-Pendak"
    REPTOID = "Reptoid"
    SAMSARAN = "Samsaran"
    STRIX = "Strix"
    WAYANG = "Wayang"

class PlayerRace:
    def __init__(self, race):
        self.race = race
        self.ability_bonus = 0
        self.ability_penalty = 0
        self.size = "Medium"
        self.type = "Humanoid"
        self.subtype = ""
        self.speed = 30
        self.s_lang = "Common"
        self.senses = ""
        self.def_traits = ""
        self.off_traits = ""
        self.skill_bonuses = ""
        self.sp_su_abilities = ""
        self.race_points = 11