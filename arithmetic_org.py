def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2)


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2


def my_reduce(function, tokens):
    if function == add:
        res = 0
        for num in tokens:
            res = add(res, num)
    elif function == subtract:
        res = tokens[0]
        for num in tokens[1:]:
            res = subtract(res, num)
    elif function == multiply:
        res = 1
        for num in tokens:
            res = multiply(res, num)
    elif function == divide:
        res = tokens[0]
        for num in tokens[1:]:
            res = divide(res, num)
    elif function == power:
        res = tokens[0]
        for num in tokens[1:]:
            res = power(res, num)
    elif function == mod:
        res = tokens[0]
        for num in tokens[1:]:
            res = mod(res, num)
    else:
        print "I don't know this function"
    return "{0:.4f}".format(res)
