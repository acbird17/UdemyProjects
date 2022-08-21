import random
import os
from gamedata import data

def clear():
    os.system('clear')

def get_random_celeb():
    return random.choice(data)

def format_data(celebrity):
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
    print(celebrity["follower_count"])
    return f"{name}, who is a {description} from {country}."

def check_answer(guess, a_follower, b_followers):
    if a_follower > b_followers:
        return guess == "a"
    else:
        return guess == "b"    

def run_game():
    score = 0
    game_continue = True
    celeb_a = get_random_celeb()
    celeb_b = get_random_celeb()

    while game_continue:
        celeb_a = celeb_b
        celeb_b = get_random_celeb()
        while celeb_a == celeb_b:
            celeb_b = get_random_celeb()

        print(f"Compare A: {format_data(celeb_a)}.")
        print("VS")
        print(f"Against B: {format_data(celeb_b)}.")
        
        guess = input("Who do you think has more Instagram followers? 'A' or 'B': ").lower()
        a_followers = celeb_a["follower_count"]
        b_followers = celeb_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)
        
        clear()

        if is_correct:
            score += 1
            print(f"You are correct, your score is {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Your final score is {score}.")
        

run_game()