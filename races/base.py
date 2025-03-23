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

