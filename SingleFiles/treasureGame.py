print("Welcome to Treasure Island.\n Your mission is to find the treasure.\n")

q_one = input("You come to a fork in the road, do you want to go 'left' or 'right'?\n")

if q_one == "right":
    print("Game over, you lose.")
else:
    q_two = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if q_two == "swim":
        print("You get eaten by a fish, game over.")
    else:
        q_three = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if q_three == "red":
            print("Game Over")
        elif q_three == "blue":
            print("Game Over")
        else:
            print("You win!")