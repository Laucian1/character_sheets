from enum import Enum
from .base import CharacterRace

class CoreRace(Enum):
    DWARF = "Dwarf"
    ELF = "Elf"
    GNOME = "Gnome"
    HALF_ELF = "Half Elf"
    HALF_ORC = "Half Orc"
    HALFLING = "Halfling"
    HUMAN = "Human"

class Dwarf(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.DWARF.value
        self.ability_score_modifiers = {
            "Constitution" : 2,
            "Wisdom" : 2,
            "Charisma" : -2
        }
        self.subtype = ["dwarf"]
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
        self.subtype = ["elf"]
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

class Gnome(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.GNOME.value 
        self.ability_score_modifiers = {
            "Strength": -2,
            "Constitution": 2,
            "Charisma": 2,
        }
        self.size = "Small"
        self.subtype = ["gnome"]
        self.speed = 20
        self.languages.extend(["Gnome", "Sylvan"])
        self.senses = {"Low Light Vision": "Gnomes can see twice as far as humans in conditions of dim light."}
        self.racial_abilities = [
            {"Defensive Training": "Gnomes gain a +4 dodge bonus to AC against monsters of the giant subtype."},
            {"Illusion Resistance": "Gnomes gain a +2 racial saving throw bonus against illusion spells and effects."},
            {"Gnome Magic": "Gnomes add +1 to the DC of any saving throws against illusion spells that they cast. Gnomes with Charisma scores of 11 or higher also gain the following spell-like abilities: 1/day—dancing lights, ghost sound, prestidigitation, and speak with animals. The caster level for these effects is equal to the gnome’s level. The DC for these spells is equal to 10 + the spell’s level + the gnome’s Charisma modifier."},
            {"Hatred": "Gnomes receive a +1 bonus on attack rolls against humanoid creatures of the reptilian and goblinoid subtypes because of their special training against these hated foes."},
            {"Weapon Familiarity": "Gnomes are proficient with gnome hooked hammers and treat any weapon with the word 'gnome' in its name as a martial weapon."},
        ]
        self.skill_bonuses = [
            {"Keen Senses": "Gnomes receive a +2 racial bonus on Perception checks."},
            {"Obsessive": " Gnomes receive a +2 racial bonus on a Craft or Profession skill of their choice."},
        ]
        self.race_points = 10

class HalfElf(CharacterRace): 
    def __init__(self):
        super().__init__()
        self.name = CoreRace.HALF_ELF.value
        self.subtype = ["human", "elf"]
        self.languages.append("Elven")
        self.senses = {"Low-light vision": "Half-elves can see twice as far as humans in conditions of dim light."}
        self.racial_abilities = [
            {"Elven Immunities": "Half-elves are immune to magic sleep effects and gain a +2 racial saving throw bonus against enchantment spells and effects."},
            {"Adaptability": "Half-elves receive Skill Focus as a bonus feat at 1st level."},
            {"Elf Blood": "Half-elves count as both elves and humans for any effect related to race."},
            {"Multitalented": "Half-elves choose two favored classes at first level and gain +1 hit point or +1 skill point whenever they take a level in either one of those classes"}
        ]
        self.skill_bonuses = [
            {"Keen Senses": "Half-elves receive a +2 racial bonus on Perception checks."}
        ]
        self.race_points = 10
    
class HalfOrc(CharacterRace): 
    def __init__(self):
        super().__init__()
        self.name = CoreRace.HALF_ORC.value
        self.subtype = ["human", "orc"]
        self.languages.append("Orc")
        self.senses = {"Darkvision": "Half-orcs can see in the dark up to 60 feet."}
        self.racial_abilities = [
            {"Orc Ferocity": "Once per day, when a half-orc is brought below 0 hit points but not killed, he can fight on for 1 more round as if disabled. At the end of his next turn, unless brought to above 0 hit points, he immediately falls unconscious and begins dying."},
            {"Weapon Familiarity": "Half-orcs are proficient with greataxes and falchions and treat any weapon with the word “orc” in its name as a martial weapon."},
            {"Orc Blood": "Half-orcs count as both humans and orcs for any effect related to race."}
        ]
        self.skill_bonuses = [
            {"Intimidating": "Half-orcs receive a +2 racial bonus on Intimidate checks due to their fearsome nature."}
        ]
        self.race_points = 8

class Halfling(CharacterRace): 
    def __init__(self):
        super().__init__()
        self.name = CoreRace.HALFLING.value
        self.ability_score_modifiers = {
            "Strength": -2,
            "Dexterity": 2,
            "Charisma": 2
        }
        self.size = "Small"
        self.subtype = ["halfling"]
        self.speed = 20
        self.languages.append("Halfling")
        self.racial_abilities = [
            {"Fearless": "Halflings receive a +2 racial bonus on all saving throws against fear. This bonus stacks with the bonus granted by halfling luck."},
            {"Halfling Luck": "Halflings receive a +1 racial bonus on all saving throws."},
            {"Weapon Familiarity": "Halflings are proficient with slings and treat any weapon with the word “halfling” in its name as a martial weapon."}
        ]
        self.skill_bonuses = [
            {"Sure-Footed": "Halflings receive a +2 racial bonus on Acrobatics and Climb checks."},
            {"Keen Senses": "Halflings receive a +2 racial bonus on Perception checks."}
        ]
        self.race_points = 9

class Human(CharacterRace):
    def __init__(self):
        super().__init__()
        self.name = CoreRace.HUMAN.value
        self.subtype = ["human"]
        self.racial_abilities = [
            {"Bonus Feat": "Humans select one extra feat at 1st level."}, 
            {"Skilled": "Humans gain an additional skill rank at first level and one additional rank whenever they gain a level."}
        ]
        self.race_points = 9

