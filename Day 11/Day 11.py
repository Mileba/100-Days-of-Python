from art import logo
import random
def blackjack():
    print(logo)
    
    ############### Blackjack Project #####################
    ############### Our Blackjack House Rules #####################

    ## The deck is unlimited in size. 
    ## There are no jokers. 
    ## The Jack/Queen/King all count as 10.
    ## The the Ace can count as 11 or 1.
    ## Use the following list as the deck of cards:
    ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ## The cards in the list have equal probability of being drawn.
    ## Cards are not removed from the deck as they are drawn.
    ## The computer is the dealer.


    def calculate_score(list):
        if sum(list) == 21 and len(list) == 2:
            return 0
        if 11 in list and sum(list) > 21:
            list.remove(11)
            list.append(1)
        return sum(list)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card


    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your current card {user_cards}, current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")
            

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            round = input("Press 'y' to draw another card, press 'n' to pass: ")
            if round == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    def compare(user,comp):
        print(f"Your final card: {user_cards}, final score: {user_score}")
        print(f"Computer's card: {computer_cards}, final score: {computer_score}")
        if user == comp: 
            print("Draw")
        elif comp == 0:
            print("You Lose, He has a blackjack")
        elif user == 0:
            print("You won with a blackjack")
        elif user > 21:
            print("This is a bust, You drew over 21")
        elif comp > 21:
            print("You win, He has over 21")
        elif comp > user:
            print("You lose")
        else:
            print("You Win")
            

    compare(user_score,computer_score)
    
    continue_game = input("Type 'y' to continue the game or 'n' to end the game: ")
    
    if continue_game == "y":
        blackjack()
            
blackjack()
