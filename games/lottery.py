from numpy import random


def generate_ticket():
    """this function generates a lottery ticket with 8 numbers"""
    values = random.randint(1, 100, 8)
    return list(values)
