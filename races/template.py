class CharacterRace:
    def __init__(self, race):
        self.name = race
        self.ability_score_modifiers = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        self.size = "Medium"
        self.type = "Humanoid"
        self.subtype = []
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
        character.skill_bonuses.extend(self.skill_bonuses)
    
    def set_ability_score_bonus(self, ability):
        if "human" in self.subtype:
            if ability in self.ability_score_modifiers:
                self.ability_score_modifiers[ability] += 2
            else:
                raise ValueError(f"Invalid ability score: {ability}")
        else:
            raise ValueError(f"{self.name} does not have a flexible ability score bonus.")

    # Automate Bonus Languages?

