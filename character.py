from classes import *
from races import *

class Character:
    def __init__(self, name, race, char_class, level):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = level
        self.ability_scores = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        self.hit_points = 0
        self.armor_class = 10
        self.skills = {}
        self.feats = []
        self.equipment = []
        self.spells = []

    def set_ability_score(self, ability, value):
        if ability in self.ability_scores:
            self.ability_scores[ability] = value
        else:
            raise ValueError(f"Invalid ability score: {ability}")
        
    def calculate_modifier(self, ability):
        score = self.ability_scores[ability]
        return (score - 10)//2
    
    def add_skill(self, skill, ranks):
        self.skills[skill] = ranks

    def add_feat(self, feat):
        self.feats.append(feat)

    def add_equipment(self, item):
        self.equipment.append(item)

    def add_spell(self, spell):
        self.spells.append(spell)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Race: {self.race}\n"
                f"Class: {self.char_class}\n"
                f"Level: {self.level}\n"
                f"Ability Scores: {self.ability_scores}\n"
                f"HP: {self.hit_points}\n"
                f"AC: {self.armor_class}\n"
                f"Skills: {self.skills}\n"
                f"Feats: {self.feats}\n"
                f"Equipment: {self.equipment}\n"
                f"Spells: {self.spells}\n")
    
    def create_character():
        name = input("Enter character name: ")
        race = input("Enter race: ")
        char_class = input("Enter class: ")
        level = int(input("Enter level: "))
        character = Character(name, race, char_class, level)

        for ability in character.ability_scores:
            score = int(input(f"Enter {ability} score: "))
            character.set_ability_score(ability, score)

        # Add more input for skills, feats, equipment, etc.

        return character
    
    def print_character_sheet(character):
        print(character)