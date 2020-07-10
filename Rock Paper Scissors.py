import random

Player1 = input("Hello, welcome to Rock Paper Scissors. What's your name? ")
Player2 = "Computer"
Playing = True

def result(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "It's a draw"
    elif player_hand == 0 and computer_hand == 1:
        return Player1 + " loses"
    elif player_hand == 1 and computer_hand == 2:
        return Player1 + " loses"
    elif player_hand == 2 and computer_hand == 0:
        return Player1 + " loses"
    else:
        return Player1 + " wins"

hands = ["rock", "paper", "scissors"]

def print_hand(hand, player):
    print(player, "chose", hands[hand])

while Playing:
    print("Let's begin! Rock is 0, paper is 1 and scissors is 2.", Player1, "goes first.")
    player_hand = int(input("Rock, paper, scissors? (Enter a number: 0, 1, 2) "))

    computer_hand = random.randint(0, 2)


    print_hand(player_hand, Player1)
    print_hand(computer_hand, Player2)

    print(result(player_hand, computer_hand))

    y_n = ""
    while y_n != "Yes" and y_n != "yes" and y_n != "No" and y_n != "no":
        y_n = input("Play again? ")
        if y_n == "Yes" or y_n == "yes":
            Playing = True  
        elif y_n == "No" or y_n == "no":
            Playing = False