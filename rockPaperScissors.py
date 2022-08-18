import random


rock = '''
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
        ______)
        _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
        ______)
    __________)
    (____)
---.__(___)
'''

    #Write your code below this line 👇

user_input = input("Enter 'Rock', 'Paper, or 'Scissors'\n")
user_upper = user_input.lower()

ran_list = ["rock", "paper", "scissors"]

num = random.randint(0,2)

computer_choice = ran_list[num]

if user_upper == "rock" and computer_choice == "paper":
    print(f"{paper}\nComputer chose Paper, you lose!")
elif user_upper == "rock" and computer_choice == "scissors":
    print(f"{scissors}\nComputer chose Scissors, you win!!!")
elif user_upper == "paper" and computer_choice == "rock":
    print(f"{rock}\nComputer chose Rock, you win!!!") 
elif user_upper == "paper" and computer_choice == "scissors":
    print(f"{scissors}\nComputer chose Rock, you win!!!") 
elif user_upper == "scissors" and computer_choice == "rock":
    print(f"{rock}\nComputer chose Rock, you lose!") 
elif user_upper == "scissors" and computer_choice == "paper":
    print(f"{paper}\nComputer chose Paper, you win!!!") 
elif user_upper == computer_choice:
    print(f"It's a draw, play again.") 

    # check = input("Do you want to quit or start again? enter Y to restart or another key to end:\n")
    # if check.lower() == "y": #go back to the top
    #     continue    
    # print("Bye...")
    # break #exit)