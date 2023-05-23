from random import randint


def lottery_generator():
    numbers = []
    for number in range(0, 6):
        numbers.append(randint(0, 9))
    return numbers

print("Random Number Generator result are %s" % lottery_generator())