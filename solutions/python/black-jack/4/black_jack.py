"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    'J', 'Q', 'K' = 10
    'A' = 1
    '2'-'10' = int value
    """
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    # For cards '2' to '10'
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    # If values are equal, return both cards as a tuple.
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11
            
        return int(card)

    # If there's already an Ace, return 1
    if card_one == 'A' or card_two == 'A':
        return 1

    total = card_value(card_one) + card_value(card_two)

    # If counting ace as 11 keeps total <= 21, use 11; otherwise, use 1
    if total + 11 <= 21:
        return 11

    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    # A blackjack consists of one Ace and one card with a value of 10.
    # We check for the two possible combinations: (Ace, 10-card) or (10-card, Ace).
    
    # Check if the first card is an Ace and the second has a value of 10.
    is_ace_then_ten = (card_one == 'A' and value_of_card(card_two) == 10)
    
    # Check if the first card has a value of 10 and the second is an Ace.
    is_ten_then_ace = (value_of_card(card_one) == 10 and card_two == 'A')
    
    # The hand is a blackjack if either of the two cases is true.
    return is_ace_then_ten or is_ten_then_ace


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    # A hand can be split if the two cards have the same scoring value.
    # We use the value_of_card() helper function to get the value of each card.
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    # A hand can be doubled down if the sum of the card values is 9, 10, or 11.
    hand_total = value_of_card(card_one) + value_of_card(card_two)
    
    # Check if the total is in the valid set for doubling down.
    return hand_total in [9, 10, 11]
