# your code goes here
import sys

def ratings_dictionary(filename):
    restaurant_rating_file = open(filename)
    restaurant_rating_dict = {}
    for line in restaurant_rating_file:
        restaurant, score = line.rstrip().split(':') #list with two words: name of rest & rating
        restaurant_rating_dict[restaurant] = score
    restaurant_rating_file.close
    return restaurant_rating_dict


def print_ratings(ratings_dictionary):
    for restaurant_name, restaurant_rating in sorted(ratings_dictionary.items()):
        print "%s is rated at %s" % (restaurant_name, restaurant_rating)

while True:
    print "\nHi! please enter 1 to see all ratings in alphabetical order."
    print "Or, please enter 2 to add a new restaurant and rating it."
    print "Or, please enter 3 to quit."

    choice = raw_input()

    if choice == '1':
        restaurant_rating_dict = ratings_dictionary("scores.txt")
        print_ratings(restaurant_rating_dict)
    elif choice == '2':
        restaurant_rating_dict = ratings_dictionary("scores.txt")
        new_restaurant = raw_input("Enter new restaurant:")
        new_rating = raw_input("Enter rating for new restaurant:")
        restaurant_rating_dict[new_restaurant] = new_rating
        print_ratings(restaurant_rating_dict)
    elif choice == '3':
        sys.exit(0)
    else:
        print "Enter one of the given options, please."