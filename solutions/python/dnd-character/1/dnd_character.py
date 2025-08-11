import random
import math

class Character:
    def __init__(self):
        # Generate all six abilities
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Calculate hitpoints = 10 + constitution modifier
        self.hitpoints = 10 + ((self.constitution - 10) // 2)

    def ability(self):
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.remove(min(dice)) # Remove the lowest die roll
        return sum(dice)

    def strength(self):
        self.strength = self.ability()
        return self.strength

    def dexterity(self):
        self.dexterity = self.ability()
        return self.dexterity

    def constitution(self):
        self.constitution = self.ability()
        return self.constitution

    def intelligence(self):
        self.intelligence = self.ability()
        return self.intelligence

    def wisdom(self):
        self.wisdom = self.ability()
        return self.wisdom

    def charisma(self):
        self.charisma = self.ability()
        return self.charisma

    def hitpoints(self):
        self.hitpoints = (self.charisma - 10) // 2 + 10
        return self.hitpoints


def modifier(value):
    constitution_modifier = (value - 10) // 2
    return constitution_modifier
