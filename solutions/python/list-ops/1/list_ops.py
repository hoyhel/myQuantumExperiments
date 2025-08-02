from functools import reduce

def append(list1, list2):
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result += [item]
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    result = []
    for item in list:
        result += [function(item)]
    return result


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reversed(list):
        result = function(result, item)
    return result


def reverse(list):
    result = []
    for item in list:
        result = [item] + result
    return result
