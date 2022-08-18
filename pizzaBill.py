from re import S


size = input("What size pizza do you want, S, M, L?\n")
pepperoni = input("Would you like to add Pepperoni to this pizza, type Y or N?\n")
cheese = input("Would you like to add extra cheese to this pizza, type Y or N\n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25
else: 
    print("Please enter a valid size.")
    
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3
    else: 
        print("Please enter a valid input.")

if cheese == "Y":
    bill += 1
elif cheese == "N":
    bill += 0
else:
    print("Please enter a valid input.")

print(f"Your final bill is ${bill}.")