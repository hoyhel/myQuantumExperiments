import re

class PhoneNumber:
    def __init__(self, number):
        # Check for letters
        if re.search(r'[A-Za-z]', number):
            raise ValueError("letters not permitted")
        
        # Check for forbidden punctuations (anything that's not digit, space, +, -, ., (), etc.)
        if re.search(r'[^0-9\s\+\-\.\(\)]', number):
            raise ValueError("punctuations not permitted")
        
        # Extract digits only
        digits = re.findall(r'\d', number)
        digits_str = ''.join(digits)

        # Validate length
        if len(digits_str) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits_str) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits_str) == 11:
            if digits_str[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits_str = digits_str[1:]  # remove country code

        # Now we have exactly 10 digits
        area_code = digits_str[0]
        exchange_code = digits_str[3]

        if area_code == '0':
            raise ValueError("area code cannot start with zero")
        if area_code == '1':
            raise ValueError("area code cannot start with one")
        if exchange_code == '0':
            raise ValueError("exchange code cannot start with zero")
        if exchange_code == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = digits_str
        self.area_code = digits_str[0:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
