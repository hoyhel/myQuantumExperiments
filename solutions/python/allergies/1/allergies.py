class Allergies:
    def __init__(self, score):
        self.score = score % 256  # Ignore values >= 256
        self.allergens = [
            ("eggs", 1),
            ("peanuts", 2),
            ("shellfish", 4),
            ("strawberries", 8),
            ("tomatoes", 16),
            ("chocolate", 32),
            ("pollen", 64),
            ("cats", 128)
        ]

    def allergic_to(self, item):
        for name, value in self.allergens:
            if name == item:
                return self.score & value != 0
        return False

    @property
    def lst(self):
        return [name for name, value in self.allergens if self.score & value != 0]