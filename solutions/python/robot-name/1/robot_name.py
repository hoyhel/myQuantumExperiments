import random
import string

class Robot:
    def __init__(self):
        self.name = self.create_name()

    def create_name(self):
        first_letter = random.choice(string.ascii_uppercase)
        second_letter = random.choice(string.ascii_uppercase)
        first_digit = random.randint(0, 9)
        second_digit = random.randint(0, 9)
        third_digit = random.randint(0, 9)
        robot_name = first_letter + second_letter + str(first_digit) + str(second_digit) + str(third_digit)
        return robot_name

    def reset(self):
        random.randint(1, 10) # Advance RNG state
        self.name = self.create_name()
    