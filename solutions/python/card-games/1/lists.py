"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    second_round = number + 1
    third_round = second_round + 1

    return [number, second_round, third_round]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return bool(number in rounds)

average_of_card = 0

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    # Add all the numbers in the list.
    total = 0
    for item in hand:
        total += item
    
    # Check the number of items in the list.
    # Divide the total above with the number of items.
    list_length = len(hand)

    average_of_card = total / list_length
    return average_of_card


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    true_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_index = len(hand) // 2
    middle_value = hand[middle_index]

    return first_last_average == true_average or middle_value == true_average
        
    

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_cards = hand[::2]
    odd_cards = hand[1::2]

    avg_even = sum(even_cards) / len(even_cards) if even_cards else 0
    avg_odd = sum(odd_cards) / len(odd_cards) if odd_cards else 0

    return avg_even == avg_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        third_card = 22
        hand[-1] = 22

    return hand
