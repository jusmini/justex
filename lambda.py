# def hello():
#     return 'Hello'


# my_function = lambda param1, param2: param1 + param2
#
# print(my_function(4, 5))

my_function = lambda: 5

print(my_function())


def zero(function=None):
    return function(0) if function else 0


def one(function=None):
    return function(1) if function else 1


def two(function=None):
    return function(2) if function else 2


def three(function=None):
    return function(3) if function else 3


def four(function=None):
    return function(4) if function else 4


def five(function=None):
    return function(5) if function else 5


def six(function=None):
    return function(6) if function else 6


def seven(function=None):
    return function(7) if function else 7


def eight(function=None):
    return function(8) if function else 8


def nine(function=None):
    return function(9) if function else 9


def plus(number):
    return lambda param: param + number


def minus(number):
    return lambda param: param - number


def times(number):
    return lambda param: param * number


def divided_by(number):
    return lambda param: param // number if number != 0 else 0


print(seven(times(five())))