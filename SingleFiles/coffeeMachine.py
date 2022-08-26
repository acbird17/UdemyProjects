import random
import os

def clear():
    os.system('clear')
    
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How man dimes?: ")) * .10
    total += int(input("How man nickels?: ")) * .05
    total += int(input("How man pennies?: ")) * .01
    return total
    
def is_resources(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True
    
def check_transaction(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(choice, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {choice}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like to drink? 'Espresso', 'Latte', 'Cappuccino': ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources(drink["ingredients"]):
            payment = coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])