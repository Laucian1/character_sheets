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

class CharacterRace:
    def __init__(self, race):
        self.name = race
        self.ability_score_modifiers = {}
        self.size = "Medium"
        self.type = "Humanoid"
        self.subtype = ""
        self.speed = 30
        self.languages = ["Common"]
        self.senses = {}
        self.racial_abilities = []
        self.skill_bonuses = []
        self.race_points = 0

    def apply_racial_traits(self, character):
        for ability, modifier in self.ability_score_modifiers.items():
            character.ability_scores[ability] += modifier

        character.size = self.size
        character.speed = self.speed

        character.languages.extend(self.languages)
        character.senses.update(self.senses)
        character.racial_abilities.extend(self.racial_abilities)

    # Automate Languages?

class Dwarf(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.DWARF.value
        self.ability_score_modifiers = {
            "Constitution" : 2,
            "Wisdom" : 2,
            "Charisma" : -2
        }
        self.subtype = "(dwarf)"
        self.speed = 20
        self.languages.append("Dwarven")
        self.senses = {"Darkvision": "Dwarves can see perfectly in the dark up to 60 feet."}
        self.racial_abilities = [
            {"Defensive Training": "Dwarves gain a +4 dodge bonus to AC against monsters of the giant subtype."}, 
            {"Hardy": "Dwarves gain a +2 racial bonus on saving throws against poison, spells, and spell-like abilities."}, 
            {"Stability": "Dwarves gain a +4 racial bonus to their Combat Maneuver Defense when resisting a bull rush or trip attempt while standing on the ground."}, 
            {"Hatred": "Dwarves gain a +1 racial bonus on attack rolls against humanoid creatures of the orc and goblinoid subtypes because of their special training against these hated foes."},
            {"Weapon Familiarity": "Dwarves are proficient with battleaxes, heavy picks, and warhammers, and treat any weapon with the word “dwarven” in its name as a martial weapon."},
        ]
        self.skill_bonuses = [
            {"Greed": "Dwarves gain a +2 racial bonus on Appraise checks made to determine the price of non-magical goods that contain precious metals or gemstones"},
            {"Stonecunning": "Dwarves gain a +2 bonus on Perception checks to notice unusual stonework, such as traps and hidden doors located in stone walls or floors. They receive a check to notice such features whenever they pass within 10 feet of them, whether or not they are actively looking."},
        ]
        self.race_points = 11

class Elf(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.ELF.value
        self.ability_score_modifiers = {
            "Dexterity" : 2,
            "Constitution" : -2,
            "Intelligence" : 2
        }
        self.subtype = "(elf)"
        self.languages.append("Elven")
        self.senses = {"Low-Light Vision": "Elves can see twice as far as humans in conditions of dim light."}
        self.racial_abilities = [
            {"Elven Immunities": "Elves are immune to magic sleep effects and gain a +2 racial saving throw bonus against enchantment spells and effects."}, 
            {"Weapon Familiarity": "Elves are proficient with longbows (including composite longbows), longswords, rapiers, and shortbows (including composite shortbows), and treat any weapon with the word “elven” in its name as a martial weapon."},
            {"Elven Magic": "Elves receive a +2 racial bonus on caster level checks made to overcome spell resistance. In addition, elves receive a +2 racial bonus on Spellcraft skill checks made to identify the properties of magic items."}
        ]
        self.skill_bonuses = [
            {"Keen Senses": "Elves receive a +2 racial bonus on Perception checks"}
        ]
        self.race_points = 10

class Human(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.HUMAN.value
        self.ability_score_modifiers = {
            "Strength" : 0,
            "Dexterity" : 0,
            "Constitution" : 0,
            "Intelligence" : 0,
            "Wisdom" : 0,
            "Charisma" : 0
        } # Add ability to choose +2 to one ability score
        self.subtype = "(Human)"
        self.racial_abilities = [
            {"Bonus Feat": "Humans select one extra feat at 1st level."}, 
            {"Skilled": "Humans gain an additional skill rank at first level and one additional rank whenever they gain a level."}
        ]
        self.race_points = 9

    def set_ability_score_bonus(self, ability):
        if ability in self.ability_score_modifiers:
            self.ability_score_modifiers[ability] += 2
        else:
            raise ValueError(f"Invalid ability score: {ability}")