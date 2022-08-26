import os
import random

def clear():
    os.system('clear')

def start_game():
    clear()
    random_num = random.randint(1, 101)
    print(random_num)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts remaining.")
    if difficulty == "hard":
        attempts = 5
        print("You have 5 attempts remaining.")
    while attempts > 0:
        user_num = int(input("Make a guess: "))
        if user_num == random_num:
            print(f"You got it! The answer is {user_num}")
            return
        elif user_num < random_num:
            attempts -= 1
            print(f"Too Low\nGuess Again\nYou have {attempts} attempts remaining.")
        elif user_num > random_num:
            attempts -= 1
            print(f"Too High\nGuess Gain\nYou have {attempts} attempts remaining.")

start_game()
