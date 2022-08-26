import random
import os

def clear():
    os.system('clear')

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return(sum(cards))

def compare_scores(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        return "Bust, you lose."
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Dealer has Blackjack, you lose."
    elif user_score == 0:
        return "Blackjack, You Win!"
    elif user_score > 21:
        return "Bust, you lose."
    elif dealer_score > 21:
        return "Dealer Bust, You Win!"
    elif user_score > dealer_score:
        return "You Win."
    else:
        return "You lose"
        
def start_game():
    dealer_cards = []
    user_cards = []
    game_finished = False
    for _ in range(2):
        user_cards.append(draw_card())
        dealer_cards.append(draw_card())
    while not game_finished:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, your current score is: {user_score}.")
        print(f"Dealer's first card is: {dealer_cards[0]}.")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_finished = True
        else:
            user_deal = input("     Type 'y' to get another  card, or type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(draw_card())
            else:
                game_finished = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}.")
    print(f"Dealers final hand: {dealer_cards}, final score: {dealer_score}.")
    print(compare_scores(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    start_game()