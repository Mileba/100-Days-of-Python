from art import logo
from art import vs
from data import data
import random

is_game_over = False

def compare(first_ques,second_ques):
    if first_ques > second_ques:
        return "A"
    else:
        return "B"
    
score = 0

while not is_game_over:

    print(logo)

    
    if score > 0:
        print(f"You have scored {score} point")


    first_question = data[random.randrange(0,len(data))]
    print(f"Compare A: {first_question['name']}, a {first_question['description']}, from {first_question['country']}")
    #print(f"{first_question['follower_count']}")

    print(vs)

    second_question = data[random.randrange(0,len(data))]
    print(f"Compare B: {second_question['name']}, a {second_question['description']}, from {second_question['country']}")
    #print(f"{second_question['follower_count']}")


    compared_score = compare(first_question['follower_count'],second_question['follower_count'])
    #print(compared_score)
    game_input = input("Who has more followers, Type 'A' or 'B': ").upper()

    if game_input == compared_score:
        score += 1
        print(score)
    else:
        print(f"Your Score is {score}")
        is_game_over = True
