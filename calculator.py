"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    my_input = raw_input(">>> ")
    token = my_input.split(" ")
    token[1] = int(token[1])
    token[2] = int(token[2])
    if token[0] is 'q':
        break
    else:
        if token[0] is '+':
            print(add(token[1], token[2]))
        elif token[0] is '-':
            print(subtract(token[1], token[2]))
        elif token[0] is '*':
            print(multiply(token[1], token[2]))
        elif token[0] is '/':
            print(divide(token[1], token[2]))
        elif token[0] == 'square':
            print(square(token[1], token[2]))
        elif token[0] == 'cube':
            print(cube(token[1], token[2]))
        elif token[0] == 'power':
            print(power(token[1], token[2]))
        elif token[0] == 'mod':
            print(mod(token[1], token[2]))
        else:
            print("I don't understand.")
