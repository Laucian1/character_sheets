class CoreClass:
    def __init__(self):
        self.name = "Base Class"
        self.hit_die = 0
        self.skill_ranks_per_level = 0
        self.bab_progression = "poor"
        self.saves = {
            "fortitude": "poor",
            "reflex": "poor",
            "will": "poor"
        }
        self.class_features = {}
        self.spellcasting = None

    def apply_class_features(self, character, level):
        for feature_level in sorted(self.class_features.keys()):
            if feature_level <= level:
                for feature in self.class_features[feature_level]:
                    character.add_class_feature(feature)

    def get_bab(self, level):
        if self.bab_progression == "full":
            return level
        elif self.bab_progression == "medium":
            return level * 3 // 4
        else:
            return level // 2