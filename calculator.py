"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic_org import *


# Your code goes here
while True:
    my_input = raw_input(">>> ")
    token = my_input.split()
    if token[0] is 'q':
        break
    else:
        if len(token) > 1:
            for item in range(1, len(token)):
                try:
                    token[item] = float(token[item])
                except:
                    print("ValueError: That is not a number!")
            if token[0] is '+':
                print(my_reduce(add, token[1:]))
            elif token[0] is '-':
                print(my_reduce(subtract, token[1:]))
            elif token[0] is '*':
                print(my_reduce(multiply, token[1:]))
            elif token[0] is '/':
                print(my_reduce(divide, token[1:]))
            elif token[0] == 'square':
                for num in token[1:]:
                    print(square(num))
            elif token[0] == 'cube':
                for num in token[1:]:
                    print(cube(num))
            elif token[0] == 'power':
                print(my_reduce(power, token[1:]))
            elif token[0] == 'mod':
                print(my_reduce(mod, token[1:]))
        else:
            print("I don't understand.")
