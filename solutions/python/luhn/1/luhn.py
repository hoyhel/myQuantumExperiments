import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove spaces, check length > 1
        card_num_no_space = self.card_num.replace(" ", "")
        if len(card_num_no_space) <= 1:
            return False
        elif re.search(r'[^0-9]', card_num_no_space):
            return False

        digits = [int(d) for d in card_num_no_space]
        digits.reverse() # Process from right to left

        for i in range(1, len(digits), 2): # double every second digit from the right
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        total_sum = sum(digits)
        return total_sum % 10 == 0
