# your code goes here


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
new_restaurant = raw_input("Enter new restaurant:")
new_rating = raw_input("Enter rating for new restaurant:")

restaurant_rating_dict[new_restaurant] = new_rating
print_ratings(restaurant_rating_dict)
