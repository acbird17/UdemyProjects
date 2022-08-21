year = int(input("Enter a year to see if it is a leap year or not:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
         print("This is a leap year")
    else:
        print("This is not a leap year")
else:
    print("This is a leap year")
