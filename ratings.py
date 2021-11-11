"""Restaurant rating lister."""

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
    
   

def user_choice():
    print("Would you like to see all the ratings in alphabetical order, add a new restaurant, or quit?\nEnter '1' to see all ratings.\nEnter '2' to add a new restaurant.\nEnter 3 to quit.")
    choice = input()
    if choice == '1':
        sort_scores()
    elif choice == '2':
        new_restaurant()
    elif choice == '3':
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
