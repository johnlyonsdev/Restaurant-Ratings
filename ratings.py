"""Restaurant rating lister."""

import random

def sort_scores():    
    for name, rating in sorted(scores.items()):
        print(f"{name} is rated at {rating}.")
    user_choice()

def new_restaurant():
    print('Please enter the name of the restaurant.')
    new_name = input()
    while True:
        print('Please enter a rating between 1 and 5 for the restaurant.')
        new_rating = input()
        valid = False
        good_rating = ["1","2","3","4","5"]
        for item in good_rating:
            if item == new_rating:
                valid = True
        if valid != True:
            print("That is not a valid rating between 1 and 5.")
        else:
            break
    scores[new_name] = new_rating
    user_choice()
    
def random_update():
    name, rating = random.choice(list(scores.items()))
    print(f"Your random restaurant is {name} which has a rating of {rating}.")
    print("What would you like the new rating to be?\nPlease enter a rating between 1 and 5 for the restaurant.")
    new_rating = input()
    valid = False
    good_rating = ["1","2","3","4","5"]
    for item in good_rating:
        if item == new_rating:
            valid = True
        if valid != True:
            print("That is not a valid rating between 1 and 5.")
        else:
            break
    d1 = {name: new_rating}
    scores.update(d1)
    user_choice()
   
def choose_update():
    while True:
        print("Please enter the name of the restaurant you would like to update.")
        chosen_name = input()
        match = False
        for name, rating in scores.items():
            if name == chosen_name:
                match = True
        if match == False:
            print('Please enter a valid restaurant name.')
        else:
            break
    print("What would you like the new rating to be?\nPlease enter a rating between 1 and 5 for the restaurant.")
    new_rating = input()
    valid = False
    good_rating = ["1","2","3","4","5"]
    for item in good_rating:
        if item == new_rating:
            valid = True
        if valid != True:
            print("That is not a valid rating between 1 and 5.")
        else:
            break
    d1 = {chosen_name: new_rating}
    scores.update(d1)
    user_choice()



def user_choice():
    print("Would you like to see all the ratings in alphabetical order, add a new restaurant, update a random restaurant, update a chosen restaurant, or quit?\nEnter '1' to see all ratings.\nEnter '2' to add a new restaurant.\nEnter '3' to update a random restaurant.\nEnter '4' to update a chosen restaurant.\nEnter '5' to quit.")
    choice = input()
    if choice == '1':
        sort_scores()
    elif choice == '2':
        new_restaurant()
    elif choice == '3':
        random_update()
    elif choice == '4':
        choose_update()
    elif choice == '5':
        exit()
    else:
        print('Please enter a valid rating.')
        user_choice()


scores_txt = open('scores.txt')

scores = {}

for line in scores_txt:
    line = line.rstrip()
    restaurant, score = line.split(":")
    scores[restaurant] = int(score)

user_choice()
