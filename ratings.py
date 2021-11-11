"""Restaurant rating lister."""

scores_txt = open('scores.txt')

scores = {}

for line in scores_txt:
    line = line.rstrip()
    restaurant, score = line.split(":")
    scores[restaurant] = int(score)

def sort_scores():    
    for name, rating in sorted(scores.items()):
        print(f"{name} is rated at {rating}.")

sort_scores()
while True:
    print('Would you like to rate a new restaurant?\nEnter "Yes" if you would like to.')
    response = input()
    if response == 'Yes':
        print('Please enter the name of the restaurant.')
        new_name = input()
        print('Please enter the rating for the restaurant')
        new_rating = input()
        scores[new_name] = new_rating
        sort_scores()
    else:
        break