"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_my_hometown(town):
    """Determines if town is my hometown.
        For example:

        >>> is_my_hometown("Chicago")
        False
        >>> is_my_hometown("Lima")
        True
    """

    my_home_town = "Lima"
    return (town == my_home_town)

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def full_name(name, lastname):
    """ Returns first name and last name concatenated.
        For example:

        >>> full_name("Erika", "Azabache")
        'Erika Azabache'
    """

    return name + ' ' + lastname

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def fullname_and_town(name, lastname, town):
    """Prints a greeting for a given name and last name. Tells you if you and I
       are from the same hometown
       For example:

       >>> fullname_and_town("Boli", "The Cat", "San Jose")
       Hi, Boli The Cat, where are you from?
    """
    fullname = full_name(name, lastname)
    if is_my_hometown(town):
        print "Hi, "+ fullname + ", we're from the same place!"
    else:
        print "Hi, "+ fullname + ", where are you from?"

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry.
        For example:

        >>> is_berry("cherry")
        True

        >>> is_berry("orange")
        False
    """

    berry_list = ["strawberry", "cherry", "blackberry"]
    return fruit in berry_list


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    return lst + [num]


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, two_letters_state, tax_decimal = 0.05):
    valid_abreviations = ["AL", "AK", "AZ", "CA", "CO", "CT", "DE", "DC", "FL",
     "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", 
     "MI", "MN", "MS", "MO", "MT", "NB", "NV", "NH", "NJ", "NM", "NY", "NC", 
     "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
     "VA", "WA", "WV", "WI", "WY"]

    if two_letters_state not in valid_abreviations:
        raise Exception("Invalid State")

    extra_fees = 0

    if two_letters_state == "CA":
        extra_fees = base_price * 0.03
    elif two_letters_state == "PA":
        extra_fees = 2.0
    elif two_letters_state == "MA":
        if base_price < 100:
            extra_fees = 1.0
        else:
            extra_fees = 3.0

    return base_price * (1.0 + tax_decimal) + extra_fees


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_args(lst, *args):
    """Appends a variable number of arguments to a given list.
    Example:
    >>> append_args([1, 2, 3], 2, 3, 4)
    [1, 2, 3, 2, 3, 4]
    """
    return lst + list(args)


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
def outer(word):
    """Takes a word and returns the same word and the word multiplied by 3
    >>> outer("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
    """
    def multiply_by_3(word):
        return word * 3
        
    return (word, multiply_by_3(word))


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
