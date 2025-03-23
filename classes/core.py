from enum import Enum
from .template import CharacterClass

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

class Fighter(CharacterClass):
    def __init__(self):
        super().__init__()
        self.name = CoreClass.FIGHTER.value
        self.hit_die = 10
        self.skill_ranks_per_level = 2
        self.bab_progression = "full"
        self.saves = {
            "fortitude": "good",
            "reflex": "poor",
            "will": "poor"
        }
        self.class_features = {
            1: ["Bonus Feat", "Bravery +1"],
            2: ["Bonus Feat", "Bravery +2"],
            # Continue with fighter progression...
        }

    def apply_class_features(self, character, level):
        super().apply_class_features(character, level)
        bravery_value = 1 + (level - 1) // 4
        character.add_special_ability(f"Bravery +{bravery_value}")

class Wizard(CharacterClass):
    def __init__(self):
        super().__init__()
        self.name = CoreClass.WIZARD.value
        self.hit_die = 6
        self.skill_ranks_per_level = 2
        self.bab_progression = "poor"
        self.saves = {
            "fortitude": "poor",
            "reflex": "poor",
            "will": "good"
        }
        self.spellcasting = {
            "type": "arcane",
            "school": None,
            "spells_per_day": {},
            "spells_known": {}
        }

        self.class_features = {
            1: ["Arcane Bond", "Arcane School", "Cantrips"],
            3: ["Metamagic Feat"],
            # Continue with wizard progression...
        }

    def apply_class_features(self, character, level):
        super().apply_class_features(character, level)
        self.spellcasting["spells_per_day"] = self._calculate_spells_per_day(level)
        character.spellbook.set_spell_progression(self.spellcasting)

