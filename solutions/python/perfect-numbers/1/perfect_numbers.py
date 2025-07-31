import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors = set()
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if i != number:
                divisors.add(i)
                divisors.add(number // i)
                
    # Need to discard the last item in the list
    divisors.discard(number)
    
    if sum(divisors) > number:
        return "abundant"
    elif sum(divisors) == number:
        return "perfect"
    else:
        return "deficient"
    