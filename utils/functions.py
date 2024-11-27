import random


def add_numbers(n1, n2):
    return n1 + n2


def subtract_numbers(n1, n2):
    return n1 - n2


def multiply_numbers(n1, n2):
    return n1 * n2


def divide_numbers(n1, n2):
    return n1 / n2


def calc_operator(operation, n1, n2):
    obj = {
        "+": add_numbers(n1, n2),
        "-": subtract_numbers(n1, n2),
        "/": divide_numbers(n1, n2),
        "*": multiply_numbers(n1, n2),
    }
    return obj[operation]


def generate_number_max_11():
    return random.randint(2, 11)

def getReminderNumber(n1):
    return 21 - sum(n1)
