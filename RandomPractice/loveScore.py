name_one = input("Enter your first and last name: \n")
name_two = input("Enter your partners first and last name: \n")

new_one = name_one.lower()
new_two = name_two.lower()
names = new_one + new_two

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t+r+u+e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l+o+v+e

score = str(true) + str(love)

new_score = int(score)

if (new_score < 10) or (new_score > 90):
    print(f"Your love score is {score}, you go together like coke and mentos")
elif (new_score >= 40) and (new_score <= 50):
    print(f"You score is {score}, you are alright together.")
else:
    print(f"Your score is {score}. Womp womp.")