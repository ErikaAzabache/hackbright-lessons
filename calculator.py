"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


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
                    token[item] = int(token[item])
                except:
                    print("ValueError: That is not a number!")
            if token[0] is '+':
                print(add(token[1:]))
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
