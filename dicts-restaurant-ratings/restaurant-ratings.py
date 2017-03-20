# your code goes here
import sys
import random

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

restaurant_rating_dict = ratings_dictionary("scores.txt")
while True:
    print "\nHi! please enter 1 to see all ratings in alphabetical order."
    print "Or, please enter 2 to add a new restaurant and rating it."
    print "Or, please enter 3 to update a random restaurant's rating."
    print "Or, please enter 4 to update a chosen restaurant's rating."
    print "Or, please enter 5 to quit."

    choice = raw_input()

    if choice == '1':
        print_ratings(restaurant_rating_dict)
    elif choice == '2':
        new_restaurant = raw_input("Enter new restaurant: ")
        new_rating = raw_input("Enter rating for new restaurant: ")
        restaurant_rating_dict[new_restaurant] = new_rating
        print_ratings(restaurant_rating_dict)
    elif choice == '3':
        random_restaurant = random.choice(restaurant_rating_dict.keys())
        print "Please rate %s: " % random_restaurant
        new_rating = raw_input()
        restaurant_rating_dict[random_restaurant] = new_rating
        print_ratings(restaurant_rating_dict)
    elif choice == '4':
        updated_restaurant = raw_input("Enter the name of the restaurant: ")    
        new_rating = raw_input("Enter rating for this restaurant: ")
        restaurant_rating_dict[updated_restaurant] = new_rating
        print_ratings(restaurant_rating_dict)
    elif choice == '5':
        sys.exit(0)
    else:
        print "Enter one of the given options, please."