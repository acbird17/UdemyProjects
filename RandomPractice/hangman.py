import random
from hangman_art import stages, logo
from hangman_words import word_list
import os

def clear():
    os.system('clear')

print(logo)
game_is_finished = False
lives = len(stages) - 1

word = random.choice(word_list)
word_length = len(word)

dashes = []
for letters in word:
    dashes += "_"
print(f"Welcome to Hangman, here is your starting word: {' '.join(dashes)}")

wrong_letters = []

while not game_is_finished:
    guess = input("Please enter a letter:\n").lower()
    clear()
    if guess in dashes:
        print(f"You've already guessed {guess}.")
    for index in range(word_length):
        letter = word[index]
        if letter == guess:
            dashes[index] = letter
    print(f"{' '.join(dashes)}")
    
    if guess not in word:
        wrong_letters.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.\nHere are your incorrect letters: {wrong_letters}")        
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You ran out of guess, you lose.")
    if not "_" in dashes:
        game_is_finished = True
        print("You win!")

    print(stages[lives])
