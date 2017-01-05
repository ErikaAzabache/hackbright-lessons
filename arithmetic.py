def add(list_o_nums):
    answer = 0
    for num in list_o_nums:
        answer += num
    return answer


def subtract(*args):
    return num1 - num2


def multiply(*args):
    return num1 * num2


def divide(*args):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2)


def square(*args):
    # Needs only one argument
    return args ** 2


def cube(*args):
    # Needs only one argument
    return args ** 3


def power(*args):
    return num1 ** num2  # ** = exponent operator


def mod(*args):
    return num1 % num2
