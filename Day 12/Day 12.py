from art import logo
import random

print(logo)
print("Welcome to The number guessing game")
rand_number = random.randrange(0, 100)
print(rand_number)
diff = input("Choose a difficulty, Type 'easy' or 'hard': ")
difficulty = diff.lower()
number_of_tries = 0
if difficulty == "easy":
    number_of_tries = 10
elif difficulty == "hard":
    number_of_tries = 5
else:
    print("Choose your difficulty")
is_game_over = False

while not is_game_over:

    print(f"You have {number_of_tries} attempt left")
    guess = int(input("Make a guess: "))
    if guess > rand_number:
        print("Too high")
        number_of_tries -= 1
    elif guess < rand_number:
        print("Too low")
        number_of_tries -= 1
    else:
        print("You win")
        is_game_over = True
    
    if number_of_tries == 0:
        print("You have run out of moves... Game Over")
        is_game_over = True